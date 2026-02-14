import pandas as pd
import numpy as np
import math
from itertools import combinations

DATASET_PATH = (
    "/home/hugo/git/personal/ainews-clustering/src/scripts/exam/dataset_exam_2022.csv"
)
OUTPUT_PATH = "/home/hugo/git/personal/ainews-clustering/src/scripts/exam/report.md"

CLUSTERS = [1, 2, 2, 1]  # C1: x1,x4 | C2: x2,x3 (exame 2022)
DISTANCE_TYPE = "manhattan"  # "euclidean", "manhattan"

df = pd.read_csv(DATASET_PATH)
df.columns = df.columns.str.strip()
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].str.strip()

output = []

output.append("# Relatório de Distâncias\n")

output.append("## Dataset")
output.append("```")
output.append(df.to_string(index=False))
output.append("```\n")

output.append(f"**Colunas:** {list(df.columns)}\n")

num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = df.select_dtypes(include=["object"]).columns.tolist()

output.append(f"- **Numéricas:** {num_cols}")
output.append(f"- **Categóricas:** {cat_cols}\n")

df_encoded = df.copy()
cat_mappings = {}

for col in cat_cols:
    unique_vals = df[col].unique()
    mapping = {val: i for i, val in enumerate(unique_vals)}
    cat_mappings[col] = mapping
    df_encoded[col] = df[col].map(mapping)

output.append("### Codificação Categóricas")
for col, mapping in cat_mappings.items():
    output.append(f"- **{col}:** {mapping}")

output.append("\n### Dados Codificados")
output.append("```")
output.append(df_encoded.to_string(index=False))
output.append("```\n")

points = df_encoded.values.astype(float)
labels = [f"P{i + 1}" for i in range(len(df))]
col_names = list(df_encoded.columns)
n = len(points)

output.append("## Resumo: Matrizes de Distância\n")


def euclidean(p1, p2):
    return math.sqrt(sum((v1 - v2) ** 2 for v1, v2 in zip(p1, p2)))


def manhattan(p1, p2):
    return sum(abs(v1 - v2) for v1, v2 in zip(p1, p2))


def minkowski(p1, p2, p):
    return sum(abs(v1 - v2) ** p for v1, v2 in zip(p1, p2)) ** (1 / p)


def chebyshev(p1, p2):
    return max(abs(v1 - v2) for v1, v2 in zip(p1, p2))


def hamming(p1, p2):
    return sum(1 for v1, v2 in zip(p1, p2) if v1 != v2)


def matrix_to_md(matrix, labels):
    header = "       " + "  ".join([f"{l:>6}" for l in labels])
    rows = [header]
    for i, row in enumerate(matrix):
        row_str = "  ".join(
            [f"{d:>6.2f}" if i != j else "   ---" for j, d in enumerate(row)]
        )
        rows.append(f"{labels[i]:>4}  {row_str}")
    return "\n".join(rows)


eucl_matrix = np.zeros((n, n))
manh_matrix = np.zeros((n, n))
cheb_matrix = np.zeros((n, n))
hamm_matrix = np.zeros((n, n))
mink_matrices = {p: np.zeros((n, n)) for p in [1, 2, 3]}

for i in range(n):
    for j in range(i + 1, n):
        eucl = euclidean(points[i], points[j])
        manh = manhattan(points[i], points[j])
        cheb = chebyshev(points[i], points[j])
        hamm = hamming(points[i], points[j])

        eucl_matrix[i, j] = eucl_matrix[j, i] = eucl
        manh_matrix[i, j] = manh_matrix[j, i] = manh
        cheb_matrix[i, j] = cheb_matrix[j, i] = cheb
        hamm_matrix[i, j] = hamm_matrix[j, i] = hamm

        for p in [1, 2, 3]:
            mink_matrices[p][i, j] = mink_matrices[p][j, i] = minkowski(
                points[i], points[j], p
            )

output.append("### Euclidiana")
output.append("```\n" + matrix_to_md(eucl_matrix, labels) + "\n```\n")

output.append("### Manhattan")
output.append("```\n" + matrix_to_md(manh_matrix, labels) + "\n```\n")

output.append("### Chebyshev (L∞)")
output.append("```\n" + matrix_to_md(cheb_matrix, labels) + "\n```\n")

output.append("### Hamming")
output.append("```\n" + matrix_to_md(hamm_matrix, labels) + "\n```\n")

output.append("### Minkowski (p=1)")
output.append("```\n" + matrix_to_md(mink_matrices[1], labels) + "\n```\n")

output.append("### Minkowski (p=2)")
output.append("```\n" + matrix_to_md(mink_matrices[2], labels) + "\n```\n")

output.append("### Minkowski (p=3)")
output.append("```\n" + matrix_to_md(mink_matrices[3], labels) + "\n```\n")

output.append("---\n")
output.append("## Cálculos Detalhados\n")

output.append("### Euclidiana\n")
output.append("Fórmula: $d(p,q) = \\sqrt{\\sum(p_i - q_i)^2}$\n")

