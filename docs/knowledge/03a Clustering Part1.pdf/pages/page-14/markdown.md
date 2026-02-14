# Common distance metrics (numeric data)

## Minkowski distance

$$
d(i,j) = \sqrt[4]{\underbrace{|a_{i1} - a_{j1}|^q}_{1^{\text{st} \text{ dimension}}} + \underbrace{|a_{i2} - a_{j2}|^q}_{2^{\text{nd} \text{ dimension}}} + \dots + \underbrace{|a_{ip} - a_{jp}|^q}_{p^{\text{th} \text{ dimension}}}
$$

## Euclidean distance $(q = 2)$

$$
d(i,j) = \sqrt{ \left| a_{i1} - a_{j1} \right|^2 + \left| a_{i2} - a_{j2} \right|^2 + \dots + \left| a_{ip} - a_{jp} \right|^2 } \quad \text{(Note: } \text{where } \text{a}_{i1} = (a_{i1}, a_{i2}, \dots, a_{ip}) \text{ } \text{)}.
$$

## Manhattan distance $(q = 1)$

$$
d(i,j) = \left| a_{i1} - a_{j1} \right| + \left| a_{i2} - a_{j2} \right| + \dots + \left| a_{ip} - a_{jp} \right|
$$

TÉCNICO+
FORMAÇÃO AVANÇADA
14