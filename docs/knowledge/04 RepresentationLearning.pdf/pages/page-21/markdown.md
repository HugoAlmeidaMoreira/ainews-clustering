# Learning neural networks

## Goal

- given a training set of input-output pairs $(\mathbf{x}_i, \mathbf{z}_i)$, learn the parameters $\theta$ of the network
- the parameters are essentially the weights from all layers

## How?

- finding the weights that minimize a loss between the real and estimated outputs
- a common loss is the squared error $L(\hat{\mathbf{z}}, \mathbf{z}) = \|\hat{\mathbf{z}} - \mathbf{z}\|^2$
- gradients are used to adjust weights in a direction that decreases the loss
- the adjusting process is often termed gradient descent (GD) or backpropagation
- randomly initialize weights and iteratively adjust throughout epochs using batches of pairs
- the learning rate $\eta$ and batch size controls the intensity and stability of weight updates

TÉCNICO+ FORMACÃO AVANÇADA