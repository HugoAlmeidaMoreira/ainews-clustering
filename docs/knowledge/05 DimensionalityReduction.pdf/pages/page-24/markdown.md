# Algebra ground

- Covariance matrix, given $m$ attributes, $y_1, \ldots, y_m$

$$
C^{m \times m} = (c_{ij} | \mathrm{i}, \mathrm{j} = 1.. \mathrm{m}), \text{ where } c_{ij} = \operatorname{cov}(y_i, y_j)
$$

|   | Hours(H) | Mark(M)  |
| --- | --- | --- |
|  Data | 9 | 39  |
|   |  15 | 56  |
|   |  25 | 93  |
|   |  14 | 61  |
|   |  10 | 50  |
|   |  18 | 75  |
|   |  0 | 32  |
|   |  16 | 85  |
|   |  5 | 42  |
|   |  19 | 70  |
|   |  16 | 66  |
|   |  20 | 80  |
|  Totals | 167 | 749  |
|  Averages | 13.92 | 62.42  |

$$
\begin{array}{l}
C^{m \times m} = \left( \begin{array}{cc} \operatorname{cov}(H, H) &amp; \operatorname{cov}(H, M) \\ \operatorname{cov}(M, H) &amp; \operatorname{cov}(M, M) \end{array} \right) \\
= \left( \begin{array}{cc} \operatorname{var}(H) &amp; 104.5 \\ 104.5 &amp; \operatorname{var}(M) \end{array} \right) \\
= \left( \begin{array}{cc} 47.7 &amp; 104.5 \\ 104.5 &amp; 370 \end{array} \right)
\end{array}
$$

TÉCNICO+

FORMAÇÃO AVANÇADA