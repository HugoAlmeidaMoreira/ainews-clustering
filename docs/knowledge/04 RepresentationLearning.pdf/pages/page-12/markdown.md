# Autoencoders

- How then? A classic approach is to learn an autoencoder:
- learn an encoder $g: X \to Z$ and the corresponding $(g^{-1})$ decoder $d: Z \to X$
- the goal is to reconstruct the input, i.e. $\mathbf{x} \approx d(g(\mathbf{x}))$
- we can learn the encoder and decoder functions from data by minimizing a loss
- reconstruction loss, $Loss(\mathbf{x}) = Loss(\mathbf{x}, d(g(\mathbf{x})))$
using, for instance, the mean squared error (MSE) on numeric features

- Yet... How to learn encoder-decoder functions without previous knowledge?
- Neural networks!
- and indeed... neural representations can attain some of the nice properties!

TÉCNICO+
FORMAÇÃO AVANÇADA