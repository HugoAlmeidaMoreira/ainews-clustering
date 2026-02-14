# Efficient pattern mining

- Exhaustive discovery of patterns is a highly computational heavy task
- Principle to boost efficiency: downward closure property
- any subset of a frequent pattern is also frequent
- if {beer, diaper, nuts} is frequent, so is {beer, diaper}
- i.e., transactions with {beer, diaper, nuts} also contain {beer, diaper}
- Three major approaches mining approaches (details in Appendix)
- Apriori family (Agrawal and Srikant)
- FP-growth family (Han, Pei &amp; Yin)
- Vertical family (Charm and Zaki)

TÉCNICO+
FORMAÇÃO AVANÇADA
35