# Outlier analysis: supervised methods

## Supervised outlier detection

- outlier detection as a **classification** task
- observations validated by domain experts (e.g., fraud clearance) for training and testing
- given an observation, the probability of the outlier class can be seen as a score
- **single-class prediction** task
- model normal (outlier) observations and report those not matching the model

## Challenges

- imbalanced classes (outliers are rare)
- ensure that the applied learning approach can handle imbalance (e.g. avoid kNN, favor neural networks with weighted observations or trees/ensembles)
- catch as many outliers as possible
- **sensitivity**/recall more important than accuracy
- $F_{\beta}$-measure with higher $\beta$ values

10