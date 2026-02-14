# Statistically significant patterns

- Considering a transactional database of 1000 baskets
- the probability of a user buying water is 30% and buying potatoes is 10% (probabilities directly estimated from the database)
- what is the null joint probability of buying $\varphi = \{\text{water, potatoes}\}$?
Under independence assumption:
$$
p_{\text{null}}(\varphi) = p_{\text{null}}(\text{water} \cap \text{potatoes}) = p(\text{water}) \times p(\text{potatoes}) = 0.3 \times 0.1 = 0.03
$$

- Assuming that we observe 35 baskets in the database with water and potatoes: Is $\{\text{water, potatoes}\}$ statistically significant?
- to answer this, we need to test "Given $N = 1000$, what is the probability of at least $n = 35$ users buying water and potatoes knowing $p_{\text{null}} = 0.03$?"

TÉCNICO+ FORMAÇÃO AVANÇADA