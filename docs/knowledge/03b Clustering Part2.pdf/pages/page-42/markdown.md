# Importance of seeding initial centroids

- If there are $k$ real clusters...
- ... chance of selecting one centroid from each cluster is small when $k$ is large
- e.g. if $k = 10$, then probability = $10! / 10^10 = 0.00036$

- **Difficulty**: sometimes centroids readjust in 'right' way, sometimes don't

- **Solution**
- multiple runs (helps, but probability is not on your side)
- hierarchical clustering to determine initial centroids
- select more than $k$ initial centroids and then select among these initial centroids (select most widely separated)
- postprocessing

TÉCNICO+ FORMACÃO AVANÇADA