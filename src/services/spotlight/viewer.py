"""
Renumics Spotlight Service
==========================

Serves the AI News dataset for interactive exploration using Renumics Spotlight.
Reads directly from PostgreSQL ('datascience' database).
"""

import os
import sys

# Ensure we can find the src module from project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
sys.path.append(PROJECT_ROOT)

import pandas as pd
from renumics import spotlight
from dotenv import load_dotenv
from src.modules.database import get_datascience_db

def main():
    load_dotenv()
    
    print("🚀 Connecting to PostgreSQL (datascience)...")
    
    try:
        with get_datascience_db() as db:
            print("📦 Fetching 'ai_news' table...")
            # Fetch all data or a subset if too large
            # For now, fetching everything as per request
            df = db.read_sql("SELECT * FROM ai_news")
            
        print(f"📊 Dataset Loaded: {len(df)} rows, {len(df.columns)} columns")
        
        # Check if we have embeddings to show
        embedding_cols = [c for c in df.columns if "embedding" in c or "vector" in c]
        if embedding_cols:
            print(f"✨ Found embedding columns: {embedding_cols}")
        
        print("✨ Launching Spotlight...")
        
        # Launch Spotlight
        # Default to localhost to avoid TLS requirements
        host = os.getenv("SPOTLIGHT_HOST", "127.0.0.1")
        spotlight.show(df, host=host, port=int(os.getenv("SPOTLIGHT_PORT", 7000)))
        
    except Exception as e:
        print(f"❌ Error loading data from Postgres: {e}")
        print("Ensure the tunnel is active: cloudflared access tcp --hostname postgres.hugomoreira.eu --url localhost:5432")
        sys.exit(1)

if __name__ == "__main__":
    main()
