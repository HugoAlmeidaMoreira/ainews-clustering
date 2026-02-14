# Exam Tool (uso rápido)

Ferramenta mínima para resolver exercícios de clustering a partir de CSV.

## 1) Matriz de distância (métrica mista)

```bash
.venv/bin/python src/scripts/exam/exam_tool.py dist \
  --csv src/scripts/exam/dataset_exam_2022.csv \
  --numeric-cols y1,y2 \
  --categorical-cols y3,y4
```

Se quiseres gravar markdown:

```bash
.venv/bin/python src/scripts/exam/exam_tool.py dist \
  --csv src/scripts/exam/dataset_exam_2022.csv \
  --numeric-cols y1,y2 \
  --categorical-cols y3,y4 \
  --out src/scripts/exam/report_exam_tool.md
```

## 2) Silhouette + purity

CSV com colunas de apoio: `obs` (id), `class`, `cluster`.

```bash
.venv/bin/python src/scripts/exam/exam_tool.py cluster \
  --csv /tmp/exam_eval.csv \
  --id-col obs \
  --cluster-col cluster \
  --class-col class \
  --numeric-cols y1,y2 \
  --categorical-cols y3,y4 \
  --silhouette-of x4
```

## 3) Template para preencher no exame

Usa este ficheiro como base:

`src/scripts/exam/exam_template.csv`

## Notas rápidas

- `--metric mixed` = Manhattan(númericas) + Hamming(categóricas)
- Também tens: `euclidean`, `manhattan`, `hamming`
- Se não passares colunas, o script tenta inferir por tipo
