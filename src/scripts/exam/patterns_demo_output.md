# Demo da Pergunta (Patterns + Biclustering)

- CSV: `src/scripts/exam/exam_template.csv`
- IDs: ['x1', 'x2', 'x3']
- Colunas: `y1`, `y2`, `reference`

## Cálculos-base

- Bicluster B=({x2,x3},{y1,y2}) valores: [[1.0, 3.0], [1.0, 2.0]]
- Quality(constant, modo/total) = 2/4 = 0.5000
- conf({y1=1,y2=3}=>A) = 1.0000
- sup_abs({y2=3,A}) = 2
- sup_rel({y2=3,A}) = 0.6667
- closed({y2=3,A}) = True
- order-preserving perfeito em B (<=) = True
- lift({y1=1}=>A) = 0.7500

## Avaliação das afirmações

- a) quality constante de B = 2/3: FALSE
- b) confidence {y1=1,y2=3} => A é 100%: TRUE
- c) com minsup=2, padrão {y2=3,A} é closed: TRUE
- d) B=({x2,x3},{y1,y2}) é perfect order-preserving: TRUE
- e) lift {y1=1} => A é 2/3: FALSE
- f) suporte relativo {y2=3,A} é 2/3: TRUE
