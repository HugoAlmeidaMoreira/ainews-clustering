# Interestingness

- Classic pattern mining methods define simplistic thresholds:
- FIM aims at finding all patterns satisfying a minimum support threshold
- ARM aims at finding all rules satisfying a minimum support and confidence
- rules satisfying both thresholds are called **strong**

- Modern pattern mining methods further consider:
- statistical significance criteria
- e.g. p-value&lt;0.1 under binomial test from null data model)
- interestingness criteria, e.g. lift&gt;1.3...

|  X | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Y | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0  |
|  Z | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1  |
|  Rule | Support | Lift  |
| --- | --- | --- |
|  X⇒Y | 25% | 2  |
|  X⇒Z | 37.50% | 0.9  |
|  Y⇒Z | 12.50% | 0.57  |

TÉCNICO+
FORMAÇÃO AVANÇADA