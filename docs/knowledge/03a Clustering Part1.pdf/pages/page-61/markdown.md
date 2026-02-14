# External measures: rand index

- Counts of object pairs

|  same class
different classes | same cluster | different clusters  |
| --- | --- | --- |
|   |  true positives (TP) | false negatives (FN)  |
|   |  false positives (FP) | true negatives (TN)  |

- Rand index  $\mathrm{RI} = \frac{TP + TN}{TP + FP + FN + TN}$

- Given a specific cluster (positive):
- precision = TP/(TP+FP)
- recall = TP/(TP+FN)
- F-measure = 2×precision×recall / (precision + recall)

TÉCNICO+
FORMAÇÃO AVANÇADA