# Multimodal Representations

- Learning representations from heterogeneous data structures
- combining features, text, vision, time series, events, trajectories, multiple omics...

- Classic stance:
- extract features from each mode separately
- classic statistics and/or unimodal data representations
- concatenate the representations (larger numeric vector with mode-dedicated sections)

- Problems:
- informative features capturing cross-modal synergies are neglected
- many of earlier representation principles no longer satisfied (e.g., succinctness, disentanglement)
- dependencies between representations of each mode
- what if one modality is not available for some training or testing observations?

- Solution: multimodal autoencoders and shared multi-task learning

iit

56