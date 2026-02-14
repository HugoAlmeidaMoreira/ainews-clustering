# FP-Growth

- Bottlenecks of Apriori
- multiple database scans are costly
- long patterns generate lots of candidates
- recall $\varphi = \{y_{i1}, y_{i100}\}$ contains $1.27 \times 10^{30}$ patterns
- Can we avoid candidate generation?
- Yes! using Frequent Pattern (FP) tree structure (avoid further data scans) and pattern-conditional trees to efficiently grow patterns
- FP-Growth approach
- for each frequent itemset, construct its conditional pattern-base and FP-tree
- repeat the process on each newly created conditional FP-tree

TÉCNICO+ FORMACÃO AVANÇADA