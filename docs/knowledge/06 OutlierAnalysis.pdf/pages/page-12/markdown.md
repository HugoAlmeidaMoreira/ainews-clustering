# Outlier analysis: semi-supervised methods

## Semi-supervised outlier detection

- Number of annotated observations is often small
- annotations could be on outliers only, normal observations only, or both

- How? Semi-supervised learning
1. if some **normal observations** are annotated
- use labeled examples and the nearby unlabeled observations to train a model for normal observations; those not fitting the model are seen as outliers
2. if some **outliers** are annotated (may not cover all possible outliers well)
- get help from models for normal observations learned from unsupervised methods

TÉCNICO+ FORMACÃO AVANÇADA