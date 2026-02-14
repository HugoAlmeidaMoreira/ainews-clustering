# Example: MD sequential patterns

- Multi-dimensional (MD) sequential pattern mining as an illustrative case: integrates multi-dimensional analysis and sequential pattern mining
- Recap: sequential pattern mining to find frequent subsequences

|  10 | <a(abc)(ac)d(cf)>  |
| --- | --- |
|  20 | <(ad)c(bc)(ae)>  |
|  30 | <(ef)(ab)(df)cb>  |
|  40 | <eg(af)cbc>  |

<a(bc)dc> is a subsequence of <a(abc)(ac)d(cf)>

Given support threshold  $\theta = 2$ ,

$&lt;(\mathrm{ab})c&gt;$  is a sequential pattern

- MD sequence database: combine dimensional information to the itemset sequence produced from the fact entries of a given object (split dimension)

- example: if  $\theta = 2$ ,  $P = (\text{group} = *, \text{city} = \text{Chicago}, \text{age} = *, \text{qeq} = &lt;\text{bf}&gt;)$  is a MD pattern

|  cid | Cust_grp | City | Age_grp | sequence  |
| --- | --- | --- | --- | --- |
|  10 | Business | Boston | Middle | <(bd)cba>  |
|  20 | Professional | Chicago | Young | <(bf)(ce)(fg)>  |
|  30 | Business | Chicago | Middle | <(ah)abf>  |
|  40 | Education | New York | Retired | <(be)(ce)>  |

TÉCNICO+

FORMAÇÃO AVANÇADA</a(abc)(ac)d(cf)></a(bc)dc>