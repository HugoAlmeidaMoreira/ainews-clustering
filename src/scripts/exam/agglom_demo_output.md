# Demo da Pergunta (Agglomerative + Manhattan)

- CSV: `src/scripts/exam/exam_template.csv`
- IDs: ['x1', 'x2', 'x3']
- Variáveis numéricas: `y1`, `y2`
- Coluna de referência: `reference`

## Distâncias Manhattan

- d(x1,x2) = 2.0000
- d(x1,x3) = 3.0000
- d(x2,x3) = 1.0000

## Avaliação das afirmações

- A) all observation are merged at distance 2 (single-link): TRUE (merge final = 2.0000)
- B) d(x1,x3) = sqrt(5): FALSE (valor = 3.0000, sqrt(5) = 2.2361)
- C) silhouette(x1) = 0.33 com referência perfeita: TRUE (valor = 0.3333)
- D) x1 e x3 são o primeiro merge em complete-link: FALSE (primeiro merge = x2 & x3, d=1.0000)
- E) purity de {x1}{x2,x3} = 0.66: TRUE (valor = 0.6667)
