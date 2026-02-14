# Exam 2022

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

5. [0.8v] Consider class to be our ground truth, compute the purity of the clustering solution.

$$
purity = \frac{1}{4} (1 + 2) = 0.75
$$

6. [0.5v] Select the limitations of the k-Means algorithm (i.e. the true statements):

a) dependent on initialization/seeding
b) sensitive to outliers under mean centroid criteria
c) not suitable to discover clusters with irregular/non-convex shapes
d) dependent on the specification of a proper linkage criterion

7. [0.5v] Given the following data plot (right), select the proper clustering stances to recover its clusters:

a) model-based clustering
b) density-based clustering
c) soft clustering
d) hard clustering
e) partition-based clustering

![img-0.jpeg](img-0.jpeg)

8. [1v] Classify the following statements as True or False:

a) Clustering becomes semi-supervised when pairs of observations are known to belong to the same cluster. True
b) Agglomerative clustering algorithms allow to manually select a desirable number of clusters once a dendrogram is inferred. True
c) Complete (maximum) link criterion tends to break large clusters and is biased towards globular clusters. True
d) A rand index that is close to zero suggests that the clustering algorithm was unable to guarantee high cluster dissimilarity. False

## II. Dimensionality reduction [2.7v]

Consider that the application PCA over the numeric variables of $D$ produced the following covariance matrix, eigenvectors and eigenvalues:

$$
C = \left( \begin{array}{cc} 5.58 &amp; 2.33 \\ 2.33 &amp; 1.33 \end{array} \right), \quad \mathbf{v}_1 = ?, \quad \mathbf{v}_2 = \left( \begin{array}{c} 0.9 \\ 0.4 \end{array} \right), \quad \lambda_1 = 0.302, \quad \lambda_2 = 6.614
$$

9. [1v] What is the percentage of data variability explained by eigenvector  $\mathbf{v}_2$ ?

$$
\frac {\lambda_ {2}}{\lambda_ {1} + \lambda_ {2}} = 95.6 \%
$$

10. [1.2v] Project the numeric values of  $D$  to the reduced space using  $\mathbf{v}_2$ .

|   | c2=0.9y1+0.4y2  |
| --- | --- |
|  x1 | -1  |
|  x2 | 4.3  |
|  x3 | 1.6  |
|  x4 | -1  |

11. [0.5v] Identify the eigenvector  $\mathbf{v}_1$ .

Solving  $C\mathbf{v}_1 = \lambda_1\mathbf{v}_1$  equations (and optional normalization) yields  $\mathbf{v}_1 \approx \begin{pmatrix} -0.4 \\ 0.9 \end{pmatrix}$

# III. Pattern Mining [6.95v]

12. [1.7v] Selecting  $y_3$  and  $y_4$ , identify all the closed and maximal frequent itemsets with a relative support above 0.5.

closed:  $A[sup = 3], AC[sup = 2], D[sup = 2]$

maximal:  $AC[sup = 2], D[sup = 2]$

13. [0.8v] Given the association rule,  $AC \Rightarrow X$ , compute its support, confidence and lift.

$$
s u p (R) = s u p (A C X) = 0. 5, c o n f (R) = \frac {s u p (A C X)}{s u p (A C)} = 1, l i f t (R) = \frac {c o n f (R)}{s u p (X)} = \frac {4}{3}
$$

14. [1v] Consider that we have access to additional observations, leading to the following re-evaluation of rule

$$
A C \Rightarrow X [ \text {s u p p o r t} = 0. 5, \text {B i n o m i a l} p \text {v a l u e} = 1 E - 3, \text {c o n f i d e n c e} = 0. 8, \text {l i f t} = 0. 9 9 ]
$$

Classify the following statements as True or False:

a) Assuming a significance level  $\alpha = 0.1$ , the given pattern is not statistically significant False
b) The given lift suggests an interesting/strong association rule False
c) The given lift suggests that the consequent,  $X$ , is highly frequent (support&gt;0.5) True
d) If  $AC$  is a frequent itemset, a superset (e.g.  $ACX$ ) is also frequent (monotonicity) False

15. [1.4v] Selecting $y_1$ and $y_2$, identify the largest constant bicluster and the largest order-preserving bicluster with $\delta = 0$ and no noise ($\varepsilon = 0$)

Constant (I={x1,x4}, J={y1,y2}), Order-preserving (I={x1,x2,x3,x4}, J={y1,y2})

