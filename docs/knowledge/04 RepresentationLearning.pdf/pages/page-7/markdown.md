# Good representations

- Smoothness: if $x_1 \approx x_2$, then $g(x_1) \approx g(x_2)$
- the most basic prior
- similarity in the representation (somehow) reflects similarity of raw data

- Invariances/equivariance/coherence:
small semantic changes should result in similar representations. Invariance is domain-specific:
- image representations should be invariant under transformations like rotations, color jitter...
- time series representations can be invariant to temporal shifts, rescales...

- Less supervision: unsupervised / semi-supervised / self-supervised representations
- representations should capture raw content (easily lost when focusing on specific targets)
- one representation may be used for multiple end goals

TÉCNICO+ FORMACÃO AVANÇADA