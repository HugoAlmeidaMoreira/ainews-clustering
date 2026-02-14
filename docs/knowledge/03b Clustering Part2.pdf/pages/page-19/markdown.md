# Partitioning algorithms

Given $k$ clusters:

1. partition observations into $k$ non-empty subsets
2. compute the centroid $c_{j}$ of each subset
- centroid is the center of mass: e.g. mean or median centers
3. reassign each observation to the cluster with the nearest centroid
4. goto step 2, stop when:
i) assignment does not change, ii) $|E^{new} - E^{old}| &lt; \varepsilon$, or iii) max iterations is reached

## Variants

- centroid calculus
- selection of the initial seeds
- adjustments for **batches** of observations (instead of all) for very large datasets

TÉCNICO+
FORMAÇÃO AVANÇADA
19