# Python Client for Embeddings (BGE-M3)

This guide shows how to interact with the **Embeddings (TEI)** service using the project's internal client for data science and RAG workflows.

## Prerequisites

Ensure you have the environment variables set in `.env`.

## 1. Basic Embedding Generation

Using the `EmbeddingsClient`:

```python
from services.embeddings import get_embeddings_client

client = get_embeddings_client()
text = "O futuro da infraestrutura é agentic."
vector = client.generate(text)

# Handle potential list-of-lists response if necessary
if isinstance(vector, list) and len(vector) > 0 and isinstance(vector[0], list):
    vector = vector[0]

print(f"Generated vector with {len(vector)} dimensions.")
```

## 2. Integration with PostgreSQL (pgvector)

Ensure you have a Cloudflare Tunnel active if running locally.

```python
from services.postgres import get_postgres_client
from services.embeddings import get_embeddings_client

# 1. Generate Embedding
emb_client = get_embeddings_client()
text = "Armazenando pensamentos vectoriais."
vector = emb_client.generate(text)

# 2. Store in Postgres (datascience db)
with get_postgres_client(database="datascience") as db:
    # Ensure pgvector is enabled
    db.execute("CREATE EXTENSION IF NOT EXISTS vector")
    
    # Create table for 1024-dim vectors (BGE-M3)
    db.execute("""
        CREATE TABLE IF NOT EXISTS thoughts (
            id serial PRIMARY KEY, 
            content text, 
            vec vector(1024)
        )
    """)
    
    # Insert (pgvector accepts list as string or via specialized adapters)
    db.execute(
        "INSERT INTO thoughts (content, vec) VALUES (:content, :vec)",
        params={"content": text, "vec": str(vector)}
    )

print("✅ Vectorized thought stored in Postgres.")
```

## 3. Semantic Search

```python
def semantic_search(query_text):
    emb_client = get_embeddings_client()
    query_vec = emb_client.generate(query_text)
    
    with get_postgres_client(database="datascience") as db:
        # Use <=> for cosine similarity
        df = db.read_sql("""
            SELECT content, 1 - (vec <=> :query_vec) as similarity
            FROM thoughts
            ORDER BY vec <=> :query_vec
            LIMIT 5
        """, params={"query_vec": str(query_vec)})
        
        for _, row in df.iterrows():
            print(f"[{row['similarity']:.4f}] {row['content']}")

semantic_search("inteligência artificial")
```

