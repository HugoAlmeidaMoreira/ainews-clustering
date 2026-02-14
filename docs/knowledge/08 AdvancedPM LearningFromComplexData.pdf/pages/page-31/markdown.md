# Sequential pattern mining

- A sequence is an ordered list of events, denoted $&lt; e_1 e_2 \ldots e_l &gt;$
- an event can be univariate, multivariate or an itemset

- Given two sequences $\alpha = &lt; a_1 a_2 \ldots an &gt;$ and $\beta = &lt; b_1 b_2 \ldots bm &gt;$
- $\alpha$ is called a **subsequence** of $\beta$, denoted as $\alpha \subseteq \beta$, if there exist integers $1 \leq j_1 &lt; j_2 &lt; \ldots &lt; j_n \leq m$ such that $a_1 \subseteq bj_1, a_2 \subseteq bj_2, \ldots, an \subseteq b_{jn}$
- $\beta$ is a **supersequence** of $\alpha$
- e.g. $&lt; a(bc)dc &gt;$ is a **subsequence** of $&lt; a(abc)(ac)d(cf) &gt;$

- A sequence database is a set of (itemset) sequences
- A sequential pattern is an association capturing relevant **precedences** and **co-occurrences** in a sequence database

TÉCNICO+ FORMACÃO AVANÇADA
31