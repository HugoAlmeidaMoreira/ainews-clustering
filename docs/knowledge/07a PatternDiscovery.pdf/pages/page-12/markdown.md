# Origins... basket analysis

- Some of the origins of pattern mining resort back to market basket analysis...
- A transactional database is a set of transactions
- each transaction (basket) is a set of items
- Patterns often given by:
- frequent itemsets, i.e. co-occurring items in a number or percentage of transactions
- association rules, i.e. items that discriminate occurrence of other items
- Accordingly, frequent itemset mining (FIM) and association rule mining (ARM) aim at finding all those patterns

|  ID | Items  |
| --- | --- |
|  1 | {Bread, Milk}  |
|  2 | {Bread, Diapers, Beer, Eggs}  |
|  3 | {Milk, Diapers, Beer, Cola}  |
|  4 | {Bread, Milk, Diapers, Beer}  |
|  5 | {Bread, Milk, Diapers, Cola}  |
|  ... | ...  |

{Diapers, Beer} Example of a frequent itemset
{Diapers} → {Beer} Example of an association rule

TÉCNICO+
FORMAÇÃO AVANÇADA