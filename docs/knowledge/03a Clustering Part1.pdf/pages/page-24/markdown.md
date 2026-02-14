# Cluster distance

- Single link: smallest distance between observations
- Complete link: largest distance between observations
- Average link: average distance between observations

$$
d(c_i, c_j) = \frac{1}{|c_i||c_j|} \sum_{x_i \in C_i} \sum_{x_j \in C_j} d(x_i, x_j)
$$

- Centroid link: distance between centroids
- Ward's distance: similarity based on the error increase when two clusters are merged (sum of squared distances of points to closest centroid)

TÉCNICO+ FORMAÇÃO AVANÇADA