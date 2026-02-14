# Distances in clustering

- Distances (or similarities) applied between:
- two observations $d(\mathbf{x}_i, \mathbf{x}_j)$
- one observation and a cluster $d(\mathbf{x}_i, \mathbf{c}_j)$
- two clusters $d(\mathbf{c}_i, \mathbf{c}_j)$

- **Cluster**: $\mathbf{c}_j = \{\mathbf{x} \mid d(\mathbf{x}, \mathbf{c}_j) = \min_i d(\mathbf{x}, \mathbf{c}_i)\}$

- **Centroid** of a cluster as its mass center: $\bar{\mathbf{c}}_j$ (e.g., mean/mode value per real/categorical variable)

- Squared **error** of clustering solution: $E = \sum_{k=1}^{K} \sum_{\mathbf{x} \in \mathbf{c}_k} d(\mathbf{x}, \bar{\mathbf{c}}_k)^2$

TÉCNICO+
FORMAÇÃO AVANÇADA
16