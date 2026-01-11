# 📊 Descrição de Datasets - Conceitos Fundamentais

## Anatomia de um Dataset

Um dataset tabular pode ser descrito por três dimensões principais:

```
                    ← ─ ─ ─ ─  dimensionalidade  ─ ─ ─ ─ →
                    
                         Y₁    Y₂   ...   Yₘ    Z₁    Zₚ
                       ┌─────┬─────┬─────┬─────┬─────┬─────┐
                   X₁  │     │     │     │     │     │     │
                       ├─────┼─────┼─────┼─────┼─────┼─────┤
         ↑         X₂  │     │     │     │     │  ●  │     │  ← variável categórica
         │             ├─────┼─────┼─────┼─────┼─────┼─────┤      cardinalidade |Σ|
       size        X₃  │     │     │     │     │     │     │
         │             ├─────┼─────┼─────┼─────┼─────┼─────┤
         ↓        Xₙ   │     │     │     │     │     │     │
                       └─────┴─────┴─────┴─────┴─────┴─────┘
```

---

## 1. Size (Tamanho) - `n`

**O que é:** Número de observações/linhas/registos no dataset.

```python
# Em pandas
n = len(df)           # ou
n = df.shape[0]
```

**No nosso dataset:**
- `n = 11,922` notícias

---

## 2. Dimensionality (Dimensionalidade) - `m + p`

**O que é:** Número total de features/colunas/variáveis.

- **Variáveis numéricas (Y):** Valores contínuos ou discretos
- **Variáveis categóricas (Z):** Valores de um conjunto finito

```python
# Em pandas
dimensionality = df.shape[1]
```

**No nosso dataset:**
- `dimensionalidade = 15` colunas

---

## 3. Cardinality (Cardinalidade) - `|Σ|`

**O que é:** Número de modalidades (valores únicos/distintos) de uma variável categórica.

> A cardinalidade indica quantos valores diferentes uma variável pode assumir.

```python
# Em pandas
cardinalidade = df['coluna'].nunique()

# Para todas as colunas categóricas
for col in df.select_dtypes(include='object'):
    print(f"{col}: {df[col].nunique()} modalidades")
```

### Classificação por Cardinalidade

| Tipo | Cardinalidade | Exemplo no dataset |
|------|---------------|-------------------|
| **Baixa** | 2-10 | `tag` (3 modalidades) |
| **Média** | 10-100 | `topic` (21), `Âmbito` (18) |
| **Alta** | 100-1000 | `source` (908 fontes) |
| **Muito Alta** | >1000 | `title` (9,783 títulos únicos) |

### No contexto do Dataset AI News

| Variável | Cardinalidade | Notas |
|----------|---------------|-------|
| `tag` | 3 | Baixa - fácil para modelação |
| `topic` | 21 | Média - bom para classificação |
| `Âmbito` | 18 | Média |
| `source` | 908 | Alta - pode precisar de agrupamento |
| `title` | 9,783 | Muito alta - texto livre |

**⚠️ Nota:** Variáveis de cardinalidade muito alta podem ser:
- **Identificadores únicos** (não úteis para modelação)
- **Texto livre** (requer NLP)

---

## 4. Outras Métricas Importantes

### 4.1 Sparsity (Dispersão)
Percentagem de valores nulos/em falta:

```python
sparsity = df.isnull().sum() / len(df) * 100
```

**No nosso dataset:**
- `enclosure`: 100% nulo (coluna vazia)
- `Autores`: 56.9% nulo
- `Engaged`: 61.0% nulo

### 4.2 Densidad de Informação
```python
# Bytes por registo
density = df.memory_usage(deep=True).sum() / len(df)
```

### 4.3 Distribuição de Classes (para classificação)
```python
# Balance das classes
class_distribution = df['topic'].value_counts(normalize=True)
```

---

## 5. Resumo do Dataset AI News

| Métrica | Valor | Interpretação |
|---------|-------|---------------|
| **Size (n)** | 11,922 | Dataset de tamanho médio |
| **Dimensionalidade** | 15 | Baixa dimensionalidade |
| **Cardinalidade `topic`** | 21 | Multi-class classification viável |
| **Cardinalidade `source`** | 908 | Alta - pode precisar de agrupamento |
| **Cardinalidade `tag`** | 3 | Binária/ternária |
| **Sparsity máx** | 61% (`Engaged`) | Atenção ao usar esta feature |
| **Range temporal** | 2021-2024 | ~3 anos de dados |

---

## 6. Código de Análise Rápida

```python
def describe_dataset(df):
    """Análise rápida de um dataset."""
    print(f"📊 SIZE: {len(df):,} registos")
    print(f"📐 DIMENSIONALITY: {df.shape[1]} colunas")
    print()
    print("📋 CARDINALITY por coluna:")
    for col in df.columns:
        card = df[col].nunique()
        null_pct = 100 * df[col].isnull().sum() / len(df)
        dtype = "📝" if df[col].dtype == 'object' else "🔢"
        print(f"  {dtype} {col}: {card:,} únicos | {null_pct:.1f}% nulos")
```

---

## Referências

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn: Dataset transformations](https://scikit-learn.org/stable/data_transforms.html)
