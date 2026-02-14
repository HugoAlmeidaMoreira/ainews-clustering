import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def _parse_cols(raw: str | None) -> list[str] | None:
    if raw is None:
        return None
    cols = [c.strip() for c in raw.split(",") if c.strip()]
    return cols or None


def _resolve_columns(
    df: pd.DataFrame,
    numeric_cols: list[str] | None,
    categorical_cols: list[str] | None,
    excluded_cols: set[str],
) -> tuple[list[str], list[str]]:
    if numeric_cols is None:
        inferred = df.select_dtypes(include=[np.number]).columns.tolist()
        numeric_cols = [c for c in inferred if c not in excluded_cols]
    else:
        numeric_cols = [c for c in numeric_cols if c not in excluded_cols]

    if categorical_cols is None:
        inferred = df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
        categorical_cols = [c for c in inferred if c not in excluded_cols]
    else:
        categorical_cols = [c for c in categorical_cols if c not in excluded_cols]

    for col in numeric_cols + categorical_cols:
        if col not in df.columns:
            raise ValueError(f"Coluna não encontrada: {col}")

    overlap = set(numeric_cols).intersection(set(categorical_cols))
    if overlap:
        raise ValueError(f"Colunas repetidas entre numéricas e categóricas: {sorted(overlap)}")

    return numeric_cols, categorical_cols


def _row_labels(df: pd.DataFrame, id_col: str | None) -> list[str]:
    if id_col:
        if id_col not in df.columns:
            raise ValueError(f"id-col '{id_col}' não existe no CSV")
        return df[id_col].astype(str).tolist()
    return [f"x{i + 1}" for i in range(len(df))]


def _distance(a_num, b_num, a_cat, b_cat, metric: str) -> float:
    if metric == "euclidean":
        return float(np.sqrt(np.sum((a_num - b_num) ** 2)))
    if metric == "manhattan":
        return float(np.sum(np.abs(a_num - b_num)))
    if metric == "hamming":
        return float(np.sum(a_cat != b_cat))
    if metric == "mixed":
        man = float(np.sum(np.abs(a_num - b_num))) if len(a_num) else 0.0
        ham = float(np.sum(a_cat != b_cat)) if len(a_cat) else 0.0
        return man + ham
    raise ValueError(f"Métrica inválida: {metric}")


def _distance_matrix(
    df: pd.DataFrame,
    numeric_cols: list[str],
    categorical_cols: list[str],
    metric: str,
) -> np.ndarray:
    num = df[numeric_cols].to_numpy(dtype=float) if numeric_cols else np.zeros((len(df), 0))
    cat = (
        df[categorical_cols].astype(str).to_numpy()
        if categorical_cols
        else np.empty((len(df), 0), dtype=object)
    )

    n = len(df)
    mat = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(i + 1, n):
            d = _distance(num[i], num[j], cat[i], cat[j], metric)
            mat[i, j] = d
            mat[j, i] = d
    return mat


def _matrix_to_markdown_table(labels: list[str], matrix: np.ndarray) -> str:
    header = "|   | " + " | ".join(labels) + " |"
    sep = "|---|" + "|".join(["---" for _ in labels]) + "|"
    rows = [header, sep]
    for i, label in enumerate(labels):
        vals = []
        for j in range(len(labels)):
            if i == j:
                vals.append("0")
            else:
                vals.append(f"{matrix[i, j]:.4f}")
        rows.append("| " + label + " | " + " | ".join(vals) + " |")
    return "\n".join(rows)


def _silhouette_values(distance_matrix: np.ndarray, clusters: list[str]) -> np.ndarray:
    n = len(clusters)
    sil = np.zeros(n, dtype=float)
    unique_clusters = sorted(set(clusters))

    cluster_indices = {c: [i for i, cc in enumerate(clusters) if cc == c] for c in unique_clusters}

    for i in range(n):
        c_i = clusters[i]
        same = [idx for idx in cluster_indices[c_i] if idx != i]

        a_i = 0.0
        if same:
            a_i = float(np.mean([distance_matrix[i, j] for j in same]))

        b_i = float("inf")
        for c in unique_clusters:
            if c == c_i:
                continue
            other = cluster_indices[c]
            if not other:
                continue
            mean_dist = float(np.mean([distance_matrix[i, j] for j in other]))
            b_i = min(b_i, mean_dist)

        if b_i == float("inf"):
            sil[i] = 0.0
        else:
            denom = max(a_i, b_i)
            sil[i] = 0.0 if denom == 0 else (b_i - a_i) / denom
    return sil


def _purity(classes: list[str], clusters: list[str]) -> float:
    if len(classes) != len(clusters):
        raise ValueError("classes e clusters com tamanhos diferentes")

    df_eval = pd.DataFrame({"class": classes, "cluster": clusters})
    total = len(df_eval)
    best_sum = 0
    for _, group in df_eval.groupby("cluster"):
        best_sum += int(group["class"].value_counts().max())
    return best_sum / total if total else 0.0


