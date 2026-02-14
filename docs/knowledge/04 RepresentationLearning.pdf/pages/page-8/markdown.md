# Good representations

- Multiple explanatory factors
- recover different factors so it is useful for many tasks
- Disentangled explanatory factors
- each dimension of the representation should capture a separate/meaningful aspect of the data
- Hierarchical explanatory factors
- some underlying factors are more abstract than others and could be further defined in terms of less abstract ones
- Loose factor dependencies
- factors should be related through simple, linear dependencies
- leverage interpretability (e.g., physics) and support subsequent learning
- Sparsity: for any observation $x$, only some factors are
- relevant $\Rightarrow$ most dimensions of $g(x)$ should be zero, or
- invariant to small variations of $x$

8