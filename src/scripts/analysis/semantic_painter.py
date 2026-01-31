#!/usr/bin/env python3
"""
Semantic Painter (ADR-003)
==========================
Uses LLM (vLLM/Qwen-72B) to interpret and label the topographic clusters found by HDBSCAN/K-Means.
Incorporates ADR-005 logic (Context Extraction via ADR-006 pre-computed snippets) and Semantic Sliders.
"""

import os
import sys
import time
import json
import numpy as np
import pandas as pd
from typing import List, Dict, Optional
from tqdm import tqdm

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.modules.database import get_datascience_db
from src.services.vllm.client import get_vllm_client

# NOTE: We now use pre-computed ai_context_snippets from the database (ADR-006)
# This improves performance and consistency vs on-the-fly extraction

# ============================================================================
# CONFIGURATION
# ============================================================================

CLUSTERING_METHOD = "cluster_hdbscan"  # or "cluster_kmeans"
MIN_CLUSTER_SIZE_TO_LABEL = 10       # Ignore tiny micro-clusters for now
BATCH_SIZE = 1                       # One cluster at a time mostly due to LLM context

# ============================================================================
# PROMPTS
# ============================================================================

SYSTEM_PROMPT = """You are an expert News Editor and Semantic Cartographer. 
Your task is to analyze a group of news headlines and identify the single cohesive topic that unites them."""

USER_PROMPT_TEMPLATE = """
Here are the representative articles from a news cluster:
{headlines}

The collective "Semantic Profile" (normalized 0-1 scores) of this group is:
{semantics}

Analyze these articles and the semantic profile to provide a structured JSON response with:
1. "label": A short, punchy category name (max 3-4 words).
2. "summary": A concise 2-sentence description of what this cluster represents, capturing the nuance.
3. "coherence": A score from 0.0 to 1.0 indicating how tightly related these articles seem.

JSON Output:
"""

# ============================================================================
# LOGIC
# ============================================================================

def get_cluster_representatives(cluster_id: int, method: str, limit: int = 10) -> tuple[pd.DataFrame, Dict[str, float]]:
    """
    Get representative articles AND the average semantic profile of the cluster.
    Now uses pre-computed ai_context_snippets (ADR-006) instead of raw descriptions.
    """
    with get_datascience_db() as db:
        # Fetch headlines + PRE-COMPUTED context snippets (ADR-006)
        query_arts = f"""
            SELECT t.guid, n.title, n.source, n.ai_context_snippets
            FROM ai_news_topography t
            JOIN ai_news n ON t.guid = n.guid
            WHERE t.{method} = {cluster_id}
            LIMIT {limit * 2} 
        """
        df_arts = db.read_sql(query_arts)
        
        # Fetch Average Semantics for the WHOLE cluster
        # NOTE: We specify the model_name to avoid mixing scores from different models (ADR-010)
        target_model = "mesolitica/Qwen2.5-72B-Instruct-FP8"
        query_sem = f"""
            SELECT 
                AVG(s.s_opp_risk) as "Opp_vs_Risk",
                AVG(s.s_reg) as "Regulation",
                AVG(s.s_econ) as "Economy",
                AVG(s.s_eth_util) as "Ethics",
                AVG(s.s_tech) as "Technical",
                AVG(s.s_geo) as "Geopolitics",
                AVG(s.s_urgency) as "Urgency"
            FROM ai_news_topography t
            JOIN ai_news_semantics s ON t.guid = s.guid
            WHERE t.{method} = {cluster_id}
              AND s.model_name = '{target_model}'
        """
        df_sem = db.read_sql(query_sem)
        
        # Fallback to 7B if 72B coverage is not complete yet
        if df_sem.empty or df_sem.iloc[0].isna().all():
            fallback_model = "Qwen/Qwen2.5-7B-Instruct"
            query_sem_fallback = query_sem.replace(target_model, fallback_model)
            df_sem = db.read_sql(query_sem_fallback)
        
    avg_scores = df_sem.iloc[0].to_dict() if not df_sem.empty else {}
    avg_scores = {k: (v if v is not None else 0.5) for k, v in avg_scores.items()}
    
    return df_arts.head(limit), avg_scores

