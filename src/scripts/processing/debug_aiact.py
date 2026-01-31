
import sys
import os
import re
import pandas as pd
from sqlalchemy import text

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from src.modules.database import get_datascience_db

def investigate_aiact():
    print("🔍 Investigating 'aiact' vs current AI detection...")
    
    with get_datascience_db() as db:
        # Get all data for analysis (or a sample if strictly huge, but 12k is fine)
        # We need to see if 'aiact' exists and if it overlaps with current flags
        query = """
            SELECT guid, title, description, has_ai_in_title, ai_mentions_description
            FROM ai_news
        """
        df = db.read_sql(query)
    
    # 1. How many mentions of 'aiact' (case insensitive)?
    # We look for "AI Act", "AI-Act", "AIACT" (unlikely but user said it)
    # The user specifically said "termo que é o aiact". Let's assume matches "AI Act" or "aiact"
    
    aiact_pattern = r"(?i)\b(ai\s*act|aiact)\b" 
    
    df['has_aiact_mentions'] = df['description'].fillna('').str.contains(aiact_pattern, regex=True) | \
                               df['title'].fillna('').str.contains(aiact_pattern, regex=True)
                               
    aiact_count = df['has_aiact_mentions'].sum()
    print(f"Stats:")
    print(f"- Total Articles: {len(df)}")
    print(f"- Articles mentioning 'AI Act'/'aiact': {aiact_count}")
    
    # 2. Overlap with current detection
    # Current detection: has_ai_in_title is True OR ai_mentions_description > 0
    df['currently_detected'] = df['has_ai_in_title'] | (df['ai_mentions_description'] > 0)
    
    detected_aiact = df[df['has_aiact_mentions'] & df['currently_detected']]
    undetected_aiact = df[df['has_aiact_mentions'] & ~df['currently_detected']]
    
    print(f"- 'AI Act' articles CAUGHT by current regex: {len(detected_aiact)}")
    print(f"- 'AI Act' articles MISSED by current regex: {len(undetected_aiact)}")
    
    if len(undetected_aiact) > 0:
        print("\nExamples of MISSED 'AI Act' articles (False Negatives?):")
        for _, row in undetected_aiact.head(5).iterrows():
            print(f"  - [{row['guid']}] {row['title']}")
            
    # 3. Check for specific "false positive" logic user mentioned?
    # If they thought 'aiact' was causing FPs, maybe they meant the word 'act' or something?
    # But let's assume they meant 'AI Act' is important.
    
if __name__ == "__main__":
    investigate_aiact()
