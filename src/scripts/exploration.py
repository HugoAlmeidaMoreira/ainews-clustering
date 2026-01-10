# %% [markdown]
# # 📰 AI News Dataset Exploration
# 
# Exploração inicial do dataset de notícias sobre Inteligência Artificial.

# %% Imports e configuração
import pandas as pd
import numpy as np
from pathlib import Path

# Configuração do pandas para melhor visualização
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 100)

# %% Carregar o dataset
DATA_PATH = Path(__file__).parent.parent.parent / "data" / "bronze" / "ai_news.parquet"
df = pd.read_parquet(DATA_PATH)

print(f"✅ Dataset carregado: {df.shape[0]:,} linhas × {df.shape[1]} colunas")

# %% [markdown]
# ## 1. Visão Geral do Dataset

# %% Shape e tipos de dados
print("📊 SHAPE DO DATASET")
print("=" * 50)
print(f"Linhas:  {df.shape[0]:,}")
print(f"Colunas: {df.shape[1]}")
print()

print("📋 COLUNAS E TIPOS")
print("=" * 50)
print(df.dtypes)

# %% Primeiras linhas
print("\n🔍 PRIMEIRAS 5 LINHAS")
print("=" * 50)
df.head()

# %% Valores nulos
print("\n⚠️ VALORES NULOS POR COLUNA")
print("=" * 50)
null_counts = df.isnull().sum()
null_pct = 100 * null_counts / len(df)
null_df = pd.DataFrame({
    'Nulos': null_counts,
    'Percentagem': null_pct.round(1)
})
print(null_df[null_df['Nulos'] > 0])

# %% [markdown]
# ## 2. Análise de Colunas Categóricas

# %% Distribuição de tópicos
print("\n📌 DISTRIBUIÇÃO DE TÓPICOS")
print("=" * 50)
topic_counts = df['topic'].value_counts()
print(topic_counts)

# %% Distribuição de tags
print("\n🏷️ DISTRIBUIÇÃO DE TAGS")
print("=" * 50)
print(df['tag'].value_counts())

# %% Distribuição de âmbito
print("\n🌍 DISTRIBUIÇÃO DE ÂMBITO")
print("=" * 50)
print(df['Âmbito'].value_counts())

# %% Top 10 fontes
print("\n📰 TOP 10 FONTES")
print("=" * 50)
print(df['source'].value_counts().head(10))

# %% [markdown]
# ## 3. Análise Temporal

# %% Converter datas
df['pubDate_parsed'] = pd.to_datetime(df['pubDate'], errors='coerce')
df['year'] = df['pubDate_parsed'].dt.year
df['month'] = df['pubDate_parsed'].dt.month
df['year_month'] = df['pubDate_parsed'].dt.to_period('M')

# %% Range temporal
print("\n📅 RANGE TEMPORAL")
print("=" * 50)
print(f"Data mais antiga: {df['pubDate_parsed'].min()}")
print(f"Data mais recente: {df['pubDate_parsed'].max()}")

# %% Distribuição por ano
print("\n📆 NOTÍCIAS POR ANO")
print("=" * 50)
print(df['year'].value_counts().sort_index())

# %% [markdown]
# ## 4. Análise de Texto

# %% Comprimento dos títulos e descrições
df['title_len'] = df['title'].str.len()
df['description_len'] = df['description'].str.len()

print("\n📝 ESTATÍSTICAS DE COMPRIMENTO DE TEXTO")
print("=" * 50)
print(df[['title_len', 'description_len']].describe())

# %% Exemplo de títulos por tópico
print("\n📰 EXEMPLOS DE TÍTULOS POR TÓPICO")
print("=" * 50)
for topic in df['topic'].unique()[:5]:
    print(f"\n--- {topic} ---")
    sample_titles = df[df['topic'] == topic]['title'].head(3).tolist()
    for title in sample_titles:
        print(f"  • {title[:80]}...")

# %% [markdown]
# ## 5. Preparação para Clustering
# 
# Próximos passos:
# - Limpeza e normalização de texto
# - Vectorização (TF-IDF, embeddings)
# - Clustering (K-Means, HDBSCAN)
# - Avaliação de clusters

# %% Resumo das colunas úteis para clustering
print("\n🎯 COLUNAS ÚTEIS PARA CLUSTERING")
print("=" * 50)
print("""
Texto principal:
  • title - Título da notícia
  • description - Corpo/descrição da notícia

Metadados para análise:
  • topic - Tópico atribuído (21 valores únicos) - pode servir como ground truth
  • tag - Tag atribuída (3 valores únicos)
  • source - Fonte da notícia (908 fontes)
  • pubDate - Data de publicação
  • Âmbito - Âmbito geográfico/temático (18 valores únicos)
""")

# %% Verificar unicidade de topic vs tag
print("\n🔗 RELAÇÃO TOPIC vs TAG")
print("=" * 50)
topic_tag = df.groupby('topic')['tag'].unique()
print(topic_tag)
