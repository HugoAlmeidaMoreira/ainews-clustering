# Univariate summary statistics

- variability statistics
- standard deviation for numeric variables (square root of the variance)

$$
\sigma_{population} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{\mathbf{X}})^2}, \quad \sigma_{sample} = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{\mathbf{X}})^2}
$$

- population-based (divided by $n$) versus sample-based (divided by $n - 1$)
- sample is a conservative estimate (higher) since we do not observe the whole population
- example: $\{1,2,15\}$ measurements: $\mu = 6$, median $= 2$, $\sigma_{population} = 6.37$, $\sigma_{sample} = 7.81$

- entropy for categorical variables $H(\mathbf{x}) = -\sum_{x \in \mathbf{x}} p(x) \log p(x)$
- the higher entropy, the higher the variability
- example: $H(A,A,A,A) = 0$, $H(A,A,A,B) = 0.81$, $H(A,A,B,B) = 1$

TÉCNICO+ FORMÁCÃO AVANÇADA