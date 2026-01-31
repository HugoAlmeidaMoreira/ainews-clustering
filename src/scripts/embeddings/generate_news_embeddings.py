import sys
import os
import pandas as pd
from tqdm import tqdm
import time

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.services.embeddings import EmbeddingsClient, get_embeddings_client
from src.modules.database import get_datascience_db

def truncate_text(text, max_chars=8000):
    """Truncate text to stay within reasonable limits for the embedding model."""
    if not text or not isinstance(text, str):
        return ""
    return text[:max_chars]

def process_embeddings(limit=None):
    """
    Fetch news articles, generate embeddings using Qwen-8B, and save back to DB.
    """
    MODEL_ID = "Qwen/Qwen3-Embedding-8B"
    client = EmbeddingsClient(model=MODEL_ID)
    
    print(f"🐘 Connecting to database for model {MODEL_ID}...")
    with get_datascience_db() as db:
        # 1. Ensure the column exists
        print("🔧 Ensuring embedding_qwen_8b column exists...")
        db.execute("CREATE EXTENSION IF NOT EXISTS vector")
        # Qwen-8B uses 4096 dimensions
        db.execute("ALTER TABLE ai_news ADD COLUMN IF NOT EXISTS embedding_qwen_8b vector(4096)")
        
        # 2. Fetch rows that don't have embeddings yet
        query = "SELECT guid, title, description FROM ai_news WHERE embedding_qwen_8b IS NULL"
        if limit:
            query += f" LIMIT {limit}"
            
        print("🔍 Fetching articles without Qwen embeddings...")
        df = db.read_sql(query)
        
        if df.empty:
            print("✅ All articles already have Qwen embeddings!")
            return

        print(f"📦 Found {len(df)} articles to process.")
        
        # 3. Batch processing
        # Using 64 for 8B model to be safer with memory, but could go higher on Blackwell
        batch_size = 64 
        print(f"🚀 Processing in batches of {batch_size} using Qwen-8B...")
        
        for i in tqdm(range(0, len(df), batch_size), desc="Generating Qwen Embeddings", unit="batch"):
            batch = df.iloc[i : i + batch_size]
            
            # Prepare inputs: "Title: [title] \n\n Content: [truncated_desc]"
            inputs = []
            for _, row in batch.iterrows():
                title = row['title'] if row['title'] else ""
                desc = truncate_text(row['description'], max_chars=25000)
                combined = f"Title: {title}\n\nContent: {desc}"
                inputs.append(combined)
            
            try:
                # Generate embeddings
                vectors = client.generate(inputs)
                
                # Update database
                for j, (_, row) in enumerate(batch.iterrows()):
                    guid = row['guid']
                    vector = vectors[j]
                    
                    vector_str = "[" + ",".join(map(str, vector)) + "]"
                    
                    db.execute(
                        "UPDATE ai_news SET embedding_qwen_8b = :vec WHERE guid = :guid",
                        params={"vec": vector_str, "guid": guid}
                    )
                
            except Exception as e:
                print(f"⚠️ Batch starting at {i} failed. Error: {e}")
                print("🔄 Switching to single-item processing for this batch...")
                
                for j, (_, row) in enumerate(batch.iterrows()):
                    try:
                        title = row['title'] if row['title'] else ""
                        desc = truncate_text(row['description'], max_chars=25000)
                        combined = f"Title: {title}\n\nContent: {desc}"
                        
                        vector = client.generate(combined)
                        
                        if isinstance(vector, list) and len(vector) > 0 and isinstance(vector[0], list):
                           vector = vector[0]

                        vector_str = "[" + ",".join(map(str, vector)) + "]"
                        
                        db.execute(
                            "UPDATE ai_news SET embedding_qwen_8b = :vec WHERE guid = :guid",
                            params={"vec": vector_str, "guid": row['guid']}
                        )
                    except Exception as inner_e:
                        print(f"❌ FAILED to process article GUID: {row['guid']}")
                        continue
                continue

    print("🎉 Qwen Embedding generation complete!")

    # Verification Step
    print("\n🔍 Verification: Checking first processed row...")
    with get_datascience_db() as db:
        check = db.read_sql("SELECT title, embedding_qwen_8b FROM ai_news WHERE embedding_qwen_8b IS NOT NULL LIMIT 1")
        if not check.empty:
            vec_s = str(check.iloc[0]['embedding_qwen_8b'])
            print(f"   Title: {check.iloc[0]['title'][:50]}...")
            print(f"   Embedding: {vec_s[:50]}... (Length: 4096)")
        else:
            print("   ❌ No Qwen embeddings found in DB.")

if __name__ == "__main__":
    process_embeddings(limit=None)
