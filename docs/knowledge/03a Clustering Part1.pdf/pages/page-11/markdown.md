# Focal point: distances

- well-established distances can be applied yet...
...best distances are generally **customized** to the problem domain (background knowledge)

$$
\text{e.g. demographic dist}(ind_1, ind_2) = \frac{age_1 - age_2}{20} + 1[region_1 = region_2] \times 0.8 + 1[sex_1 = sex_2] \times 1.2 + \cdots
$$

- apply distance to produce pairwise **distance matrices** between observations (and/or clusters)
- similarity matrix = − distance matrix

|   | A | B | C | D | E | F  |
| --- | --- | --- | --- | --- | --- | --- |
|  A | 0 | 0.71 | 5.66 | 3.61 | 4.24 | 3.20  |
|  B | 0.71 | 0 | 4.95 | 2.92 | 3.54 | 2.50  |
|  C | 5.66 | 4.95 | 0 | 2.24 | 1.41 | 2.50  |
|  D | 3.61 | 2.92 | 2.24 | 0 | 1.00 | 0.50  |
|  E | 4.24 | 3.54 | 1.41 | 1.00 | 0 | 1.12  |
|  F | 3.20 | 2.50 | 2.50 | 0.50 | 1.12 | 0  |

TÉCNICO+ FORMAÇÃO AVANÇADA