for i in range(n):
    for j in range(i + 1, n):
        p1, p2 = points[i], points[j]
        output.append(f"**{labels[i]} vs {labels[j]}:**")
        output.append(f"- {labels[i]} = {p1}")
        output.append(f"- {labels[j]} = {p2}")
        squared = [(v1 - v2) ** 2 for v1, v2 in zip(p1, p2)]
        for k, (c, v1, v2, s) in enumerate(zip(col_names, p1, p2, squared)):
            output.append(f"  - {c}: ({v1} - {v2})² = {s}")
        output.append(f"- Soma: {squared} = {sum(squared)}")
        output.append(
            f"- Resultado: $\\sqrt{{{sum(squared)}}} = {euclidean(p1, p2):.4f}$\n"
        )

output.append("\n### Manhattan\n")
output.append("Fórmula: $d(p,q) = \\sum|p_i - q_i|$\n")

for i in range(n):
    for j in range(i + 1, n):
        p1, p2 = points[i], points[j]
        output.append(f"**{labels[i]} vs {labels[j]}:**")
        abs_diffs = [abs(v1 - v2) for v1, v2 in zip(p1, p2)]
        for k, (c, v1, v2, d) in enumerate(zip(col_names, p1, p2, abs_diffs)):
            output.append(f"  - {c}: |{v1} - {v2}| = {d}")
        output.append(f"- Soma: {abs_diffs} = {sum(abs_diffs)}\n")

output.append("\n### Chebyshev (L∞)\n")
output.append("Fórmula: $d_\\infty(p,q) = \\max(|p_i - q_i|)$\n")

for i in range(n):
    for j in range(i + 1, n):
        p1, p2 = points[i], points[j]
        output.append(f"**{labels[i]} vs {labels[j]}:**")
        abs_diffs = [abs(v1 - v2) for v1, v2 in zip(p1, p2)]
        for k, (c, v1, v2, d) in enumerate(zip(col_names, p1, p2, abs_diffs)):
            output.append(f"  - {c}: |{v1} - {v2}| = {d}")
        output.append(f"- Máximo: max({abs_diffs}) = {max(abs_diffs)}\n")

output.append("\n### Hamming\n")
output.append("Fórmula: número de atributos com valores diferentes\n")

for i in range(n):
    for j in range(i + 1, n):
        p1, p2 = points[i], points[j]
        output.append(f"**{labels[i]} vs {labels[j]}:**")
        diffs = [1 if v1 != v2 else 0 for v1, v2 in zip(p1, p2)]
        for k, (c, v1, v2, d) in enumerate(zip(col_names, p1, p2, diffs)):
            symbol = "≠" if d == 1 else "="
            output.append(f"  - {c}: {v1} {symbol} {v2} → {d}")
        output.append(f"- Total: sum({diffs}) = {sum(diffs)}\n")

for p in [1, 2, 3]:
    output.append(f"\n### Minkowski (p={p})\n")
    output.append(f"Fórmula: $d(p,q) = (\\sum|p_i - q_i|^{{p}})^{{1/{p}}}$\n")

    for i in range(n):
        for j in range(i + 1, n):
            p1, p2 = points[i], points[j]
            output.append(f"**{labels[i]} vs {labels[j]}:**")
            powered = [abs(v1 - v2) ** p for v1, v2 in zip(p1, p2)]
            for k, (c, v1, v2, d) in enumerate(zip(col_names, p1, p2, powered)):
                output.append(f"  - {c}: |{v1} - {v2}|^{p} = {d}")
            output.append(f"- Soma: {powered} = {sum(powered)}")
            output.append(
                f"- Resultado: $({sum(powered)})^{{1/{p}}} = {minkowski(p1, p2, p):.4f}$\n"
            )

