# Multi-level embeddings

- Challenge: high-dimensional embeddings (e.g. thousands of dimensions for text) hamper tasks, such as retrieval and clustering, where you want to quickly find neighbors (closest records, images, signals, documents, webpages) for a given input (e.g., web search)
- Solution: learn multiple representations by training autoencoders with varying bottleneck sizes

- small-sized embeddings used to find the nearest neighbor candidates (e.g., top 200) using cosine similarity
- optimal-sized embedding of candidates to obtain a final ranking (e.g., ordered top 10)

![img-43.jpeg](img-43.jpeg)

TÉCNICO+

FORMAÇÃO AVANÇADA