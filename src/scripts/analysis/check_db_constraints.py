import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.modules.database import get_datascience_db

with get_datascience_db() as db:
    # Check current table structure and constraints
    print("📋 Checking ai_news_semantics table structure...")
    try:
        # Check standard columns
        df_cols = db.read_sql("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'ai_news_semantics'")
        print("\nColumns:")
        print(df_cols)
        
        # Check constraints (PK/Unique)
        query_constraints = """
            SELECT conname, contype, pg_get_constraintdef(c.oid) as def
            FROM pg_constraint c
            JOIN pg_namespace n ON n.oid = c.connamespace
            WHERE conrelid = 'ai_news_semantics'::regclass;
        """
        df_cons = db.read_sql(query_constraints)
        print("\nConstraints:")
        print(df_cons)
        
    except Exception as e:
        print(f"❌ Error: {e}")
