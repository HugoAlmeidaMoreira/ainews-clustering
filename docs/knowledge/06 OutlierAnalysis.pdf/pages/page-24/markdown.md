# Distance-based approaches

- An observation $\mathbf{x}$ in a dataset $X$ is a $(p, d)$-outlier if at least a fraction $p$ of observations in $X$ are $\geq$ distant $d$ from $\mathbf{x}$
- An observation $\mathbf{x}$ in a dataset is a $(k, d)$-outlier if no more than $k$ points in the dataset are at a distance $d$ or less from $\mathbf{x}$
- Distance of the $k^{\text{th}}$ nearest neighbor of $\mathbf{x}$ can be used as an outlier score
- Efficient computation:
- for any observation $\mathbf{x}_i$, calculate its distance to other observations
- if $k = pn$ observations are within $r$ distance, terminate the inner loop: $\mathbf{x}_i$ is normal, otherwise a $(p,d)$-outlier

TÉCNICO+ FORMACÃO AVANÇADA