if CLUSTERS is not None:
    output.append("---\n")
    output.append("## Distâncias entre Clusters\n")
    output.append(f"Método de distância: {DISTANCE_TYPE}\n")
    output.append(f"Cluster assignments: {CLUSTERS}\n")

    unique_clusters = sorted(set(CLUSTERS))
    output.append(f"Clusters: {unique_clusters}\n")

    def get_dist(p1, p2):
        if DISTANCE_TYPE == "euclidean":
            return euclidean(p1, p2)
        return manhattan(p1, p2)

    def get_points_in_cluster(c):
        return [i for i, cl in enumerate(CLUSTERS) if cl == c]

    def single_link(c1, c2):
        pts1 = get_points_in_cluster(c1)
        pts2 = get_points_in_cluster(c2)
        min_dist = float("inf")
        for i in pts1:
            for j in pts2:
                d = get_dist(points[i], points[j])
                if d < min_dist:
                    min_dist = d
        return min_dist

    def complete_link(c1, c2):
        pts1 = get_points_in_cluster(c1)
        pts2 = get_points_in_cluster(c2)
        max_dist = 0
        for i in pts1:
            for j in pts2:
                d = get_dist(points[i], points[j])
                if d > max_dist:
                    max_dist = d
        return max_dist

    def average_link(c1, c2):
        pts1 = get_points_in_cluster(c1)
        pts2 = get_points_in_cluster(c2)
        total = 0
        count = 0
        for i in pts1:
            for j in pts2:
                total += get_dist(points[i], points[j])
                count += 1
        return total / count if count > 0 else 0

    def centroid_link(c1, c2):
        pts1 = get_points_in_cluster(c1)
        pts2 = get_points_in_cluster(c2)
        centroid1 = np.mean([points[i] for i in pts1], axis=0)
        centroid2 = np.mean([points[i] for i in pts2], axis=0)
        return get_dist(centroid1, centroid2)

    def ward_method(c1, c2):
        pts1 = get_points_in_cluster(c1)
        pts2 = get_points_in_cluster(c2)
        all_pts = pts1 + pts2

        centroid_all = np.mean([points[i] for i in all_pts], axis=0)
        centroid1 = np.mean([points[i] for i in pts1], axis=0)
        centroid2 = np.mean([points[i] for i in pts2], axis=0)

        n1, n2 = len(pts1), len(pts2)

        ward = n1 * get_dist(centroid1, centroid_all) + n2 * get_dist(
            centroid2, centroid_all
        )
        return ward

    methods = {
        "Single Link (MIN)": single_link,
        "Complete Link (MAX)": complete_link,
        "Average Link": average_link,
        "Centroid Link": centroid_link,
        "Ward's Method": ward_method,
    }

    for method_name, method_func in methods.items():
        output.append(f"### {method_name}\n")

        dist_matrix = np.zeros((len(unique_clusters), len(unique_clusters)))

        for ic1, c1 in enumerate(unique_clusters):
            for ic2, c2 in enumerate(unique_clusters):
                if c1 == c2:
                    dist_matrix[ic1, ic2] = 0
                else:
                    d = method_func(c1, c2)
                    dist_matrix[ic1, ic2] = d

        output.append(
            "```\n"
            + matrix_to_md(dist_matrix, [f"C{c}" for c in unique_clusters])
            + "\n```\n"
        )

        output.append(f"**Cálculos:**\n")
        for ic1, c1 in enumerate(unique_clusters):
            for ic2, c2 in enumerate(unique_clusters):
                if c1 < c2:
                    pts1 = get_points_in_cluster(c1)
                    pts2 = get_points_in_cluster(c2)
                    output.append(f"**C{c1} vs C{c2}** (pts: {pts1} vs {pts2}):")

                    if method_name == "Single Link (MIN)":
                        min_d = float("inf")
                        for i in pts1:
                            for j in pts2:
                                d = get_dist(points[i], points[j])
                                output.append(
                                    f"  - {labels[i]} vs {labels[j]}: {d:.2f}"
                                )
                                if d < min_d:
                                    min_d = d
                        output.append(f"  → MIN: {min_d:.2f}\n")
                    elif method_name == "Complete Link (MAX)":
                        max_d = 0
                        for i in pts1:
                            for j in pts2:
                                d = get_dist(points[i], points[j])
                                output.append(
                                    f"  - {labels[i]} vs {labels[j]}: {d:.2f}"
                                )
                                if d > max_d:
                                    max_d = d
                        output.append(f"  → MAX: {max_d:.2f}\n")
                    elif method_name == "Average Link":
                        total, count = 0, 0
                        for i in pts1:
                            for j in pts2:
                                d = get_dist(points[i], points[j])
                                total += d
                                count += 1
                        avg = total / count
                        output.append(f"  → Média: {total}/{count} = {avg:.2f}\n")
                    elif method_name == "Centroid Link":
                        centroid1 = np.mean([points[i] for i in pts1], axis=0)
                        centroid2 = np.mean([points[i] for i in pts2], axis=0)
                        output.append(f"  - Centroide C{c1}: {centroid1}")
                        output.append(f"  - Centroide C{c2}: {centroid2}")
                        output.append(
                            f"  → Distância: {get_dist(centroid1, centroid2):.2f}\n"
                        )
                    elif method_name == "Ward's Method":
                        all_pts = pts1 + pts2
                        centroid_all = np.mean([points[i] for i in all_pts], axis=0)
                        centroid1 = np.mean([points[i] for i in pts1], axis=0)
                        centroid2 = np.mean([points[i] for i in pts2], axis=0)
                        n1, n2 = len(pts1), len(pts2)
                        d1 = get_dist(centroid1, centroid_all)
                        d2 = get_dist(centroid2, centroid_all)
                        ward = n1 * d1 + n2 * d2
                        output.append(f"  - |C{c1}|={n1}, |C{c2}|={n2}")
                        output.append(
                            f"  - d(centroid1, all)={d1:.2f}, d(centroid2, all)={d2:.2f}"
                        )
                        output.append(
                            f"  → Ward: {n1}×{d1:.2f} + {n2}×{d2:.2f} = {ward:.2f}\n"
                        )

with open(OUTPUT_PATH, "w") as f:
    f.write("\n".join(output))

print(f"Report gravado em: {OUTPUT_PATH}")
