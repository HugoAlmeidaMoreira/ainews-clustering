# Relevant association rules

- Example: among 5000 students
- 3000 play basketball
- 3750 eat cereal
- 2000 both play basketball and eat cereal

- play basketball ⇒ eat cereal [sup=40%, conf=66.7%]
- Misleading! Overall percentage of students eating cereal is 75%, higher than 66.7%
- play basketball ⇒ not eat cereal [sup=20%, conf=33.3%]
- Far more accurate! Although lower support and confidence!

- How to more accurately measure a rule's relevance?

|   | basketball | not basketball  |
| --- | --- | --- |
|  cereal | 2000 | 1750  |
|  not cereal | 1000 | 250  |

TÉCNICO+
FORMAÇÃO AVANÇADA