def cmd_dist(args):
    df = pd.read_csv(args.csv)
    labels = _row_labels(df, args.id_col)

    excluded = {c for c in [args.id_col, args.cluster_col, args.class_col] if c}
    numeric_cols, categorical_cols = _resolve_columns(
        df,
        _parse_cols(args.numeric_cols),
        _parse_cols(args.categorical_cols),
        excluded,
    )

    matrix = _distance_matrix(df, numeric_cols, categorical_cols, args.metric)

    lines = [
        "# Distâncias do Exame",
        "",
        f"- CSV: `{args.csv}`",
        f"- Métrica: `{args.metric}`",
        f"- Numéricas: {numeric_cols}",
        f"- Categóricas: {categorical_cols}",
        "",
        "## Matriz de distância",
        "",
        _matrix_to_markdown_table(labels, matrix),
        "",
    ]

    text = "\n".join(lines)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"Relatório gravado em: {args.out}")
    else:
        print(text)


def cmd_cluster(args):
    df = pd.read_csv(args.csv)
    if args.cluster_col not in df.columns:
        raise ValueError(f"cluster-col '{args.cluster_col}' não existe no CSV")

    labels = _row_labels(df, args.id_col)
    excluded = {c for c in [args.id_col, args.cluster_col, args.class_col] if c}
    numeric_cols, categorical_cols = _resolve_columns(
        df,
        _parse_cols(args.numeric_cols),
        _parse_cols(args.categorical_cols),
        excluded,
    )

    matrix = _distance_matrix(df, numeric_cols, categorical_cols, args.metric)
    clusters = df[args.cluster_col].astype(str).tolist()
    sil = _silhouette_values(matrix, clusters)

    lines = [
        "# Métricas de Clustering",
        "",
        f"- CSV: `{args.csv}`",
        f"- cluster-col: `{args.cluster_col}`",
        f"- Métrica: `{args.metric}`",
        f"- Numéricas: {numeric_cols}",
        f"- Categóricas: {categorical_cols}",
        "",
        "## Silhouette por observação",
        "",
        "| obs | cluster | silhouette |",
        "|---|---|---|",
    ]

    for obs, c, s in zip(labels, clusters, sil):
        lines.append(f"| {obs} | {c} | {s:.4f} |")

    lines.extend(
        [
            "",
            f"- Silhouette média global: `{float(np.mean(sil)):.4f}`",
            "",
            "## Silhouette média por cluster",
            "",
            "| cluster | média silhouette | tamanho |",
            "|---|---|---|",
        ]
    )

    for c in sorted(set(clusters)):
        idx = [i for i, cc in enumerate(clusters) if cc == c]
        lines.append(f"| {c} | {float(np.mean(sil[idx])):.4f} | {len(idx)} |")

    if args.silhouette_of:
        if args.silhouette_of not in labels:
            raise ValueError(
                f"silhouette-of '{args.silhouette_of}' não encontrado nos ids: {labels}"
            )
        idx = labels.index(args.silhouette_of)
        lines.extend(["", f"- Silhouette `{args.silhouette_of}`: `{sil[idx]:.4f}`"])

    if args.class_col:
        if args.class_col not in df.columns:
            raise ValueError(f"class-col '{args.class_col}' não existe no CSV")
        purity = _purity(df[args.class_col].astype(str).tolist(), clusters)
        lines.extend(["", f"## Purity", "", f"- Purity: `{purity:.4f}`"])

    text = "\n".join(lines) + "\n"
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"Relatório gravado em: {args.out}")
    else:
        print(text)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Ferramenta mínima para cálculo rápido em exame (CSV -> distâncias e métricas)."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    dist = sub.add_parser("dist", help="Calcula matriz de distância")
    dist.add_argument("--csv", required=True, help="Caminho para CSV")
    dist.add_argument(
        "--metric",
        default="mixed",
        choices=["mixed", "euclidean", "manhattan", "hamming"],
        help="Métrica a usar",
    )
    dist.add_argument("--id-col", default=None, help="Coluna com id (ex: obs=x1,x2,...)" )
    dist.add_argument("--cluster-col", default=None, help="Ignorar coluna de cluster na distância")
    dist.add_argument("--class-col", default=None, help="Ignorar coluna de classe na distância")
    dist.add_argument("--numeric-cols", default=None, help="Lista separada por vírgulas")
    dist.add_argument("--categorical-cols", default=None, help="Lista separada por vírgulas")
    dist.add_argument("--out", default=None, help="Saída markdown opcional")
    dist.set_defaults(func=cmd_dist)

    cluster = sub.add_parser(
        "cluster", help="Calcula silhouette (e purity opcional) para solução de clustering"
    )
    cluster.add_argument("--csv", required=True, help="Caminho para CSV")
    cluster.add_argument("--cluster-col", required=True, help="Coluna com rótulo de cluster")
    cluster.add_argument(
        "--metric",
        default="mixed",
        choices=["mixed", "euclidean", "manhattan", "hamming"],
        help="Métrica a usar",
    )
    cluster.add_argument("--id-col", default=None, help="Coluna com id (ex: obs=x1,x2,...)" )
    cluster.add_argument("--class-col", default=None, help="Coluna de classe para purity")
    cluster.add_argument("--numeric-cols", default=None, help="Lista separada por vírgulas")
    cluster.add_argument("--categorical-cols", default=None, help="Lista separada por vírgulas")
    cluster.add_argument(
        "--silhouette-of",
        default=None,
        help="ID de uma observação para destacar a silhouette (ex: x4)",
    )
    cluster.add_argument("--out", default=None, help="Saída markdown opcional")
    cluster.set_defaults(func=cmd_cluster)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
