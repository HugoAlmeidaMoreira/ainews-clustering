# PCA example

2. Calculate the covariance matrix:

$$
cov = \left( \begin{array}{cc} y_1 &amp; y_2 \\ .616555556 &amp; .615444444 \\ .615444444 &amp; .716555556 \end{array} \right) y_1
$$

3. Calculate its (unit) eigenvectors and eigenvalues

$$
eigenvalues = \left( \begin{array}{c} .0490833989 \\ 1.28402771 \end{array} \right) \qquad eigenvectors = \left( \begin{array}{cc} -.735178656 &amp; -.677873399 \\ .677873399 &amp; -.735178656 \end{array} \right)
$$

4. Order eigenvectors by eigenvalue, highest to lowest and select top $p$

$$
\mathbf{v}_1 = \left( \begin{array}{cc} -.6779 \\ -.7352 \end{array} \right) \quad \lambda_1 = 1.284 \qquad \mathbf{v}_2 = \left( \begin{array}{c} -.7352 \\ .6779 \end{array} \right) \quad \lambda_2 = .0491
$$

... and construct the transformed feature vector

$$
FeatureVector(k = 2) = \left( \begin{array}{cc} -.6779 &amp; -.7352 \\ -.7352 &amp; .6779 \end{array} \right) \quad FeatureVector(k = 1) = \left( \begin{array}{c} -.6779 \\ -.7352 \end{array} \right)
$$

TÉCNICO+ FORMAÇÃO AVANÇADA