16. [0.8v] Given the additive bicluster (I={x1,x2,x3,x4}, J={y1,y2}) and $\delta = 0$, compute its quality.

Considering additive factors $\{\gamma_1 = 0, \gamma_2 = 2, \gamma_3 = 2, \gamma_4 = 0\}$, the quality is 7/8

17. [0.75v] Classify the following statements as True or False:

a) A biclustering solution with 2 biclusters with overlapping elements is always non-exhaustive on rows and columns. False
b) Given a biclustering search, a statistically significant bicluster that was not retrieved by this search is termed false positive. False
c) The coherence strength of a bicluster determines the deviations from expectations. True

18. [0.5v] Which of the following actions generally increase the average size of patterns in a solution (where size is the number of elements, i.e. support × pattern length):

a) increase tolerance to noise (i.e. decrease quality)
b) choose closed pattern representations instead of all patterns
c) given perfect quality, increase the cardinality of variables in discrete data
d) decrease coherence strength (higher deviations allowed) in real-valued data

## IV. Outlier analysis [1.25v]

19. Classify the following statements as True or False:

a) Given specific context variables, a contextual outlier observation is an observation that significantly deviates from other observations that share the same context. True
b) A collective outlier is an observation that deviates from neighbour observations. False
c) Observations in clusters with bad cohesion (sparse clusters) are outlier candidates. True
d) Given a data where a few observations are annotated with normal/non-outlier tag, these observations should be removed to better detect outliers. False
e) Density-based outlier analysis approaches can be used to identify local outliers. True

v. Learning from Complex Data [3v]

20. Classify the following statements as True or False:

a) The order of a multivariate time series corresponds to the number of time points. False
b) Pattern mining in time series can be either considered in the context of a single time series (e.g. motif discovery) or multiple time series (e.g. biclustering). True
c) When computing the distance between time series, Minkowski distances (e.g. Euclidean) cannot account for temporal misalignments. True
d) Statistics extracted with a sliding window along time series observations can be used to produce a multivariate dataset. True
e) As frequent itemsets are solely focused on co-occurrences, sequential patterns are solely focused on precedences. False
f) Given time series data, biclustering can be extended to accommodate time lags between observations. True
g) Nominal univariate events are also termed typed events. True
h) Complex patterns can generally be mapped into binary or numeric variables (one variable per pattern) for subsequent multivariate data analysis. True
i) The data of a system with stationary sensors producing signals at different locations can be described by a georeferenced time series structure. True
j) The spatial slicing principle suggests that is rather more important to learn global models than multiple local/regional models. False
k) Inductive logic can be used to capture associations between tables. True

END


# Prototype Exam

## Practical exercises

### Group I. Calculus [14.6v]

Considering the following dataset, where $y_{1} \in [0,3]$, $y_{2}$ is ordinal and $z$ is a nominal target.

|   | y_{1} | y_{2} | z  |
| --- | --- | --- | --- |
|  x_{1} | 1.2 | C | X  |
|  x_{2} | 0.2 | B | X  |
|  x_{3} | 3 | A | Y  |
|  x_{4} | 0.5 | B | Y  |
|  x_{5} | 0.3 | A | Y  |

1. [1.5v] Considering $y_{2}$ numerical encoding, {A: 0, B: 1, C: 3}, Manhattan distance, and fully unsupervised setting. Draw the dendrogram under complete linkage.

|   | x_{1} | x_{2} | x_{3} | x_{4} | x_{5}  |
| --- | --- | --- | --- | --- | --- |
|  x_{1} | 0 | 3 | 4.8 | 2.7 | 3.9  |
|  x_{2} |  | 0 | 3.8 | 0.3 | 1.1  |
|  x_{3} |  |  | 0 | 3.5 | 2.7  |
|  x_{4} |  |  |  | 0 | 1.2  |
|  x_{5} |  |  |  |  | 0  |

Dendrogram: {{{x2,x4}}[0.3], x5][1.2], x3][3.8], x1][4.8}

2. [1v] Are there multivariate outliers in accordance with DBSCAN $(p=3, \varepsilon=3)$? Which? $\{x_1, x_3\}$

3. Assuming a solution with maximal purity against the output variable $z$.

a) [1v] Identify the medoid of the larger cluster

Larger cluster $\{x_{3}, x_{4}, x_{5}\}$

Average distances $q$ to other observations in the cluster: $q(x_{3}) = 3.1, q(x_{4}) = 2.35, q(x_{5}) = 1.95$

b) [1.5v] Identify the silhouette of the smaller cluster

