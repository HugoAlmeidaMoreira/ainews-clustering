# Learning from temporal data: associative

## Rule-based predictor

- **TRAIN**: given observations with temporal information
- find temporal patterns
- use the found temporal patterns to produce association rules **pattern ⇒ class**
- rule interestingness criteria reveal the discriminative power of the rule
- *lift* is a good proxy when data is imbalanced

- **TEST**: given a new observation
- find the closest patterns from the produced rules
- label the time series using the rules' consequents (voting stage)
- mode from either all matched rules or top-$k$ closest rules
- weight matched rules by their relevance and discriminative power

TÉCNICO+ FORMACÃO AVANÇADA