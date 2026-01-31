#!/usr/bin/env python3
"""
Enrich AI Mentions
==================
Adds columns to ai_news to flag explicit mentions of "Artificial Intelligence".
- has_ai_in_title (BOOL)
- ai_mentions_description (INT)
"""

import os
import sys
import re
import psycopg2
from psycopg2.extras import execute_values
from tqdm import tqdm

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from src.modules.database import get_datascience_db

# ============================================================================
# CONFIGURATION
# ============================================================================

# Robust regex for PT/EN variations
# Handles: "Inteligência Artificial", "Inteligencia Artificial", "Artificial Intelligence"
# \b ensures word boundaries
REGEX_PATTERN = r"(?i)\b(intelig[eê]ncia\s+artificial|artificial\s+intelligence|ai\s+act)\b"

def ensure_columns_exist():
    """Create the new columns if they don't exist."""
    print("🛠️  Checking schema...")
    with get_datascience_db() as db:
        db.execute("""
            ALTER TABLE ai_news 
            ADD COLUMN IF NOT EXISTS has_ai_in_title BOOLEAN DEFAULT FALSE;
        """)
        db.execute("""
            ALTER TABLE ai_news 
            ADD COLUMN IF NOT EXISTS ai_mentions_description INTEGER DEFAULT 0;
        """)
    print("✅ Schema ready.")

def process_and_update():
    print("📖 Fetching data...")
    with get_datascience_db() as db:
        # Fetch only needed fields
        df = db.read_sql("SELECT guid, title, description FROM ai_news")
    
    print(f"🔍 Processing {len(df)} records with Regex...")
    
    updates = []
    
    # Compile regex for speed
    regex = re.compile(REGEX_PATTERN)
    
    for _, row in tqdm(df.iterrows(), total=len(df)):
        guid = row['guid']
        title = row['title'] or ""
        desc = row['description'] or ""
        
        # 1. Check Title (Boolean)
        has_ai = bool(regex.search(title))
        
        # 2. Count Description (Integer)
        # findall returns list of all non-overlapping matches
        count_ai = len(regex.findall(desc))
        
        updates.append((has_ai, count_ai, guid))
        
    print("💾 Updating database...")
    
    # Batch update using raw psycopg2 for performance
    # (SQLAlchemy ORM is too slow for 12k updates)
    from src.modules.database import get_database_url
    conn = psycopg2.connect(get_database_url(database="datascience"))
    cur = conn.cursor()
    
    sql = """
        UPDATE ai_news
        SET 
            has_ai_in_title = data.has_ai,
            ai_mentions_description = data.count_ai
        FROM (VALUES %s) AS data (has_ai, count_ai, guid)
        WHERE ai_news.guid = data.guid
    """
    
    execute_values(cur, sql, updates, page_size=1000)
    conn.commit()
    conn.close()
    
    print("🎉 Done! Database enriched.")

if __name__ == "__main__":
    ensure_columns_exist()
    process_and_update()
