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