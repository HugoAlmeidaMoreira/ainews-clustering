# Example: relational patterns

- Relational patterns involve multiple relations from a relational database
- Typically stated in a more expressive language
- relational classification rules
- relational regression trees
- relational association rules

```txt
IF Customer(C1,N1,FN1,Str1,City1,Zip1,Sex1,SoSt1,In1,Age1,Resp1)
AND order(C1,O1,S1,Deliv1, Pay1)
AND Pay1 = credit_card AND In1 ≥ 108000
THEN Resp1 = Yes
```

- Relation in a relational database: predicate in predicate logic
- Relational pattern can be expressed in a subset of first-order logic

```txt
good_customer(C1) ←
customer(C1, N1, FN1, Str1, City1, Zip1, Sex1, SoSt1, In1, Age1, Resp1) ∧
order(C1, O1, S1, Deliv1, credit_card) ∧ In1 ≥ 108000
```

92

TÉCNICO+

FORMAÇÃO AVANÇADA