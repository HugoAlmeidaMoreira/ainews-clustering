import sys
import os
from dotenv import load_dotenv

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.services.embeddings import get_embeddings_client
from src.modules.database import get_datascience_db

def main():
    load_dotenv()
    
    print("🚀 Starting Embeddings + Postgres Integration Test")
    
    # 1. Get Embedding
    client = get_embeddings_client()
    text = "A inteligência artificial está a transformar o mundo de forma acelerada."
    print(f"📡 Generating embedding for: '{text}'")
    
    try:
        vector = client.generate(text)
        # Handle TEI response format (usually a list of lists if single input or list of floats)
        if isinstance(vector, list) and len(vector) > 0 and isinstance(vector[0], list):
            vector = vector[0]
            
        print(f"✅ Generated vector with {len(vector)} dimensions.")
        print(f"📊 First 5 values: {vector[:5]}")
        
        # 2. Store in Postgres
        print("\n🐘 Connecting to Postgres (datascience db)...")
        with get_datascience_db() as db:
            # Enable pgvector
            print("🔧 Ensuring pgvector extension is enabled...")
            db.execute("CREATE EXTENSION IF NOT EXISTS vector")
            
            # Create test table
            print("📝 Creating test_embeddings table...")
            # BGE-M3 usually has 1024 dimensions
            dim = len(vector)
            db.execute(f"CREATE TABLE IF NOT EXISTS test_embeddings (id serial PRIMARY KEY, content text, embedding vector({dim}))")
            
            # Insert data
            print("💾 Saving embedding to database...")
            # Convert vector to string format for pgvector if needed, or use sqlalchemy parameters
            # pgvector likes lists or strings like '[1,2,3]'
            db.execute(
                "INSERT INTO test_embeddings (content, embedding) VALUES (:content, :embedding)",
                params={"content": text, "embedding": str(vector)}
            )
            
            # Verify
            print("🔍 Verifying insertion...")
            df = db.read_sql("SELECT content, embedding FROM test_embeddings ORDER BY id DESC LIMIT 1")
            print("✅ Successfully retrieved from DB:")
            print(f"   Content: {df['content'].iloc[0]}")
            # The embedding comes back as a string from pandas usually, or a vector if using pgvector-python
            print(f"   Embedding (start): {str(df['embedding'].iloc[0])[:50]}...")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
