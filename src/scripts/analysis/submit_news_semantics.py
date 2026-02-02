"""
News Semantics Job Submitter (ADR-041)

Submits pending news articles to the Job Gateway for semantic analysis
using the standard JobGateway client.

Usage:
    uv run python -m src.scripts.analysis.submit_news_semantics
"""

import sys
import os
import json
from tqdm import tqdm

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.services.jobs.analytics_client import JobGateway
from src.modules.database import get_datascience_db

# Configuration
MODEL_NAME = "mesolitica/Qwen2.5-72B-Instruct-FP8"
QUEUE_NAME = "semantics"

# State checking
STATE_FILE = f".submitted_jobs_{QUEUE_NAME}.json"

def load_submitted_guids():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r') as f:
                return set(json.load(f))
        except:
            return set()
    return set()

def save_submitted_guids(guids):
    with open(STATE_FILE, 'w') as f:
        json.dump(list(guids), f)

def main():
    print("🚀 News Semantics Job Submitter")
    
    # Initialize Gateway Client
    try:
        gateway = JobGateway()
        if not gateway.check_health():
            print("❌ Gateway is not healthy. Aborting.")
            return
    except Exception as e:
        print(f"❌ Failed to initialize gateway: {e}")
        return

    # Load local state
    submitted_guids = load_submitted_guids()
    print(f"📂 Loaded {len(submitted_guids)} previously submitted articles from local state.")

    # Fetch pending articles
    print("🐘 Fetching pending articles from database...")
    with get_datascience_db() as db:
        df = db.read_sql(f"""
            SELECT guid, title, description 
            FROM ai_news 
            WHERE guid NOT IN (SELECT guid FROM ai_news_semantics WHERE model_name = '{MODEL_NAME}')
            ORDER BY pubdate DESC
        """)
    
    # Filter out locally submitted ones
    original_count = len(df)
    df = df[~df['guid'].isin(submitted_guids)]
    filtered_count = len(df)
    
    if original_count != filtered_count:
        print(f"ℹ️  Skipped {original_count - filtered_count} articles already in local submitted state.")

    if df.empty:
        print(f"✅ All news already scored (or submitted) for {MODEL_NAME}.")
        return

    print(f"📦 Found {len(df)} new articles to process.")
    
    # Check queue status
    try:
        current_len = gateway.get_queue_length(QUEUE_NAME)
        print(f"📊 Current queue '{QUEUE_NAME}': {current_len} pending jobs")
    except Exception:
        print(f"⚠️ Could not fetch queue length, proceeding anyway...")

    # Submit jobs
    print(f"\n📤 Submitting jobs to queue '{QUEUE_NAME}'...")
    
    new_submissions = 0
    failed = 0
    batch_guids = []
    
    try:
        for _, row in tqdm(df.iterrows(), total=len(df), desc="Submitting"):
            try:
                gateway.submit_job(
                    queue=QUEUE_NAME,
                    job_type="semantic_analysis",
                    payload={
                        "guid": row['guid'],
                        "texts": [f"{row['title']}\n{row['description']}"],
                        "model_name": MODEL_NAME,
                        "original_title": row['title'],
                        "original_description": row['description']
                    }
                )
                new_submissions += 1
                submitted_guids.add(row['guid'])
                batch_guids.append(row['guid'])
                
                # Save state every 100 items to avoid data loss on crash
                if len(batch_guids) >= 100:
                    save_submitted_guids(submitted_guids)
                    batch_guids = []
                    
            except Exception as e:
                failed += 1
    finally:
        # Always save state on exit/interrupt
        save_submitted_guids(submitted_guids)
        print(f"\n💾 State saved ({len(submitted_guids)} total items).")

    # Summary
    print()
    print("=" * 50)
    print("📋 Summary")
    print("=" * 50)
    print(f"   ✅ Submitted: {new_submissions}")
    print(f"   ❌ Failed:    {failed}")
    
    try:
        new_len = gateway.get_queue_length(QUEUE_NAME)
        print(f"   📊 Queue now has {new_len} jobs")
    except:
        pass

    print()
    print("🎉 Done! Jobs queued. Monitor at: https://jobs.vectorized.pt/queue/semantics")

if __name__ == "__main__":
    main()
