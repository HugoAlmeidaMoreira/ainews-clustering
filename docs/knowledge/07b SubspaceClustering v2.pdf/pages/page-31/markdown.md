# Evaluation metrics

## Real data (subjective metrics)

- **statistical significance**: unexpected occurrence probability
- **domain relevance**: unexpected probability of participating in studied process
- domain and statistical significance correlated but not always in agreement!

- HOW to assess domain relevance of bicluster $(I, J)$?
- source of annotations: knowledge bases (e.g. GO) and literature data (e.g. PubMED)
- statistically test I and J against well-established annotations
- hypergeometric tests to compute enrichment p-values against an annotation database
- intuition: most of entries in I (or J) sharing annotations in a database suggests relevance

TÉCNICO+ FORMACÃO AVANÇADA