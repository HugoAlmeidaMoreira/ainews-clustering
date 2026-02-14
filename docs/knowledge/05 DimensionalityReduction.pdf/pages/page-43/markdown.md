# Reconstruction error

- PCA minimizes the reconstruction error:  $\| \mathbf{x} - \hat{\mathbf{x}}\|$
- It can be shown that the reconstruction error is:  $\text{error} = 1/2 \sum_{i=k+1}^{m} \lambda_i$

- using 2 components: recovery error = 0 (from previous slide)
- using 1 component

|  y'₁ | y'_₂ | y'_1 | y'_2  |
| --- | --- | --- | --- |
|  0.56 | 0.61 | 2.4 | 2.5  |
|  -1.20 | -1.31 | 0.6 | 0.6  |
|  0.67 | 0.73 | 2.5 | 2.6  |
|  0.19 | 0.20 | 2.0 | 2.1  |
|  1.14 | 1.23 | 2.9 | 3.1  |
|  0.62 | 0.67 | 2.4 | 2.6  |
|  -0.07 | -0.07 | 1.7 | 1.8  |
|  -0.78 | -0.84 | 1.0 | 1.1  |
|  -0.30 | -0.32 | 1.5 | 1.6  |
|  -0.83 | -0.90 | 1.0 | 1.0  |

$$
\text{error} = 0.245 = \frac{0.49}{2} = \frac{\lambda}{2}
$$

$$
\text{DataRecovered} = (\text{FeatureVector}(p=1) \times \text{TransformedData}) + \text{OriginalMean}
$$

TÉCNICO+
FORMAÇÃO AVANÇADA