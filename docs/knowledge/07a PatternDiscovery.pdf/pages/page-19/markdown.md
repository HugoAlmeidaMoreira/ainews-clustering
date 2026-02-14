# Negative patterns

- Support-based definition
- If patterns $P1$ and $P2$ are both frequent or significant, yet rarely occur together, i.e., $\sup(P1 \cup P2) \ll \sup(P1) \times \sup(P2)$
- then $P1$ and $P2$ are negatively correlated
- Example: a store sells needles $A$ and $B$, with $p(A) = p(B) = 0.5$
- assuming only one transaction contained both $A$ and $B$
- when there is a total of 200 observations, $\sup(A) \times \sup(B) = 0.25$ and $\sup(A \cup B) = \frac{1}{200} = 0.005 &lt; \sup(A) \times \sup(B)$
- Other definitions available, e.g. Kulzynski-based definition
- If patterns $P1$ and $P2$ are frequent, yet $(P(P1|P2) + P(P2|P1))/2 &lt; \epsilon$, then $P1$ and $P2$ are negatively correlated

TÉCNICO+ FORMAÇÃO AVANÇADA