# Demo da Questão (Autoencoder Linear)

- x = [1.0, 2.0]
- W1 = [0.5, 0.5] (encoder 1x2)
- W2 = [1.0, 1.0] (decoder 2x1)

## Cálculos

- Embedding z = W1·x = 0.5*1.0 + 0.5*2.0 = 1.5000
- Reconstrução x_hat = W2*z = [1.5, 1.5]
- MAE = mean(|x - x_hat|) = 0.5000

## Avaliação das opções

- a) MAE da reconstrução é 0.5: TRUE
- b) embedding de x é (0.5,1): FALSE
- c) bom embedding maximiza dependência entre features latentes: FALSE
- d) uma rede pode combinar autoencoding e supervised learning para embeddings numéricos: TRUE
- e) reconstrução de x é (1.5,1.5): TRUE
