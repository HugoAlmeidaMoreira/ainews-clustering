# Python Client for Embeddings (BGE-M3)

This guide shows how to interact with the **Embeddings (TEI)** service using Python for data science and RAG workflows.

## Prerequisites

```bash
pip install requests psycopg2-binary pgvector
```

## 1. Basic Embedding Generation

```python
import requests

def get_embedding(text, endpoint="https://embeddings.vectorized.pt/embed"):
    response = requests.post(endpoint, json={"inputs": text})
    response.raise_for_status()
    # TEI usually returns a list [vec] for single input, or list of lists for multiple
    return response.json()[0]

text = "O futuro da infraestrutura é agentic."
vector = get_embedding(text)
print(f"Generated vector with {len(vector)} dimensions.")
```

## 2. Integration with PostgreSQL (pgvector)

Ensure you have a Cloudflare Tunnel or direct connection to Postgres.

```python
import psycopg2
from pgvector.psycopg2 import register_vector

# Connection details (adjust if using tunnel on localhost)
DB_CONFIG = "postgresql://postgres:pass@localhost:5432/datascience"

def store_thought(text, vector):
    conn = psycopg2.connect(DB_CONFIG)
    register_vector(conn)
    cur = conn.cursor()
    
    # 1. Setup (do once)
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
    cur.execute("CREATE TABLE IF NOT EXISTS thoughts (id serial PRIMARY KEY, content text, vec vector(1024))")
    
    # 2. Insert
    cur.execute("INSERT INTO thoughts (content, vec) VALUES (%s, %s)", (text, vector))
    conn.commit()
    cur.close()
    conn.close()

store_thought(text, vector)
print("✅ Vectorized thought stored in Postgres.")
```

## 3. Semantic Search

```python
def semantic_search(query_text):
    query_vec = get_embedding(query_text)
    
    conn = psycopg2.connect(DB_CONFIG)
    register_vector(conn)
    cur = conn.cursor()
    
    # Use <=> for cosine similarity
    cur.execute("""
        SELECT content, 1 - (vec <=> %s) as similarity
        FROM thoughts
        ORDER BY vec <=> %s
        LIMIT 5
    """, (query_vec, query_vec))
    
    for content, score in cur.readlines():
        print(f"[{score:.4f}] {content}")
        
    cur.close()
    conn.close()
```
