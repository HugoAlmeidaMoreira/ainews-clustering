# Mining maximal patterns

- 1st scan: find frequent items
- A, B, C, D, E
- 2nd scan: find support for
- AB, AC, AD, AE, ABCDE
- BC, BD, BE, BCDE ← candidate max-patterns
- CD, CE, DE, CDE

|  ID | items  |
| --- | --- |
|  10 | A,B,C,D,E  |
|  20 | B,C,D,E,  |
|  30 | A,C,D,F  |

- Since BCDE is a max-pattern, no need to check BCD, BDE, CDE in later scan
- Principles combined in Apriori and FP-Growth approaches

61

TÉCNICO+

FORMAÇÃO AVANÇADA