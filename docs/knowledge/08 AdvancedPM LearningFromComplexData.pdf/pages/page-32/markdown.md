# Sequential pattern mining (SPM)

- Given a set of sequences and support threshold, SPM tasks aims at finding all frequent subsequences
- example: considering a min support of 2:  $&lt;(\text{ab})c&gt;$  is a sequential pattern
- challenges?

|  SID | sequence  |
| --- | --- |
|  10 | <a(abc)(ac)d(cf)>  |
|  20 | <(ad)c(bc)(ae)>  |
|  30 | <(ef)(ab)(df)cb>  |
|  40 | <eg(af)cbc>  |

- Extend the definition to further guarantee:
- statistical significance of sequential patterns (unexpectedly high frequency)
- ability to incorporate various kinds of user-specific constraints to focus on novel, actionable and non-trivial patterns

TÉCNICO+ FORMACÃO AVANÇADA