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


def _agglomerative_final_merge_distance(distance_matrix: np.ndarray, linkage: str) -> float:
    clusters = [[i] for i in range(distance_matrix.shape[0])]

    while len(clusters) > 1:
        best_pair = None
        best_value = float("inf")

        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                c1 = clusters[i]
                c2 = clusters[j]
                pairwise = [distance_matrix[a, b] for a in c1 for b in c2]
                if linkage == "single":
                    d = float(min(pairwise))
                elif linkage == "complete":
                    d = float(max(pairwise))
                else:
                    raise ValueError(f"Linkage inválido: {linkage}")

                if d < best_value:
                    best_value = d
                    best_pair = (i, j)

        i, j = best_pair
        merged = clusters[i] + clusters[j]
        new_clusters = [clusters[k] for k in range(len(clusters)) if k not in (i, j)]
        new_clusters.append(merged)
        clusters = new_clusters

    return best_value


def _first_merge_pair(distance_matrix: np.ndarray) -> tuple[int, int, float]:
    n = distance_matrix.shape[0]
    best = None
    for i in range(n):
        for j in range(i + 1, n):
            d = float(distance_matrix[i, j])
            if best is None or d < best[2]:
                best = (i, j, d)
    return best


def cmd_agglom_demo(args):
    df = pd.read_csv(args.csv, index_col=False)
    labels = _row_labels(df, args.id_col)

    if len(df) != 3:
        raise ValueError("Este demo foi feito para 3 observações (x1, x2, x3)")

    for required in [args.y1_col, args.y2_col, args.reference_col]:
        if required not in df.columns:
            raise ValueError(f"Coluna obrigatória não encontrada: {required}")

    obs_to_idx = {obs: i for i, obs in enumerate(labels)}
    for obs in ["x1", "x2", "x3"]:
        if obs not in obs_to_idx:
            raise ValueError(
                f"Este demo espera ids x1,x2,x3 na coluna de ids. Recebidos: {labels}"
            )

    num_cols = [args.y1_col, args.y2_col]
    matrix = _distance_matrix(df, num_cols, [], metric="manhattan")

    i1, i2, i3 = obs_to_idx["x1"], obs_to_idx["x2"], obs_to_idx["x3"]
    d12 = float(matrix[i1, i2])
    d13 = float(matrix[i1, i3])
    d23 = float(matrix[i2, i3])

    final_single = _agglomerative_final_merge_distance(matrix, "single")
    first_i, first_j, first_d = _first_merge_pair(matrix)

    ref = df[args.reference_col].astype(str).tolist()
    sil_ref = _silhouette_values(matrix, ref)
    sil_x1 = float(sil_ref[i1])

    candidate_clusters = ["K1", "K2", "K2"]
    candidate_purity = _purity(ref, candidate_clusters)

    a_true = np.isclose(final_single, 2.0)
    b_true = np.isclose(d13, np.sqrt(5.0))
    c_true = np.isclose(sil_x1, 1.0 / 3.0, atol=1e-2)
    d_true = {labels[first_i], labels[first_j]} == {"x1", "x3"}
    e_true = np.isclose(candidate_purity, 2.0 / 3.0, atol=1e-2)

    lines = [
        "# Demo da Pergunta (Agglomerative + Manhattan)",
        "",
        f"- CSV: `{args.csv}`",
        f"- IDs: {labels}",
        f"- Variáveis numéricas: `{args.y1_col}`, `{args.y2_col}`",
        f"- Coluna de referência: `{args.reference_col}`",
        "",
        "## Distâncias Manhattan",
        "",
        f"- d(x1,x2) = {d12:.4f}",
        f"- d(x1,x3) = {d13:.4f}",
        f"- d(x2,x3) = {d23:.4f}",
        "",
        "## Avaliação das afirmações",
        "",
        f"- A) all observation are merged at distance 2 (single-link): {'TRUE' if a_true else 'FALSE'} (merge final = {final_single:.4f})",
        f"- B) d(x1,x3) = sqrt(5): {'TRUE' if b_true else 'FALSE'} (valor = {d13:.4f}, sqrt(5) = {np.sqrt(5):.4f})",
        f"- C) silhouette(x1) = 0.33 com referência perfeita: {'TRUE' if c_true else 'FALSE'} (valor = {sil_x1:.4f})",
        f"- D) x1 e x3 são o primeiro merge em complete-link: {'TRUE' if d_true else 'FALSE'} (primeiro merge = {labels[first_i]} & {labels[first_j]}, d={first_d:.4f})",
        f"- E) purity de {{x1}}{{x2,x3}} = 0.66: {'TRUE' if e_true else 'FALSE'} (valor = {candidate_purity:.4f})",
        "",
    ]

    text = "\n".join(lines)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"Relatório gravado em: {args.out}")
    else:
        print(text)


