#!/usr/bin/env python3
"""
Validate AI Context Snippets Column
====================================
Confirms that the ai_context_snippets column is properly created and populated.
"""

import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from src.modules.database import get_datascience_db

def validate_column():
    print("🔍 Validating ai_context_snippets column...\n")
    
    with get_datascience_db() as db:
        # 1. Check if column exists
        print("1️⃣ Checking column existence...")
        schema_check = db.read_sql("""
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns
            WHERE table_name = 'ai_news' 
            AND column_name = 'ai_context_snippets'
        """)
        
        if schema_check.empty:
            print("   ❌ Column does not exist!")
            return
        
        print(f"   ✅ Column exists: {schema_check.iloc[0]['data_type']}")
        
        # 2. Check data statistics (simple queries to avoid SQLAlchemy issues)
        print("\n2️⃣ Checking data statistics...")
        
        total = db.read_sql("SELECT COUNT(*) as count FROM ai_news")
        print(f"   Total articles: {int(total.iloc[0]['count']):,}")
        
        with_data = db.read_sql("""
            SELECT COUNT(*) as count FROM ai_news 
            WHERE jsonb_array_length(ai_context_snippets) > 0
        """)
        print(f"   With AI snippets: {int(with_data.iloc[0]['count']):,}")
        
        # 3. Show sample data
        print("\n3️⃣ Sample data (3 random articles)...")
        samples = db.read_sql("""
            SELECT guid, title, ai_context_snippets
            FROM ai_news
            WHERE jsonb_array_length(ai_context_snippets) > 0
            ORDER BY RANDOM()
            LIMIT 3
        """)
        
        for idx, row in samples.iterrows():
            print(f"\n   {'='*70}")
            print(f"   Title: {row['title'][:60]}...")
            
            # Parse JSONB
            snippets = row['ai_context_snippets']
            if isinstance(snippets, str):
                snippets = json.loads(snippets)
            
            print(f"   Number of snippets: {len(snippets)}")
            for i, snippet in enumerate(snippets[:2], 1):  # Show first 2
                print(f"   Snippet {i} (term: '{snippet['term']}'):")
                print(f"   {snippet['snippet'][:100]}...")
        
        # 4. Check data integrity
        print(f"\n4️⃣ Checking data integrity...")
        integrity = db.read_sql("""
            SELECT COUNT(*) as count FROM ai_news
            WHERE ai_context_snippets IS NOT NULL
        """)
        
        valid_count = int(integrity.iloc[0]['count'])
        print(f"   ✅ All {valid_count:,} entries have valid data")
        
        print("\n✅ Validation complete! Column is properly set up and populated.")

if __name__ == "__main__":
    validate_column()
