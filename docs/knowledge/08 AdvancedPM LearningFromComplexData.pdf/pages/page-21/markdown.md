# Learning from temporal data: associative

## Pattern-centric predictor

- **TRAIN**: given the time series data
- discover temporal patterns and create a tabular dataset with a feature per pattern
- fill the tabular dataset in accordance with one of the following options:
1. **boolean dataset**: whether a time series $x_i$ has or not a given pattern $y_j$
2. **real-valued dataset**: how well a time series $x_i$ contains a given pattern $y_j$
- apply classic classifiers to learn a model using this tabular dataset

- **TEST**: given a new time series
- produce the feature-vector: test if the testing time series has the given patterns (boolean) or how well captures the patterns (real-valued)
- apply the trained classifier to on the feature-vector to return a label

TÉCNICO+ FORMACÃO AVANÇADA