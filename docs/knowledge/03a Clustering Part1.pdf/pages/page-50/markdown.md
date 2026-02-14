# Internal measures: cohesion and separation

- Cohesion (e.g. sum of squared errors or sum of square within):
how closely related are points in a cluster
$$
SSE = SSW = \sum_{k=1}^{K} \sum_{x_i \in C_k} d(x_i, c_k)^2
$$

- Separation (e.g. sum of squares between clusters)
how distinct or well-separated a cluster is from other clusters
$$
SSB = BSS = \sum_{k} |c_k| d(c_k, \hat{x})^2
$$

- Total error (e.g. sum of squares): within and between errors
$$
TSS = SSB + SSE
$$
$$
TSS = \sum_{i}^{n} d(x_i, \hat{x})^2
$$

TÉCNICO+ FORMAÇÃO AVANÇADA