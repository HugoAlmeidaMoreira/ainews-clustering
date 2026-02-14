# From MLPs to other neural architectures

MLPs originally proposed for the analysis of simple multivariate data, however...

- fully-connected layers are computationally expensive for high-dimensional data
- given $p$ units in the 1st layer: $m \times p$ parameters (high $m$, $p$ in same magnitude) for this single layer
- other data structures are described by features with unique dependencies...

- image and video: features are spatiotemporally correlated! Spatial dependencies
- (multivariate) time series: features change along time! Temporal dependencies
- text and speech: terms are situated (syntactical and semantical context)! Sequential dependencies

- we need to go beyond classic fully-connected layering...

- convolutional layering (CNNs) for signal and image data
- recurrent layering (RNNs) for time series data
- self-attention layering for language data

TÉCNICO+
FORMAÇÃO AVANÇADA