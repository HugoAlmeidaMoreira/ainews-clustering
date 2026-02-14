# Pattern fusion

- Philosophy: jump out of the swamp of mid-sized patterns and quickly reach colossal patterns
- mid-sized patterns are called **core patterns**
- a colossal pattern is composed by multiple **core patterns** and a few **small-sized patterns**

- Pattern Fusion is an approach to this end using tree structures
- traverses the tree in a bounded-breadth way, only expands a bounded-size candidate pool
- only a fixed number of patterns are used as starting nodes — avoiding the exponential search space
- identifies "shortcuts" whenever possible (e.g. agglomeration of patterns in the pool)
- pattern fusion shortcuts will direct the search down the tree much more rapidly towards the colossal patterns

TÉCNICO+ FORMACÃO AVANÇADA