# Chebyshev distance
(numeric data)

- when $q \to \infty$, the metric highly penalizes maximum attribute errors
- useful if the worst case must be avoided:

$$
d_{\infty}(\mathbf{x}, \mathbf{y}) = \lim_{q \to \infty} \left( \sum_{i=1}^{n} |x_i - y_i|^q \right)^{1/q} = \max(|x_1 - y_1|, |x_2 - y_2|, \dots, |x_n - y_n|)
$$

Example:

$$
d_{\infty}((2,8), (6,3)) = \max(|2 - 6|, |8 - 3|) = \max(4,5) = 5
$$

TÉCNICO+
FORMAÇÃO AVANÇADA