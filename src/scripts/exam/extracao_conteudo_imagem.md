# Extração de conteúdo (imagem do exame)

> Transcrição manual do conteúdo visível na imagem. Pode haver pequenas diferenças de pontuação/formatação devido à qualidade da foto.

## Questão (PCA)

The following eigenvectors and eigenvalues were identified by PCA:

$$
v_1 = \begin{pmatrix}-0.86 \\ 0.51\end{pmatrix},\quad v_2 = ?,\quad \lambda_1 = 1.5,\quad \lambda_2 = ?
$$

Opções:

- a. Similarly to PCA, LDA aims to find the axes with the highest data variability
- b. The x=(1,1) one-dimensional projection using v1 is -0.35
- c. PCA can be used for data compression and reconstruction
- d. Knowing λ1 is able to explain 80%, λ2=0.3
- e. Knowing λ2=0.5, λ1 is able to explain more than 85%

## Pergunta 4 (Autoencoder)

Given a bivariate observation x and an autoencoder f. The autoencoder produces 1-dim embeddings, no biases, one encoder layer W1, one decoder layer W2, and no activations (i.e φ(x)=x):

$$
x = \begin{pmatrix}1 \\ 2\end{pmatrix},\quad W_1 = (0.5\ \ 0.5),\quad W_2 = \begin{pmatrix}1 \\ 1\end{pmatrix}
$$

Opções:

- a. The mean absolute error of the reconstructed x is 0.5
- b. The neural embedding of x is (0.5,1)
- c. A good embedding is one that maximizes the coupling/dependency between the latent features.
- d. A single neural network can combine both autoencoding and supervised learning to produce numeric embeddings.
- e. The reconstruction of x after compression is (1.5,1.5)