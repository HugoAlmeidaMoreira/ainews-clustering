# Constrained pattern mining

- Finding all the patterns in a database autonomously? Unrealistic!
- the patterns could be too many but not focused
- what makes a truly interesting pattern?

- Available domain knowledge can be used to guide the pattern discovery
- ideally we can formalize background knowledge using constraints

- A constraint is a predicate in the data space
- Given a dataset and a set of constraints $C$, the problem of **constrained pattern mining** is the discovery of all relevant patterns satisfying $C$
- Simplistic examples:
- metric constraints, e.g. lift $&gt; \theta$
- value/item constraints, e.g. specific features to be included/excluded from patterns

TÉCNICO+ FORMACÃO AVANÇADA