# Quantitative associations

- Two major forms of association rules:
- categorical ⇒ quantitative rules or quantitative ⇒ quantitative rules
- e.g. education in [14-18] (yrs) ⇒ mean wage = $11.64/h

- Finding extraordinary and therefore interesting phenomena, e.g.
$$
\text{sex} = \text{female} \Rightarrow \text{wage: mean} = \$7 \text{ (overall mean} = \$9\text{)}
$$

- LHS: a subset of the population
- RHS: an extraordinary behavior of this subset

- The rule is accepted if a statistical test (e.g. Z-test) confirms inference with high confidence

- Subrule: highlights the extraordinary behavior of a pop. subset of the super rule, e.g.
$$
(\text{sex} = \text{female}) \wedge (\text{south} = \text{yes}) \Rightarrow \text{mean wage} = \$6.3/h
$$

- Open problem: efficient methods for LHS containing two or more quantitative attributes

42