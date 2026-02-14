# Interestingness: lift

- Lift measures the discriminative power (also known as surprise) of the rule

$$
lift(A \Rightarrow B) = \frac{P(B|A)}{P(B)} = \frac{P(A \cap B)}{P(A) \times P(B)}
$$

- in contrast with confidence, takes into account the probability of the consequent
- in fact, $\operatorname{lift}(A \Rightarrow B) = \frac{\operatorname{conf}(A \Rightarrow B)}{P(B)}$

- lift &lt; 1: A and B negatively correlated, if the value is less than 1
- the higher, the greater the relevance of the rule

- lift &gt; 1: A and B are positively correlated

- lift = 1: A and B are independent, $P(A \cap B) = P(A)P(B)$

TÉCNICO+
FORMAÇÃO AVANÇADA
27