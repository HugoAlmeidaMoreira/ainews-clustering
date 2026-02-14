# Component selection

- The variance in the direction of the $k^{\text{th}}$ eigenvector is given by the eigenvalue $\lambda_{k}$
- Singular values can be used to estimate how many components to keep
- **Rule of thumb**: keep enough to explain 85% of the variation

$$
\frac {\sum_ {j = 1} ^ {k} \lambda_ {j}}{\sum_ {j = 1} ^ {m} \lambda_ {j}} \approx 0.85
$$

if $k = m$, we preserve 100% of the original variation

- depending on the reduced dimensionality and learning needs: 90%, 95%, 98% also common
- **Karhunen-Loeve (KL)** transform is PCA without subsequent removal of components
- no information loss

TÉCNICO+ FORMACÃO AVANÇADA