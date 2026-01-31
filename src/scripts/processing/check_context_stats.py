#!/usr/bin/env python3
"""Quick stats check for context extraction"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from src.modules.database import get_datascience_db

with get_datascience_db() as db:
    # Simpler query without FILTER
    result = db.read_sql("""
        SELECT 
            COUNT(*) as total,
            SUM(CASE WHEN jsonb_array_length(ai_context_snippets) > 0 THEN 1 ELSE 0 END) as with_snippets,
            SUM(CASE WHEN ai_context_snippets::text LIKE '%lead_paragraph%' THEN 1 ELSE 0 END) as fallback,
            AVG(jsonb_array_length(ai_context_snippets))::numeric(10,2) as avg_snippets
        FROM ai_news
    """)
    
    row = result.iloc[0]
    print('📊 Context Extraction Statistics:')
    print(f"   Total Articles: {int(row['total']):,}")
    print(f"   With AI context snippets: {int(row['with_snippets']):,}")
    print(f"   Using fallback (lead paragraph): {int(row['fallback']):,}")
    print(f"   Average snippets per article: {float(row['avg_snippets']):.2f}")
