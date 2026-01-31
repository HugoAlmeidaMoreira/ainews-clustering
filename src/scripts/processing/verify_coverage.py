#!/usr/bin/env python3
"""
Verify Coverage After AI Act Addition
======================================
Check if there are still missing articles after adding 'AI Act' to the regex.
"""

import sys
import os
import re

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from src.modules.database import get_datascience_db

def verify_coverage():
    print("🔍 Verifying coverage after 'AI Act' addition...\n")
    
    with get_datascience_db() as db:
        # Get the UPDATED data (after running enrich_ai_mentions.py)
        query = """
            SELECT guid, title, description, has_ai_in_title, ai_mentions_description
            FROM ai_news
        """
        df = db.read_sql(query)
    
    # Current detection logic (same as in enrich_ai_mentions.py)
    # Articles are "detected" if has_ai_in_title OR ai_mentions_description > 0
    df['detected'] = df['has_ai_in_title'] | (df['ai_mentions_description'] > 0)
    
    total = len(df)
    detected = df['detected'].sum()
    not_detected = total - detected
    
    print(f"📊 Coverage Statistics:")
    print(f"   Total Articles: {total:,}")
    print(f"   ✅ Detected (has AI mentions): {detected:,} ({100*detected/total:.2f}%)")
    print(f"   ❌ Not Detected: {not_detected:,} ({100*not_detected/total:.2f}%)")
    
    # Check specifically for "AI Act" coverage
    aiact_pattern = r"(?i)\b(ai\s+act|aiact)\b"
    df['has_aiact'] = df['description'].fillna('').str.contains(aiact_pattern, regex=True) | \
                      df['title'].fillna('').str.contains(aiact_pattern, regex=True)
    
    aiact_total = df['has_aiact'].sum()
    aiact_detected = df[df['has_aiact'] & df['detected']].shape[0]
    aiact_missed = df[df['has_aiact'] & ~df['detected']].shape[0]
    
    print(f"\n🎯 'AI Act' Specific Coverage:")
    print(f"   Articles mentioning 'AI Act': {aiact_total:,}")
    print(f"   ✅ Detected: {aiact_detected:,} ({100*aiact_detected/aiact_total:.2f}%)")
    print(f"   ❌ Missed: {aiact_missed:,} ({100*aiact_missed/aiact_total:.2f}%)")
    
    if aiact_missed > 0:
        print(f"\n⚠️ Still missing {aiact_missed} 'AI Act' articles!")
        print("\nExamples of MISSED 'AI Act' articles:")
        missed_df = df[df['has_aiact'] & ~df['detected']]
        for _, row in missed_df.head(5).iterrows():
            print(f"  - [{row['guid'][:50]}...] {row['title']}")
            # Check why it was missed
            title_match = bool(re.search(aiact_pattern, row['title'] or ''))
            desc_match = bool(re.search(aiact_pattern, row['description'] or ''))
            print(f"    'AI Act' in title: {title_match}, in description: {desc_match}")
            print(f"    has_ai_in_title: {row['has_ai_in_title']}, ai_mentions_description: {row['ai_mentions_description']}")
    else:
        print(f"\n🎉 Perfect! All 'AI Act' articles are now detected!")
    
    # Show breakdown of what's NOT detected (to understand the remaining articles)
    if not_detected > 0:
        print(f"\n📋 Sample of articles NOT detected (no AI terms):")
        not_detected_df = df[~df['detected']]
        for _, row in not_detected_df.head(3).iterrows():
            print(f"  - {row['title'][:80]}...")

if __name__ == "__main__":
    verify_coverage()
