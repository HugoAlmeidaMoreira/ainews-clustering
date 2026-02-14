# Definition

- Subspace clustering can be applied to different data structures, including:
- [biclustering] simple multivariate data
- [n-way subspace clustering] tensor data (e.g. **triclustering** for three-way data)

- Given a dataset, $D$, with a set of observations $X = \{\mathbf{x}_1, \ldots, \mathbf{x}_N\}$, a set of variables $Y = \{y_1, \ldots, y_M\}$, and elements $a_{ij} \in R$ relating observation $x_i$ and variable $y_j$:
- A bicluster $B = (I, J)$ defines a pattern in $D$, where $I = (\mathbf{x}_{i_1}, \ldots, \mathbf{x}_{i_n}) \subset X$ is a subset of observations (pattern support) and $J = (y_{j_1}, \ldots, y_{j_m}) \subset Y$ is a subset of variables (subspace)
- The biclustering task aims to identify a set of biclusters $\mathbf{B} = \{B_1, \ldots, Bs\}$ such that each bicluster $B_k = (I_k, J_k)$ satisfies specific criteria of homogeneity and statistical significance

![img-1.jpeg](img-1.jpeg)

TÉCNICO+
FORMAÇÃO AVANÇADA