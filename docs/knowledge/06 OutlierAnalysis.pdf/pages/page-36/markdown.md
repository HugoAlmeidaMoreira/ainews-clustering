# Outlier analysis in high-dimensional data

## Challenges
- distance between observations becomes heavily dominated by noise
- data in high-dimensional spaces are often sparse
- interpretation of outliers: detecting outliers without saying why they are outliers is not very useful in high-dim data due to many involved features

## Solutions
- use more robust distance functions and find full-dimensional outliers
- find outliers in projections of the original feature space: dimensionality reduction works only when in lower-dimensional spaces normal instances can still be distinguished from outliers
- PCA: components with low variance preferred since normal observations are likely close to each other and outliers often deviate from majority
- use supervised reduction whenever possible

TÉCNICO+ FORMACÃO AVANÇADA