def generate_label_for_cluster(client, cluster_id: int, articles: pd.DataFrame, avg_scores: Dict[str, float]) -> Optional[Dict]:
    """
    Call vLLM to generate the label using headlines + PRE-COMPUTED snippets + semantics.
    Uses ai_context_snippets from ADR-006 instead of on-the-fly extraction.
    """
    titles = articles['title'].tolist()
    context_snippets = articles['ai_context_snippets'].tolist()
    sources = articles['source'].tolist()
    
    # Format list for prompt: "Title (Source): Context..."
    headlines_text = ""
    for title, snippets_json, src in zip(titles, context_snippets, sources):
        # Parse JSONB snippets
        if isinstance(snippets_json, str):
            snippets = json.loads(snippets_json)
        else:
            snippets = snippets_json if snippets_json else []
        
        # Combine up to 2 snippets per article (to keep context window manageable)
        combined_context = " [...] ".join([s['snippet'] for s in snippets[:2]])
        
        # Clean whitespace
        combined_context = " ".join(combined_context.split())
        
        headlines_text += f"- [{src}] {title}\n  Context: {combined_context}\n\n"
    
    # Format semantics
    semantics_text = "\n".join([f"- {k}: {v:.2f}" for k, v in avg_scores.items()])
    
    prompt = USER_PROMPT_TEMPLATE.format(headlines=headlines_text, semantics=semantics_text)
    
    try:
        response_text = client.chat_completion(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2, 
            max_tokens=256
        )
        
        # Parse JSON
        start_idx = response_text.find('{')
        end_idx = response_text.rfind('}') + 1
        if start_idx == -1 or end_idx == 0:
            return None
            
        json_str = response_text[start_idx:end_idx]
        data = json.loads(json_str)
        return data
        
    except Exception as e:
        print(f"❌ Error generating label for cluster {cluster_id}: {e}")
        return None

def save_cluster_metadata(cluster_id: int, method: str, metadata: Dict, article_count: int):
    """
    Save the generated metadata to the database.
    """
    with get_datascience_db() as db:
        # Create table if not exists
        db.execute("""
            CREATE TABLE IF NOT EXISTS ai_news_clusters_metadata (
                cluster_id INTEGER,
                method TEXT,
                label TEXT,
                summary TEXT,
                coherence FLOAT,
                article_count INTEGER,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (cluster_id, method)
            )
        """)
        
        sql = """
            INSERT INTO ai_news_clusters_metadata (cluster_id, method, label, summary, coherence, article_count)
            VALUES (:cid, :method, :label, :summary, :coh, :ac)
            ON CONFLICT (cluster_id, method) DO UPDATE SET
                label = EXCLUDED.label,
                summary = EXCLUDED.summary,
                coherence = EXCLUDED.coherence,
                article_count = EXCLUDED.article_count,
                updated_at = CURRENT_TIMESTAMP
        """
        
        db.execute(sql, params={
            "cid": cluster_id,
            "method": method,
            "label": metadata.get("label", "Unknown"),
            "summary": metadata.get("summary", ""),
            "coh": metadata.get("coherence", 0.0),
            "ac": article_count
        })

def main():
    print("🎨 Starting Semantic Painter...")
    
    # 1. Connect to vLLM
    try:
        client = get_vllm_client()
        print(f"✅ Connected to vLLM Model: {client.model}")
    except Exception as e:
        print(f"❌ Could not connect to vLLM: {e}")
        return

    # 2. Get list of clusters to paint
    method = CLUSTERING_METHOD
    print(f"🔍 Analyzing clusters from method: {method}")
    
    with get_datascience_db() as db:
        query = f"""
            SELECT {method} as id, COUNT(*) as count
            FROM ai_news_topography
            WHERE {method} != -1
            GROUP BY {method}
            HAVING COUNT(*) >= {MIN_CLUSTER_SIZE_TO_LABEL}
            ORDER BY count DESC
        """
        clusters_df = db.read_sql(query)
    
    print(f"Found {len(clusters_df)} clusters to label.")
    
    # 3. Iterate and Paint
    for _, row in tqdm(clusters_df.iterrows(), total=len(clusters_df)):
        cluster_id = int(row['id'])
        count = int(row['count'])
        
        # Fetch representatives AND semantics
        articles_df, avg_scores = get_cluster_representatives(cluster_id, method, limit=8)
        
        if articles_df.empty:
            continue
            
        # Generate Label
        metadata = generate_label_for_cluster(client, cluster_id, articles_df, avg_scores)
        
        if metadata:
            tqdm.write(f"🎨 Cluster {cluster_id} ({count} arts): {metadata['label']}")
            save_cluster_metadata(cluster_id, method, metadata, count)
        else:
            tqdm.write(f"⚠️ Skipping Cluster {cluster_id} (Generation failed)")
            
        time.sleep(0.5)

    print("🎉 All clusters painted!")

if __name__ == "__main__":
    main()
