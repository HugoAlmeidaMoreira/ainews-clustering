import sys
import os
from dotenv import load_dotenv

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.services.embeddings import EmbeddingsClient
from src.modules.database import get_datascience_db

def main():
    load_dotenv()
    
    # Target the new Qwen model
    MODEL_ID = "Qwen/Qwen3-Embedding-8B"
    print(f"🚀 Testing Qwen Embedding Model: {MODEL_ID}")
    
    client = EmbeddingsClient(model=MODEL_ID)
    text = "A inteligência artificial do Qwen está agora ativa na Blackwell."
    print(f"📡 Generating embedding for: '{text}'")
    
    try:
        vector = client.generate(text)
        print(f"✅ Generated vector with {len(vector)} dimensions.")
        print(f"📊 First 5 values: {vector[:5]}")
        
        # 2. Store in a dedicated column for comparison
        print("\n🐘 Connecting to Postgres to prepare Qwen column...")
        with get_datascience_db() as db:
            db.execute("CREATE EXTENSION IF NOT EXISTS vector")
            # Qwen 8B usually has 1536 or 3072 or 4096 dimensions depending on the variant, 
            # let's detect from the vector itself
            dim = len(vector)
            db.execute(f"ALTER TABLE ai_news ADD COLUMN IF NOT EXISTS embedding_qwen_8b vector({dim})")
            
            print(f"📝 Table updated with column embedding_qwen_8b vector({dim})")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
