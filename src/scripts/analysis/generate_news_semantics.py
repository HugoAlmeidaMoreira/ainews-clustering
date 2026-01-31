import sys
import os
import asyncio
import pandas as pd
import math
from tqdm.asyncio import tqdm
from typing import List, Dict, Any, Optional

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.services.vllm.client import get_vllm_client
from src.modules.database import get_datascience_db

# Configuration
BATCH_SIZE = 32  # Concurrent requests to vLLM
MAX_CHARS_CONTENT = 10000 # Limit text to focus on the meat of the news
MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"

# Semantic Axes Definitions (Mapped to Sliders)
AXES = [
    {"id": "s_opp_risk", "name": "Opportunity vs. Risk", "desc": "1: Pure Hype/Gain, 9: Pure Fear/Danger"},
    {"id": "s_reg", "name": "Regulatory Pressure", "desc": "1: Deregulation, 9: High Compliance/Control"},
    {"id": "s_econ", "name": "Economic Momentum", "desc": "1: Niche/Non-profit, 9: High Investment/Commercial"},
    {"id": "s_eth_util", "name": "Ethics vs. Utility", "desc": "1: Human Rights focused, 9: Performance/Efficiency focused"},
    {"id": "s_tech", "name": "Technical Depth", "desc": "1: Generalist/Pop, 9: Specialized/Scientific"},
    {"id": "s_geo", "name": "Geopolitical Scope", "desc": "1: Local/PT/EU, 9: Global/US/China"},
    {"id": "s_urgency", "name": "Urgency / Sentiment", "desc": "1: Educational/Long-form, 9: Alarmist/Breaking News"}
]

def parse_probabilistic_score(token_logprobs) -> Optional[float]:
    """Extracts the 0.0-1.0 score from the logprobs of a single token position."""
    token_probs = {}
    total_prob = 0.0
    
    for item in token_logprobs.top_logprobs:
        token = item.token.strip()
        if token.isdigit() and token in "123456789":
            prob = math.exp(item.logprob)
            val = int(token)
            token_probs[val] = prob
            total_prob += prob

    if total_prob == 0:
        return None

    weighted_sum = sum(v * (p/total_prob) for v, p in token_probs.items())
    return (weighted_sum - 1) / 8

async def score_article(client, row):
    title = row.get('title', '')
    desc = (row.get('description') or '')[:MAX_CHARS_CONTENT]
    
    # Prompting for all 7 dimensions in one shot
    axes_str = "\n".join([f"- {a['name']}: {a['desc']}" for a in AXES])
    
    prompt = f"""Task: Analyze the AI news article provided and score it on 7 semantic axes.
For each axis, provide a single digit from 1 to 9.

Axes Definitions:
{axes_str}

Format: Return ONLY the 7 digits separated by spaces.
Example: 3 1 5 2 1 4 2

Article Title: {title}
Content: {desc}

Scores:"""

    try:
        # We need the underlying OpenAI client for advanced logprobs support
        response = await asyncio.to_thread(
            client.client.chat.completions.create,
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a precise linguistic data extractor. You respond only with 7 digits separated by spaces."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=15, # 7 digits + spaces is around 13-14 tokens
            temperature=0,
            logprobs=True,
            top_logprobs=10
        )

        logprobs_content = response.choices[0].logprobs.content
        scores = {}
        
        # We look for the tokens that represent our numbers
        # The model usually outputs: "Digit Space Digit Space..."
        found_axes = 0
        for token_data in logprobs_content:
            token = token_data.token.strip()
            if token.isdigit() and token in "123456789":
                score = parse_probabilistic_score(token_data)
                if score is not None:
                    axis_id = AXES[found_axes]['id']
                    scores[axis_id] = score
                    found_axes += 1
                
                if found_axes >= len(AXES):
                    break
        
        if len(scores) < len(AXES):
            return None
            
        scores['guid'] = row['guid']
        scores['model_name'] = MODEL_NAME
        return scores

    except Exception as e:
        # print(f"Error scoring {row['guid']}: {e}")
        return None

async def main():
    print(f"🐘 Connecting to database...")
    with get_datascience_db() as db:
        # 1. Prepare Schema - Composite PK for A/B testing
        db.execute("""
            CREATE TABLE IF NOT EXISTS ai_news_semantics (
                guid TEXT,
                model_name TEXT,
                s_opp_risk FLOAT,
                s_reg FLOAT,
                s_econ FLOAT,
                s_eth_util FLOAT,
                s_tech FLOAT,
                s_geo FLOAT,
                s_urgency FLOAT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (guid, model_name)
            )
        """)
        
        # 2. Fetch news that haven't been scored by this model yet
        df = db.read_sql(f"""
            SELECT guid, title, description 
            FROM ai_news 
            WHERE guid NOT IN (SELECT guid FROM ai_news_semantics WHERE model_name = '{MODEL_NAME}')
        """)
        
        if df.empty:
            print(f"✅ All news already scored by {MODEL_NAME}.")
            return

        print(f"📦 Found {len(df)} news to process.")
        
    client = get_vllm_client()
    results = []
    
    # 3. Process in Async batches
    for i in tqdm(range(0, len(df), BATCH_SIZE), desc="Analyzing Semantics"):
        batch = df.iloc[i:i+BATCH_SIZE]
        tasks = [score_article(client, row) for _, row in batch.iterrows()]
        
        batch_results = await asyncio.gather(*tasks)
        valid_results = [r for r in batch_results if r is not None]
        
        # 4. Save batch to database
        if valid_results:
            with get_datascience_db() as db:
                for res in valid_results:
                    db.execute("""
                        INSERT INTO ai_news_semantics 
                        (guid, model_name, s_opp_risk, s_reg, s_econ, s_eth_util, s_tech, s_geo, s_urgency)
                        VALUES (:guid, :model_name, :s_opp_risk, :s_reg, :s_econ, :s_eth_util, :s_tech, :s_geo, :s_urgency)
                        ON CONFLICT (guid, model_name) DO UPDATE SET
                            s_opp_risk = EXCLUDED.s_opp_risk,
                            s_reg = EXCLUDED.s_reg,
                            s_econ = EXCLUDED.s_econ,
                            s_eth_util = EXCLUDED.s_eth_util,
                            s_tech = EXCLUDED.s_tech,
                            s_geo = EXCLUDED.s_geo,
                            s_urgency = EXCLUDED.s_urgency,
                            updated_at = CURRENT_TIMESTAMP
                    """, params=res)
        
    print(f"🎉 Semantic Analysis Complete for {MODEL_NAME}!")

if __name__ == "__main__":
    asyncio.run(main())
