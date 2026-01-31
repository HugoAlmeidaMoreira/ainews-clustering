#!/usr/bin/env python3
"""
Test Semantic Painter with Pre-computed Snippets
=================================================
Quick validation that semantic_painter.py works with ai_context_snippets.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.scripts.analysis.semantic_painter import get_cluster_representatives

def test_snippet_extraction():
    """Test that we can fetch and parse pre-computed snippets."""
    print("🧪 Testing semantic_painter with pre-computed snippets...\n")
    
    # Test with cluster 0 from HDBSCAN (should have data)
    cluster_id = 0
    method = "cluster_hdbscan"
    
    print(f"Fetching representatives for cluster {cluster_id} ({method})...")
    articles_df, avg_scores = get_cluster_representatives(cluster_id, method, limit=3)
    
    if articles_df.empty:
        print("❌ No articles found for this cluster!")
        return
    
    print(f"✅ Found {len(articles_df)} articles\n")
    
    # Show what we got
    print("📋 Sample articles with pre-computed snippets:\n")
    for idx, row in articles_df.iterrows():
        print(f"{'='*70}")
        print(f"Title: {row['title'][:60]}...")
        print(f"Source: {row['source']}")
        
        # Parse snippets
        import json
        snippets = row['ai_context_snippets']
        if isinstance(snippets, str):
            snippets = json.loads(snippets)
        
        print(f"Number of snippets: {len(snippets)}")
        for i, snippet in enumerate(snippets[:2], 1):
            print(f"\nSnippet {i} (term: '{snippet['term']}'):")
            print(f"{snippet['snippet'][:150]}...")
        print()
    
    # Show semantic profile
    print(f"\n📊 Average Semantic Profile for cluster {cluster_id}:")
    for key, value in avg_scores.items():
        print(f"   {key}: {value:.2f}")
    
    print("\n✅ Test passed! semantic_painter.py is ready to use pre-computed snippets.")

if __name__ == "__main__":
    test_snippet_extraction()
