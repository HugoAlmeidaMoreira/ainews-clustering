#!/usr/bin/env python3
"""
Extract AI Context Snippets (ADR-006)
======================================
Pre-computes context windows around AI term mentions and stores them in the database.
This improves semantic_painter.py performance and consistency.
"""

import os
import sys
import re
import json
from typing import List, Dict
from tqdm import tqdm
import psycopg2
from psycopg2.extras import execute_values

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from src.modules.database import get_datascience_db, get_database_url

# ============================================================================
# CONFIGURATION
# ============================================================================

# Same regex as enrich_ai_mentions.py for consistency
REGEX_PATTERN = r"(?i)\b(intelig[eê]ncia\s+artificial|artificial\s+intelligence|ai\s+act)\b"

# Context window sizes
CHARS_BEFORE = 200
CHARS_AFTER = 300
MAX_SNIPPETS = 3  # Limit to avoid overwhelming LLM
FALLBACK_LENGTH = 400  # Lead paragraph fallback (ADR-005)

# ============================================================================
# EXTRACTION LOGIC
# ============================================================================

def extract_context_snippets(text: str, max_snippets: int = MAX_SNIPPETS) -> List[Dict]:
    """
    Extract context windows around AI term mentions.
    
    Args:
        text: Article description text
        max_snippets: Maximum number of snippets to extract
        
    Returns:
        List of dicts with 'term', 'snippet', 'position'
    """
    if not text:
        return []
    
    # Compile regex
    regex = re.compile(REGEX_PATTERN)
    
    # Find all matches
    matches = list(regex.finditer(text))
    
    if not matches:
        # Fallback to Lead Paragraph (ADR-005)
        return [{
            "term": "lead_paragraph",
            "snippet": text[:FALLBACK_LENGTH] + ("..." if len(text) > FALLBACK_LENGTH else ""),
            "position": 0
        }]
    
    snippets = []
    used_ranges = []  # Track used character ranges to avoid overlaps
    
    for match in matches[:max_snippets]:  # Limit to max_snippets
        start_pos = match.start()
        end_pos = match.end()
        matched_term = match.group(0)
        
        # Calculate context window
        snippet_start = max(0, start_pos - CHARS_BEFORE)
        snippet_end = min(len(text), end_pos + CHARS_AFTER)
        
        # Check for overlap with existing snippets
        overlaps = False
        for used_start, used_end in used_ranges:
            if not (snippet_end < used_start or snippet_start > used_end):
                overlaps = True
                break
        
        if overlaps:
            continue  # Skip overlapping snippets
        
        # Extract snippet
        snippet_text = text[snippet_start:snippet_end]
        
        # Add ellipsis if not at boundaries
        prefix = "..." if snippet_start > 0 else ""
        suffix = "..." if snippet_end < len(text) else ""
        snippet_text = f"{prefix}{snippet_text}{suffix}"
        
        # Clean up whitespace
        snippet_text = " ".join(snippet_text.split())
        
        snippets.append({
            "term": matched_term,
            "snippet": snippet_text,
            "position": start_pos
        })
        
        used_ranges.append((snippet_start, snippet_end))
    
    return snippets

# ============================================================================
# DATABASE OPERATIONS
# ============================================================================

def ensure_column_exists():
    """Create the ai_context_snippets column if it doesn't exist."""
    print("🛠️  Checking schema...")
    with get_datascience_db() as db:
        db.execute("""
            ALTER TABLE ai_news 
            ADD COLUMN IF NOT EXISTS ai_context_snippets JSONB DEFAULT '[]'::jsonb;
        """)
    print("✅ Schema ready.")

def process_and_update():
    """Extract contexts for all articles and update the database."""
    print("📖 Fetching articles...")
    with get_datascience_db() as db:
        df = db.read_sql("SELECT guid, description FROM ai_news")
    
    print(f"🔍 Extracting context snippets for {len(df)} articles...")
    
    updates = []
    stats = {
        "with_ai_terms": 0,
        "fallback_lead": 0,
        "total_snippets": 0
    }
    
    for _, row in tqdm(df.iterrows(), total=len(df)):
        guid = row['guid']
        description = row['description'] or ""
        
        snippets = extract_context_snippets(description)
        
        # Update stats
        if snippets and snippets[0]['term'] == "lead_paragraph":
            stats["fallback_lead"] += 1
        else:
            stats["with_ai_terms"] += 1
        stats["total_snippets"] += len(snippets)
        
        # Convert to JSON string
        snippets_json = json.dumps(snippets, ensure_ascii=False)
        
        updates.append((snippets_json, guid))
    
    print(f"\n📊 Extraction Statistics:")
    print(f"   Articles with AI terms: {stats['with_ai_terms']:,}")
    print(f"   Articles using fallback (lead paragraph): {stats['fallback_lead']:,}")
    print(f"   Total snippets extracted: {stats['total_snippets']:,}")
    print(f"   Average snippets per article: {stats['total_snippets']/len(df):.2f}")
    
    print("\n💾 Updating database...")
    
    # Batch update using raw psycopg2 for performance
    conn = psycopg2.connect(get_database_url(database="datascience"))
    cur = conn.cursor()
    
    sql = """
        UPDATE ai_news
        SET ai_context_snippets = data.snippets::jsonb
        FROM (VALUES %s) AS data (snippets, guid)
        WHERE ai_news.guid = data.guid
    """
    
    execute_values(cur, sql, updates, page_size=1000)
    conn.commit()
    conn.close()
    
    print("🎉 Done! Context snippets extracted and stored.")

def validate_extraction(sample_size: int = 5):
    """Show sample extractions for validation."""
    print(f"\n🔬 Validation: Showing {sample_size} sample extractions...\n")
    
    with get_datascience_db() as db:
        df = db.read_sql(f"""
            SELECT guid, title, ai_context_snippets
            FROM ai_news
            WHERE jsonb_array_length(ai_context_snippets) > 0
            ORDER BY RANDOM()
            LIMIT {sample_size}
        """)
    
    for idx, row in df.iterrows():
        print(f"{'='*80}")
        print(f"Article: {row['title'][:70]}...")
        print(f"GUID: {row['guid'][:50]}...")
        
        snippets = json.loads(row['ai_context_snippets']) if isinstance(row['ai_context_snippets'], str) else row['ai_context_snippets']
        
        for i, snippet in enumerate(snippets, 1):
            print(f"\n  Snippet {i} (term: '{snippet['term']}'):")
            print(f"  {snippet['snippet'][:200]}...")
        print()

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    ensure_column_exists()
    process_and_update()
    validate_extraction(sample_size=5)
