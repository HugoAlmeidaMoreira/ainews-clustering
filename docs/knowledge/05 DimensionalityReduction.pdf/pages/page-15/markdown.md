# Information measures in classification

- $\chi^2$ test (chi2 in Python)
- robust for input categorical variables
- two values: $\chi^2$ statistic (higher the better), $p$-value

```python
iris = datasets.load_iris()
X, y = iris.data, iris.target
chi2, pval = chi2(X, y)
[ 10.81782088 3.59449902 116.16984746 67.24482759 ]
[ 4.47651e-03 1.6575e-01 5.943443e-26 2.50017e-15 ]
```

- ANOVA test (f_classif in Python)
- robust for numeric input variables
- also valid for categorical input with numerical output
- two values: F-value statistic (higher the better), $p$-value

TÉCNICO+
FORMAÇÃO AVANÇADA