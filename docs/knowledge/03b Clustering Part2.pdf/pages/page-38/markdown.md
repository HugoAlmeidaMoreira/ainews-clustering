# Visualizing clustering solutions

Key principles for knowledge discovery (to be mastered during our course!)

- Compute the variables that are better separated by the clusters
- add a cluster's column to the dataset and run ANOVA (f-classif in sklearn) to assess the discriminative power of each input variable (use p-values to rank them by importance)
- Retrieve the centroids
- Compute the cluster-conditional distributions for the most important features
- Retrieve observation memberships/distances to each cluster/centroid
- Visualize clustering solutions in a 2D or 3D space
- select specific features of interest (importance or domain knowledge)
- project the original m-dimensional space into a 2D or 3D space using uMAP, PCA, tSNE

TÉCNICO+ FORMACÃO AVANÇADA