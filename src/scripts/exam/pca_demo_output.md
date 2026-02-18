# Demo da Pergunta (PCA)

- v1 = [-0.86, 0.51]
- lambda1 = 1.5
- x = [1.0, 1.0]
- Razão explicada em d) para lambda1: 0.8000
- lambda2 em e): 0.5

## Cálculos-base

- Projeção 1D x·v1 = -0.3500
- lambda2 em d): lambda2 = lambda1*(1-r)/r = 1.5*(1-0.8000)/0.8000 = 0.3750
- Variância explicada de lambda1 em e): 1.5/(1.5+0.5) = 0.7500

## Avaliação das afirmações

- a) LDA, tal como PCA, procura máxima variabilidade global: FALSE
- b) Projeção de x=(1,1) em v1 é -0.35: TRUE (valor=-0.3500)
- c) PCA pode ser usada para compressão e reconstrução: TRUE
- d) Se lambda1 explica 80%, lambda2=0.3: FALSE (lambda2=0.3750)
- e) Se lambda2=0.5, lambda1 explica >85%: FALSE (explicação=0.7500)
