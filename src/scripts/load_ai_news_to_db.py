#!/usr/bin/env python3
"""
Load ai_news.parquet into PostgreSQL database.

Run: uv run python src/scripts/load_ai_news_to_db.py

Requires active cloudflared tunnel:
    cloudflared access tcp --hostname postgres.hugomoreira.eu --url localhost:5432
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

from src.modules.database import get_engine

# Load environment variables
load_dotenv()


def main() -> None:
    """Load ai_news parquet file into PostgreSQL."""
    parquet_path = Path("data/bronze/ai_news.parquet")

    print(f"📂 A carregar {parquet_path}...")
    df = pd.read_parquet(parquet_path)
    print(f"   Shape: {df.shape[0]} linhas × {df.shape[1]} colunas")

    # Clean column names (remove special characters)
    df.columns = [
        col.lower()
        .replace("â", "a")
        .replace(" ", "_")
        for col in df.columns
    ]
    print(f"   Colunas: {list(df.columns)}")

    # Connect to PostgreSQL
    print("\n🔗 A ligar ao PostgreSQL...")
    engine = get_engine()

    # Create datascience database if it doesn't exist
    print("\n📦 A criar database 'datascience' (se não existir)...")
    with engine.connect() as conn:
        # Check if database exists
        result = conn.execute(
            text("SELECT 1 FROM pg_database WHERE datname = 'datascience'")
        )
        if not result.fetchone():
            # Need to commit current transaction and use autocommit for CREATE DATABASE
            conn.execute(text("COMMIT"))
            conn.execute(text("CREATE DATABASE datascience"))
            print("   ✅ Database 'datascience' criada!")
        else:
            print("   ℹ️ Database 'datascience' já existe")

    # Connect to datascience database - build URL from env
    print("\n📤 A carregar dados para tabela 'ai_news'...")
    base_url = os.getenv("POSTGRES_URL")
    # Replace /postgres with /datascience
    datascience_url = base_url.rsplit("/", 1)[0] + "/datascience"
    ds_engine = create_engine(datascience_url)

    # Write DataFrame to table
    rows = df.to_sql(
        name="ai_news",
        con=ds_engine,
        if_exists="replace",
        index=False,
        method="multi",  # Faster batch inserts
        chunksize=1000,
    )

    print(f"   ✅ {len(df)} linhas inseridas na tabela 'ai_news'!")

    # Verify
    print("\n🔍 A verificar...")
    result = pd.read_sql("SELECT COUNT(*) as count FROM ai_news", ds_engine)
    print(f"   Linhas na tabela: {result['count'].iloc[0]}")

    # Show sample
    sample = pd.read_sql("SELECT title, source, category FROM ai_news LIMIT 3", ds_engine)
    print("\n📋 Amostra:")
    for _, row in sample.iterrows():
        print(f"   • {row['title'][:60]}... ({row['source']})")

    print("\n✅ Concluído!")


if __name__ == "__main__":
    main()
