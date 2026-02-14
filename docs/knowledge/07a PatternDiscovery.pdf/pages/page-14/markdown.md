# Frequent vs relevant patterns

- Considering the itemset {water, potatoes}
- Can it be considered frequent if its support is 5%? 20% 50%?
- What about the itemset {diapers, flowers}?

- Challenge: impossible to define a single support threshold as item probabilities highly vary!
- same challenge in multivariate data (e.g. brown skin and blue eyes)
- implication: frequency is not good proxy for relevance
- e.g. the pattern "dog bites human" is as frequent as "human bites dog" on a given dataset, yet the latest is much less expected so surely more important!

- Replace frequency by statistical significance

TÉCNICO+ FORMACÃO AVANÇADA