def _rows_matching(df: pd.DataFrame, conditions: dict[str, object]) -> pd.Series:
    mask = pd.Series([True] * len(df))
    for col, value in conditions.items():
        mask = mask & (df[col] == value)
    return mask


def _relative_support(df: pd.DataFrame, conditions: dict[str, object]) -> float:
    mask = _rows_matching(df, conditions)
    return float(mask.sum()) / float(len(df))


def _confidence(
    df: pd.DataFrame,
    antecedent: dict[str, object],
    consequent: dict[str, object],
) -> float:
    ant_mask = _rows_matching(df, antecedent)
    ant_count = int(ant_mask.sum())
    if ant_count == 0:
        return 0.0
    both_mask = ant_mask & _rows_matching(df, consequent)
    return float(both_mask.sum()) / float(ant_count)


def _lift(
    df: pd.DataFrame,
    antecedent: dict[str, object],
    consequent: dict[str, object],
) -> float:
    conf = _confidence(df, antecedent, consequent)
    sup_cons = _relative_support(df, consequent)
    if sup_cons == 0:
        return 0.0
    return conf / sup_cons


def _is_closed_pattern(
    df: pd.DataFrame,
    pattern: dict[str, object],
    candidate_cols: list[str],
) -> bool:
    base_mask = _rows_matching(df, pattern)
    base_sup = int(base_mask.sum())

    for col in candidate_cols:
        if col in pattern:
            continue
        values = df.loc[base_mask, col].unique().tolist()
        for value in values:
            extended = dict(pattern)
            extended[col] = value
            ext_sup = int(_rows_matching(df, extended).sum())
            if ext_sup == base_sup:
                return False
    return True


