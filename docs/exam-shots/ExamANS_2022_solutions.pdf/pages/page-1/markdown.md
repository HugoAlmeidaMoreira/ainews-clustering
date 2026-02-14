J

DASH: ANS

Exam 2022

Version A

# Solutions

Consider the $D$ dataset below to answer questions along the exam:

|   | y_{1} | y_{2} | y_{3} | y_{4} | class | cluster  |
| --- | --- | --- | --- | --- | --- | --- |
|  x_{1} | -2 | 2 | B | D | X | C1  |
|  x_{2} | 3 | 4 | A | C | X | C2  |
|  x_{3} | 0 | 4 | A | C | X | C1  |
|  x_{4} | -2 | 2 | A | D | Y | C1  |

# I. Clustering [6.1v]

Given $D$ and distance $d(\mathbf{x}_A, \mathbf{x}_B) = \text{Manhattan}(\mathbf{x}_A, \mathbf{x}_B | y_1, y_2) + \text{Hamming}(\mathbf{x}_A, \mathbf{x}_B | y_3, y_4)$

1. [0.5v] Complete the following pairwise distance matrix

|   | x_{1} | x_{2} | x_{3} | x_{4}  |
| --- | --- | --- | --- | --- |
|  x_{1} | 0 | 9 | ? | ?  |
|  x_{2} |  | 0 | 3 | 8  |
|  x_{3} |  |  | 0 | 5  |
|  x_{4} |  |  |  | 0  |

$$
d(\mathbf{x}_1, \mathbf{x}_3) = 6, \quad d(\mathbf{x}_1, \mathbf{x}_4) = 1
$$

2. [1v] Can the given clustering solution be obtained by an agglomerative algorithm under single link? Justify by presenting the final dendrogram.

No. Dendrogram: $\{\{\mathbf{x}_1,\mathbf{x}_4\} [1]\{\mathbf{x}_2,\mathbf{x}_3\} [3]\} [5]$

3. [1.2v] Let $\mathbf{x}_1$ and $\mathbf{x}_4$ be the initial centroids of $k$-means. Compute one iteration of the $k$-means, identifying the new centroids using medoid averaging criteria.

After iteration: $\{\mathbf{x}_1\}, \{\mathbf{x}_2, \mathbf{x}_3, \mathbf{x}_4\}$

Medoids: $\mathbf{x}_1$ and $\mathbf{x}_3$

4. [0.6v] Using $d(\mathbf{x}_A, \mathbf{x}_B)$, identify the silhouette of observation $\mathbf{x}_4$.

$$
\text{silhouette}(\mathbf{x}_4) = 1 - \frac{3}{8} = \frac{5}{8}
$$