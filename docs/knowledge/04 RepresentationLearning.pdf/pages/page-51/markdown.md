# LLMs: self-supervision

The sequence of word (and positional) embeddings in a text concatenated into a numeric tensor
- this tensor can be a text representation by itself, yet is high-dimensional and lacks expressivity
- padding/transforms entailed to ensure the tensor has uniform shape for texts with varying length

The tensor feeds a neural network with the aim of learning an expressive embedding
- autoencoders are rare since as text reconstruction is generally insufficient to capture text semantics
- supervised neural architectures are alternatively applied using a key principle

- self-supervision
- create fictitious predictive tasks to learn embeddings
- common: targets derived from unlabeled text by masking words to allow supervision
- predictive task: classify the masked words (e.g., arbitrarily positioned word, next word)

TÉCNICO+
FORMAÇÃO AVANÇADA