def cmd_patterns_demo(args):
    df = pd.read_csv(args.csv, index_col=False)
    labels = _row_labels(df, args.id_col)

    for col in [args.id_col, args.y1_col, args.y2_col, args.reference_col]:
        if col not in df.columns:
            raise ValueError(f"Coluna obrigatória não encontrada: {col}")

    df = df.copy()
    df[args.y1_col] = pd.to_numeric(df[args.y1_col], errors="raise")
    df[args.y2_col] = pd.to_numeric(df[args.y2_col], errors="raise")
    df[args.reference_col] = df[args.reference_col].astype(str).str.strip()

    obs_to_idx = {obs: i for i, obs in enumerate(labels)}
    for obs in ["x1", "x2", "x3"]:
        if obs not in obs_to_idx:
            raise ValueError(
                f"Este demo espera ids x1,x2,x3 na coluna de ids. Recebidos: {labels}"
            )

    row_x2 = df.iloc[obs_to_idx["x2"]]
    row_x3 = df.iloc[obs_to_idx["x3"]]

    bic_values = np.array(
        [
            [float(row_x2[args.y1_col]), float(row_x2[args.y2_col])],
            [float(row_x3[args.y1_col]), float(row_x3[args.y2_col])],
        ]
    )
    flattened = bic_values.flatten().tolist()
    mode_count = int(pd.Series(flattened).value_counts().max())
    constant_quality = mode_count / len(flattened)

    op_perfect = bool(
        (row_x2[args.y1_col] <= row_x2[args.y2_col])
        and (row_x3[args.y1_col] <= row_x3[args.y2_col])
    )

    conf_b = _confidence(
        df,
        antecedent={args.y1_col: 1, args.y2_col: 3},
        consequent={args.reference_col: "A"},
    )

    pattern = {args.y2_col: 3, args.reference_col: "A"}
    abs_sup_pattern = int(_rows_matching(df, pattern).sum())
    rel_sup_pattern = _relative_support(df, pattern)
    closed_pattern = _is_closed_pattern(
        df,
        pattern,
        candidate_cols=[args.y1_col, args.y2_col, args.reference_col],
    )

    lift_e = _lift(
        df,
        antecedent={args.y1_col: 1},
        consequent={args.reference_col: "A"},
    )

    a_true = np.isclose(constant_quality, 2.0 / 3.0, atol=1e-6)
    b_true = np.isclose(conf_b, 1.0, atol=1e-6)
    c_true = abs_sup_pattern >= 2 and closed_pattern
    d_true = op_perfect
    e_true = np.isclose(lift_e, 2.0 / 3.0, atol=1e-6)
    f_true = np.isclose(rel_sup_pattern, 2.0 / 3.0, atol=1e-6)

    lines = [
        "# Demo da Pergunta (Patterns + Biclustering)",
        "",
        f"- CSV: `{args.csv}`",
        f"- IDs: {labels}",
        f"- Colunas: `{args.y1_col}`, `{args.y2_col}`, `{args.reference_col}`",
        "",
        "## Cálculos-base",
        "",
        f"- Bicluster B=({{x2,x3}},{{{args.y1_col},{args.y2_col}}}) valores: {bic_values.tolist()}",
        f"- Quality(constant, modo/total) = {mode_count}/{len(flattened)} = {constant_quality:.4f}",
        f"- conf({{{args.y1_col}=1,{args.y2_col}=3}}=>A) = {conf_b:.4f}",
        f"- sup_abs({{{args.y2_col}=3,A}}) = {abs_sup_pattern}",
        f"- sup_rel({{{args.y2_col}=3,A}}) = {rel_sup_pattern:.4f}",
        f"- closed({{{args.y2_col}=3,A}}) = {closed_pattern}",
        f"- order-preserving perfeito em B (<=) = {op_perfect}",
        f"- lift({{{args.y1_col}=1}}=>A) = {lift_e:.4f}",
        "",
        "## Avaliação das afirmações",
        "",
        f"- a) quality constante de B = 2/3: {'TRUE' if a_true else 'FALSE'}",
        f"- b) confidence {{y1=1,y2=3}} => A é 100%: {'TRUE' if b_true else 'FALSE'}",
        f"- c) com minsup=2, padrão {{y2=3,A}} é closed: {'TRUE' if c_true else 'FALSE'}",
        f"- d) B=({{x2,x3}},{{y1,y2}}) é perfect order-preserving: {'TRUE' if d_true else 'FALSE'}",
        f"- e) lift {{y1=1}} => A é 2/3: {'TRUE' if e_true else 'FALSE'}",
        f"- f) suporte relativo {{y2=3,A}} é 2/3: {'TRUE' if f_true else 'FALSE'}",
        "",
    ]

    text = "\n".join(lines)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"Relatório gravado em: {args.out}")
    else:
        print(text)


def _parse_vector2(raw: str) -> tuple[float, float]:
    parts = [p.strip() for p in raw.split(",")]
    if len(parts) != 2:
        raise ValueError("Vetor deve ter exatamente 2 valores, ex: '1,1'")
    return float(parts[0]), float(parts[1])


