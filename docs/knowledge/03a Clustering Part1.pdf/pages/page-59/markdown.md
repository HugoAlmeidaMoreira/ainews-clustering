# External measures: purity

- $\Omega = \{\omega_1, \omega_2, \dots, \omega_K\}$ is the set of clusters
$C = \{c_1, c_2, \dots, c_J\}$ is the set of classes
- For each cluster $\omega_k$: find class $c_j$ with most objects in $\omega_k$, $n_{kj}$
- Sum all $n_{kj}$ and divide by total number of points

$$
\operatorname{purity}(\Omega, C) = \frac{1}{n} \sum_{k} \max_{j} |\omega_k \cap c_j|
$$

- **Problem**: biased ⇒ n clusters maximizes purity
- Alternatives: entropy of classes in clusters

TÉCNICO+
FORMAÇÃO AVANÇADA
59