# $k$-means: challenges

- Efficiency: $O(tkn)$ $n = \# \text{observation}$, $k = \# \text{clusters}$, $t = \# \text{iterations}$, usually $k, t \ll n$
- Problems
- dependent on initialization
- sensitive to outliers
- sensitive noisy data
- noise can substantially distort centroids
- not suitable to discover clusters with non-convex shapes
- deal only with clusters with spherical symmetrical point distribution
- need to specify $k$, the number of clusters, in advance
- convergence?

TÉCNICO+ FORMACÃO AVANÇADA