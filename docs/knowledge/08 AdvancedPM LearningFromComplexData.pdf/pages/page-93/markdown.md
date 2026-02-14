# Example: relational association rules

|  LIKES  |   |
| --- | --- |
|  KID | OBJECT  |
|  Joni | ice-cream  |
|  Joni | dolphin  |
|  Elliot | piglet  |
|  Elliot | gnu  |
|  Elliot | lion  |
|  HAS  |   |
| --- | --- |
|  KID | OBJECT  |
|  Joni | ice-cream  |
|  Joni | piglet  |
|  Elliot | ice-cream  |
|  PREFERS  |   |   |   |
| --- | --- | --- | --- |
|  KID | OBJECT | TO  |   |
|  Joni | ice-cream | pudding  |   |
|  Joni | pudding | raisins  |   |
|  Joni | giraffe | gnu  |   |
|  Elliot | lion | ice-cream  |   |
|  Elliot | piglet | dolphin  |   |

likes(KID, A), has(KID, B) → prefers(KID, A, B) (70%, 98%)

**WARMR**: iteratively generate candidate $k$-atomsets from $(k-1)$-atomsets until no more large atomsets are found

likes(KID, piglet), likes(KID, ice-cream) atomset

TÉCNICO+

FORMAÇÃO AVANÇADA

93