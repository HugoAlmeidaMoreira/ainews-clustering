# Vertical approaches

- Problem: high-dimensionality
- Apriori and FP-Growth are computationally heavy for spaces with thousands of variables

- Solutions:
- scalability extensions
- vertical partitioning of the dataset, followed by efficient pattern fusion
- parallelization of operations
- vertical pattern mining approaches (e.g. ECLAT) – flip/transpose the view:
- items and categoric features have a list of observation IDs
- pattern growth by intersecting observation IDs (instead of large sets of items)

TÉCNICO+ FORMACÃO AVANÇADA