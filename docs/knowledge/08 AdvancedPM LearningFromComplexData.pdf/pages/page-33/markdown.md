# Sequential pattern mining (SPM)

- SPM is computationally complex! Approaches:
- candidate generation: Apriori-like (e.g. GSP method)
- pattern growth using suffix trees (e.g. PrefixSpan)

- Voluminous solutions?
- exact same principles as in classic pattern mining: filtering, condensed pattern representations, dissimilarity

- Statistical significance
- exact same binomial statistical test as in simple patterns on the pattern support
- null model based on Markov assumption
- e.g. $p_{null}(&lt; adc &gt;) = p(a)p(&lt; ad &gt; |a)p(&lt; dc &gt; |d)$ where the probabilities are based on the frequentist view (ratio of observations)
- using previous table $p_{null}(&lt; adc &gt;) = 1 \times \frac{2}{4} / 1 \times \frac{3}{4} / \frac{3}{4} = \frac{2}{4}$

TÉCNICO+ FORMAÇÃO AVANÇADA