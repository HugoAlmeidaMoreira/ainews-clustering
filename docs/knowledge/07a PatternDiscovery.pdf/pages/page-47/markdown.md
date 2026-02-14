# Constrained pattern mining

## Meta-rule constraints

- partially instantiated predicates and constants, example:
- $P1(x,Y) \land P2(x,W) \Rightarrow \mathrm{buys}(x,iPad)$
- pattern satisfying this constraint: $age(x, [15,25]) \land job(x, student) \Rightarrow \mathrm{buys}(x, iPad)$
- How? push constants deeply when possible into the mining process

## Other constraints:

- knowledge type constraint: known classification, association, etc.
- query constraint: e.g. "find product pairs sold together in stores in Chicago"
- dimension/level constraint: in relevance to region, price, brand, customer category

## Recall: data mining should be an interactive process

- user directs what to be mined using a data mining query language

TÉCNICO+ FORMAÇÃO AVANÇADA