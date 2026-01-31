import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.modules.database import get_datascience_db

with get_datascience_db() as db:
    print("🛠️ Migrating ai_news_semantics table to composite Primary Key...")
    try:
        # 1. Drop the old primary key
        # Using a transaction block is usually safer, but DatabaseManager.execute might handle it
        print("   - Removing old PK (guid)...")
        db.execute("ALTER TABLE ai_news_semantics DROP CONSTRAINT IF EXISTS ai_news_semantics_pkey;")
        
        # 2. Add the new composite primary key
        print("   - Adding new composite PK (guid, model_name)...")
        db.execute("ALTER TABLE ai_news_semantics ADD PRIMARY KEY (guid, model_name);")
        
        print("✅ Migration successful!")
        
    except Exception as e:
        print(f"❌ Error during migration: {e}")
        print("Note: If the migration failed due to duplicate keys, you might need to clean the table first.")
