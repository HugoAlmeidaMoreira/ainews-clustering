# Relational data structures

How to mine relational databases?

- naïve solution: bringing all information to a single table
- e.g. customer table where we combine as much info as possible
- problems:
- redundancies
- feature dependence
- how to deal with the multiplicity of orders per customer?
- one line per ‘order’ → analysis results will be about orders, not customers!

|  ID | Name | First Name | ... | Response | Delivery mode | Payment mode | Store size | Store type | Location  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  3478 | Smith | John | ... | Y | regular | cash | small | franchis | city  |
|  3478 | Smith | John | ... | Y | express | check | small | franchis | city  |
|  ... | ... | ... | ... | ... | ... | ... | ... | ... | ...  |

TÉCNICO+ FORMAÇÃO AVANÇADA