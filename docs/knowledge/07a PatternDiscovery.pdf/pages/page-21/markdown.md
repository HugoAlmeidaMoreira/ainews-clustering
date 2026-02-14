# Association rules

- Recall the concept of an association rule, $R: A \Rightarrow B$
- where $A$ is the antecedent (set of features) and $B$ is the consequent (set of features or outcomes)
- if $B$ is an outcome of interest, $R$ is also termed discriminative pattern

- Considering the following transactional database
- $\varphi = \{\text{Socks}, \text{Tie}\}$ is an itemset with coverage $\{T1, T2\}$, support 0.5, and $p$-value (Binomial test with $n=2$, $N=4$ and null probability $p(\varphi) = \frac{3}{4} \times \frac{3}{4} = 0.56$) of 0.4, hence not unexpectedly frequent
- What about Socks $\Rightarrow$ Tie? Is it relevant?

|  T1 | Shoes,Socks,Tie  |
| --- | --- |
|  T2 | Shoes,Socks,Tie,Belt,Shirt  |
|  T3 | Shoes,Tie  |
|  T4 | Shoes,Socks,Belt  |

TÉCNICO+
FORMAÇÃO AVANÇADA