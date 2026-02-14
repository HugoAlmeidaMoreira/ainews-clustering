# PCA example

## 5. Derive the new data set

TransformedData = RowFeatureVector × RowDataAdjust

$$
DataAdjusted = \left( \begin{array}{cccccccccc}
.69 &amp; -1.31 &amp; .39 &amp; .09 &amp; 1.29 &amp; .49 &amp; .19 &amp; -.81 &amp; -.31 &amp; -.71 \\
.49 &amp; -1.21 &amp; .99 &amp; .29 &amp; 1.09 &amp; .79 &amp; -.31 &amp; -.81 &amp; -.31 &amp; -1.01
\end{array} \right)
$$

$$
FeatureVector(p = 2)^T = \left( \begin{array}{cc}
-.6779 &amp; -.7352 \\
-.7352 &amp; .6779
\end{array} \right)
$$

$$
FeatureVector(p = 1)^T = (-.6779 \quad -.7352)
$$

TransformedData $(p=2)$

|  c_{1} | c_{2}  |
| --- | --- |
|  -.827970186 | -.175115307  |
|  1.77758033 | .142857227  |
|  -.992197494 | .384374989  |
|  -.274210416 | .130417207  |
|  -1.67580142 | -.209498461  |
|  -.912949103 | .175282444  |
|  .0991094375 | -.349824698  |
|  1.14457216 | .0464172582  |
|  .438046137 | .0177646297  |
|  1.22382056 | -.162675287  |

TransformedData $(p=1) =$

|  c_{1}  |
| --- |
|  -.827970186  |
|  1.77758033  |
|  -.992197494  |
|  -.274210416  |
|  -1.67580142  |
|  -.912949103  |
|  .0991094375  |
|  1.14457216  |
|  .438046137  |
|  1.22382056  |

TÉCNICO+
FORMAÇÃO AVANÇADA