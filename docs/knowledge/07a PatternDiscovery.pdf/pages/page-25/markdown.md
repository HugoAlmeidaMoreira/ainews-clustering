# Relevant association rules

- Any given association rule, e.g. $A \Rightarrow B$, can be further characterized by its:
- **support**, fraction of observations that satisfy the rule, i.e. $\sup(A \Rightarrow B) = \sup(A \cap B)$
- **confidence**, fraction of observations with the antecedent in which the consequent is also satisfied, i.e.

$$
\mathrm{confidence}(A \Rightarrow B) = P(B|A) = \frac{P(A \cap B)}{P(A)} = \frac{\mathrm{support}(A \Rightarrow B)}{\mathrm{support}(A)}
$$

- Recovering R: $\{\mathrm{Socks}\} \Rightarrow \{\mathrm{Tie}\}$
- support of R is 50% (2/4)
- confidence of R is 66.67% (2/3)
- are the observed support and confidence high enough? Is the rule relevant?

|  T1 | Shoes, **Socks, Tie**  |
| --- | --- |
|  T2 | Shoes, **Socks, Tie**, Belt, Shirt  |
|  T3 | Shoes, Tie  |
|  T4 | Shoes, Socks, Belt  |

TÉCNICO+
FORMAÇÃO AVANÇADA