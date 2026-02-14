# Evaluation metrics

Synthetic data (objective metrics)

H is the set of true biclusters and B is the set of found biclusters

- Clustering metrics on one dimension (X and Y separately)
- silhouette, recall and precision – problems?

- Jaccard-based match scores (MS) to assess the similarity of $B$ and $H$
- $MS(B,H)$ extent to which found biclusters match hidden biclusters
- $MS(H,B)$ reflects how well hidden biclusters are recovered

$$
MS(\mathcal{B}, \mathcal{H}) = \frac{1}{|\mathcal{B}|} \Sigma_{(I_1, J_1) \in \mathcal{B}} \max_{(I_2, J_2) \in \mathcal{H}} \frac{|I_1 \cap I_2|}{|I_1 \cup I_2|}
$$

- Fabia consensus is sensitive to the number of biclusters in both sets

$$
FC(\mathcal{B}, \mathcal{H}) = \frac{1}{|\mathcal{S}_1|} \Sigma_{((I_1, J_1) \in \mathcal{S}_1, (I_2, J_2) \in \mathcal{S}_2) \in MP} \frac{|I_1 \cap I_2| \times |J_1 \cap J_2|}{|I_1| \times |J_1| + |I_2| \times |J_2| - |I_1 \cap I_2| \times |J_1 \cap J_2|}
$$

TÉCNICO+ FORMAÇÃO AVANÇADA