def cmd_pca_demo(args):
    v1 = np.array([args.v1x, args.v1y], dtype=float)
    x = np.array(_parse_vector2(args.x), dtype=float)

    projection = float(np.dot(x, v1))

    expl_var_d = args.lambda1 / (args.lambda1 + args.lambda2_for_e)

    lambda2_from_80 = args.lambda1 * (1.0 - args.explained_ratio_d) / args.explained_ratio_d

    a_true = False
    b_true = np.isclose(projection, -0.35, atol=1e-6)
    c_true = True
    d_true = np.isclose(lambda2_from_80, 0.3, atol=1e-6)
    e_true = expl_var_d > 0.85

    lines = [
        "# Demo da Pergunta (PCA)",
        "",
        f"- v1 = [{args.v1x}, {args.v1y}]",
        f"- lambda1 = {args.lambda1}",
        f"- x = {x.tolist()}",
        f"- Razão explicada em d) para lambda1: {args.explained_ratio_d:.4f}",
        f"- lambda2 em e): {args.lambda2_for_e}",
        "",
        "## Cálculos-base",
        "",
        f"- Projeção 1D x·v1 = {projection:.4f}",
        f"- lambda2 em d): lambda2 = lambda1*(1-r)/r = {args.lambda1}*(1-{args.explained_ratio_d:.4f})/{args.explained_ratio_d:.4f} = {lambda2_from_80:.4f}",
        f"- Variância explicada de lambda1 em e): {args.lambda1}/({args.lambda1}+{args.lambda2_for_e}) = {expl_var_d:.4f}",
        "",
        "## Avaliação das afirmações",
        "",
        f"- a) LDA, tal como PCA, procura máxima variabilidade global: {'TRUE' if a_true else 'FALSE'}",
        f"- b) Projeção de x=(1,1) em v1 é -0.35: {'TRUE' if b_true else 'FALSE'} (valor={projection:.4f})",
        f"- c) PCA pode ser usada para compressão e reconstrução: {'TRUE' if c_true else 'FALSE'}",
        f"- d) Se lambda1 explica 80%, lambda2=0.3: {'TRUE' if d_true else 'FALSE'} (lambda2={lambda2_from_80:.4f})",
        f"- e) Se lambda2=0.5, lambda1 explica >85%: {'TRUE' if e_true else 'FALSE'} (explicação={expl_var_d:.4f})",
        "",
    ]

    text = "\n".join(lines)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"Relatório gravado em: {args.out}")
    else:
        print(text)


def cmd_dist(args):
    df = pd.read_csv(args.csv, index_col=False)
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
    df = pd.read_csv(args.csv, index_col=False)
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

    agglom_demo = sub.add_parser(
        "agglom-demo",
        help="Demonstra e avalia automaticamente a pergunta A-E de agglomerative clustering",
    )
    agglom_demo.add_argument("--csv", required=True, help="Caminho para CSV")
    agglom_demo.add_argument("--id-col", default="obs", help="Coluna com ids (default: obs)")
    agglom_demo.add_argument("--y1-col", default="y1", help="Coluna y1 (default: y1)")
    agglom_demo.add_argument("--y2-col", default="y2", help="Coluna y2 (default: y2)")
    agglom_demo.add_argument(
        "--reference-col",
        default="reference",
        help="Coluna com referência de clusters/classes (default: reference)",
    )
    agglom_demo.add_argument("--out", default=None, help="Saída markdown opcional")
    agglom_demo.set_defaults(func=cmd_agglom_demo)

    patterns_demo = sub.add_parser(
        "patterns-demo",
        help="Demonstra e avalia automaticamente a pergunta a-f (patterns e biclustering)",
    )
    patterns_demo.add_argument("--csv", required=True, help="Caminho para CSV")
    patterns_demo.add_argument("--id-col", default="obs", help="Coluna com ids (default: obs)")
    patterns_demo.add_argument("--y1-col", default="y1", help="Coluna y1 (default: y1)")
    patterns_demo.add_argument("--y2-col", default="y2", help="Coluna y2 (default: y2)")
    patterns_demo.add_argument(
        "--reference-col",
        default="reference",
        help="Coluna de classe/referência (default: reference)",
    )
    patterns_demo.add_argument("--out", default=None, help="Saída markdown opcional")
    patterns_demo.set_defaults(func=cmd_patterns_demo)

    pca_demo = sub.add_parser(
        "pca-demo",
        help="Demonstra e avalia automaticamente a pergunta de PCA (opções a-e)",
    )
    pca_demo.add_argument("--v1x", type=float, default=-0.86, help="Primeira coordenada de v1")
    pca_demo.add_argument("--v1y", type=float, default=0.51, help="Segunda coordenada de v1")
    pca_demo.add_argument("--lambda1", type=float, default=1.5, help="Valor de lambda1")
    pca_demo.add_argument(
        "--x",
        default="1,1",
        help="Vetor x para projeção no formato 'a,b' (default: 1,1)",
    )
    pca_demo.add_argument(
        "--explained-ratio-d",
        type=float,
        default=0.8,
        help="Percentagem de variância explicada em d) como fração (default: 0.8)",
    )
    pca_demo.add_argument(
        "--lambda2-for-e",
        type=float,
        default=0.5,
        help="Valor de lambda2 para avaliar opção e) (default: 0.5)",
    )
    pca_demo.add_argument("--out", default=None, help="Saída markdown opcional")
    pca_demo.set_defaults(func=cmd_pca_demo)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