$$
silhouette(x_{1}) = 1 - \frac{3}{3.8} = 0.21, \quad silhouette(x_{2}) = \frac{\frac{5.2}{3}}{3} - 1 = -0.42,
$$

Note that when $a(x) &gt; b(x)$ then a better proxy to the silhouette of an observation is $\frac{b(x)}{a(x)} - 1$

$$
silhouse(c_{1}) = \frac{0.21 - 0.42}{2} = -0.1
$$

4. [1v] Consider the following analysis of sum squared errors (SSE) gathered from a thousand of randomized datasets using k-means. Identify the correct statement:

i. A SSE in [0.02,0.023] is statistically significant
ii. A SSE above 0.34 is statistically significant
iii. A SSE below 0.017 is statistically significant $\Leftarrow$
iv. None of above

![img-0.jpeg](img-0.jpeg)

5. Under the same numerical encoding, consider the biclustering task on $\{y_1, y_2\}$.

a) [1v] Identify the largest perfect constant with coherence strength $\delta = 0.5$

Constant: $B = (I = \{x2,x4\}, J = \{y1,y2\})$

b) [1.1v] Compute the quality of order-preserving bicluster $(I = \{x1,x2,x4,x5\}, J = \{y1,y2\})$

Quality = 7/8 (mode orders are $y1 \leq y2$)

6. [1v] Binarize $y_1$ after standard scaling using equal-range discretization.

Standardly scaled y1 | X = (0.14, -0.72, 1.69, -0.46, -0.64)

Two bin equal-range of $N(0,1)$ is $[- \infty, 0[$ and $]0, \infty[$

As a result, binarized $y_1 = (U, L, U, L, L)$

7. Assuming the binarization yields $y_1 = (Q, Q, R, Q, Q)$ and $\{y_1, y_2\}$ variables:

a) [1.5v] Identify the set of closed co-occurrences satisfying $\min_{sup} = 0.4$

All patterns: Q, A, B, QB

Closed patterns: Q, A, QB

b) [2.4v] Compute the statistical significance of pattern QB and the lift of rule $Q \Rightarrow B$

$$
p_{\text{null}}(QD) = \frac{4}{5} \times \frac{2}{5} = \frac{8}{25} = 0.32
$$

$$
P(X \geq 2 \mid X \sim \text{Binomial} \quad (p = 0.32, N = 5) = 0.51
$$

$$
\text{lift} = \sup(QB) / (\sup(Q) \times \sup(B)) = \frac{2}{5} / \frac{4}{5} \times \frac{2}{5} = 1.25
$$

8. [1.6v] Consider the covariance matrix $C$ obtained from the given dataset and the corresponding eigenvectors. Which of the eigenvectors should be considered to reduce the dimensionality?

$$
C = \begin{pmatrix} 1.353 &amp; -0.225 \\ -0.225 &amp; 1.5 \end{pmatrix}, \quad v_1 = \begin{pmatrix} -0.8 \\ -0.59 \end{pmatrix}, \quad v_2 = \begin{pmatrix} 0.59 \\ -0.8 \end{pmatrix}
$$

Given $C v_1 = \lambda_1 v_1$, then $\lambda_1 \approx 1.189$

Given $C v_2 = \lambda_2 v_2$, then $\lambda_2 \approx 1.66$

The second eigenvector is used to reduce the space has it explains more variability

Group II. True-and-false [5.4v] (+0.45v for correct, -0.2v for incorrect)

1. An outlier can be inconsistent with the remaining data or just its neighbourhood. True
2. In supervised outlier analysis, assessing the sensitivity of a classifier is often preferred over its accuracy. True
3. Contextual outliers only deviate on a compact subset of variables. False
4. Hamming distance is adequate to handle ordinal variables with high cardinality. False
5. $k$-means does not adequately identify spherical clusters. False
6. Purity is biased when the number of found clusters approaches the total number of observations. True
7. Spearman correlation is preferred over Pearson correlation if the order of values is more relevant than their absolute value. True
8. Given a $m$-dimensional dataset, PCA can reconstruct any data point using $m - 1$ components of PCA with zero reconstruction error. False

9. The lift measure of an association rule $A \Rightarrow B$ does not change if we add a new transaction that does not either contain A or B. False
10. Sequential pattern mining can be applied to find frequent co-occurrences in symbolic multivariate time series data. True
11. A false negative tricluster is a statistically significant subspace that was not retrieved. True
12. The search for triclusters with low variance allows the discovery of additive subspaces. False

END