# Interestingness

- many other possibilities...
- DISA is a Python package that implements most of them:

https://github.com/JupitersMight/DISA

|  symbol | measure | range | formula  |
| --- | --- | --- | --- |
|  φ | φ-coefficient | -1...1 | P(A,B)-P(A)P(B)  |
|  Q | Yule's Q | -1...1 | √P(A)P(B)(1-P(A))(1-P(B))P(A,B)P(A,B)-P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A)  |
|  Y | Yule's Y | -1...1 | √P(A,B)P(A,B)-√P(A,B)P(A,B)√P(A,B)P(A,B)+√P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A)  |
|  k | Cohen's | -1...1 | P(A,B)+P(A,B)-P(A)P(B)-P(A)P(B)1-P(A)P(B)-P(A)P(B)  |
|  PS | Piatetsky-Shapiro's | -0.25...0.25 | P(A,B)-P(A)P(B)  |
|  F | Certainty factor | -1...1 | max(P(B|A)-P(B), P(A|B)-P(A))1-P(B), P(A|B)-P(A))  |
|  AV | added value | -0.5...1 | max(P(B|A)-P(B), P(A|B)-P(A))  |
|  K | Klosgen's Q | -0.33...0.38 | √P(A,B)max(P(B|A)-P(B), P(A|B)-P(A))ΣjmaxkP(Aj,Bk)+ΣkmaxjP(Aj,Bk)-maxjP(Aj)-maxkP(Bk)ΣjΣjP(Aj,Bj)log P(Aj,Bj)max(P(Aj,Bj)min(-ΣjP(Aj)log P(Aj)log P(Aj)-maxjP(Aj))  |
|  g | Goodman-kruskal's | 0...1 | ∑jΣjP(Aj,Bj)log P(Aj)-maxjP(Aj)max(P(Aj,Bj)min(-ΣjP(Aj)log P(Aj)log P(Aj)-maxjP(Aj))  |
|  M | Mutual Information | 0...1 | max(P(A|P(B|A)+P(A|B)-P(A|B)+P(A|B)-P(A|B)+P(A|B))  |
|  J | J-Measure | 0...1 | max(P(A|B)-P(A|B)-P(A|B)-P(A|B)-P(A|B)-P(A|B)-P(A|B)  |
|  G | Gini index | 0...1 | max(P(A|P(B|A)+P(A|B)-P(A|B)+P(A|B)-P(A|B)-P(A|B))  |
|  s | support | 0...1 | P(A,B)  |
|  c | confidence | 0...1 | max(P(B|A), P(A|B))  |
|  L | Laplace | 0...1 | max(NP(A,B)+1/NP(A,B)+1/NP(A,B)+1/NP(A,B)+1/NP(A,B)+1/NP(A,B)+1/NP(A,B)  |
|  IS | Cosine | 0...1 | √P(A,B)  |
|  γ | coherence(Jaccard) | 0...1 | √P(A,B)P(A)P(B)-P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A)  |
|  α | all_confidence | 0...1 | max(P(A|P(B), P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))  |
|  o | odds ratio | 0...∞ | P(A,B)P(A)P(B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A)  |
|  V | Conviction | 0.5...∞ | max(P(A|P(B), P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))  |
|  λ | lift | 0...∞ | P(A,B)P(A)P(B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A)  |
|  S | Collective strength | 0...∞ | ∑i(P(A,i)-Ei)2Ei  |

#

TÉCNICO+

FORMAÇÃO AVANÇADA