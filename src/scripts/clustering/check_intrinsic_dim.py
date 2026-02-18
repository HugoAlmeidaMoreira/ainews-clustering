#!/usr/bin/env python3
import sys
import os
import numpy as np
import json
import time

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.modules.database import get_datascience_db
from skdim.id import MLE, TwoNN, CorrInt

def load_embeddings():
    print("🐘 Fetching embeddings from Postgres...")
    start_time = time.time()
    
    with get_datascience_db() as db:
        query = """
            SELECT embedding_qwen_8b
            FROM ai_news
            WHERE embedding_qwen_8b IS NOT NULL
            LIMIT 2000 -- Reduce for debugging speed
        """
        import pandas as pd
        df = db.read_sql(query)
        
    print(f"✅ Loaded {len(df)} embeddings in {time.time() - start_time:.2f}s")
    
    if len(df) == 0:
        return np.array([])

    # Process embeddings
    sample = df['embedding_qwen_8b'].iloc[0]
    if isinstance(sample, str):
        print("Parsing string embeddings...")
        try:
            # Safer parsing: json loads is robust for standard JSON arrays
            embeddings = np.array([json.loads(x) for x in df['embedding_qwen_8b'].values], dtype=np.float32)
        except Exception:
            # Fallback to string split if json fails (e.g. Postgres array format '{1,2,3}')
            print("Trying fallback parsing for potentially non-JSON strings...")
            embeddings = np.array([np.fromstring(x.replace('{','').replace('}',''), sep=',') for x in df['embedding_qwen_8b'].values], dtype=np.float32)
    else:
        print("Converting list/array objects...")
        embeddings = np.stack(df['embedding_qwen_8b'].values).astype(np.float32)
        
    return embeddings

def main():
    embeddings = load_embeddings()
    if embeddings.size == 0:
        print("No data!")
        return

    print(f"Start Estimations on shape {embeddings.shape}...")
    
    # Check for duplicates or zero variance
    unique_rows = np.unique(embeddings, axis=0)
    print(f"Unique rows: {len(unique_rows)} / {len(embeddings)}")
    
    if len(unique_rows) < len(embeddings) * 0.1:
        print("WARNING: Too many duplicates. Intrinsic dimension will be biased towards 0.")
        
    # Sample view
    print(f"Sample[0, :5]: {embeddings[0, :5]}")
    
    print("Running MLE...")
    mle = MLE()
    id_mle = mle.fit_transform(embeddings)
    print(f"🔮 Intrinsic Dimension (MLE): {id_mle}")

    print("Running TwoNN...")
    twonn = TwoNN()
    id_twonn = twonn.fit_transform(embeddings)
    print(f"🔮 Intrinsic Dimension (TwoNN): {id_twonn}")
    
    # CorrInt can be slow, skipping for now unless needed

if __name__ == "__main__":
    main()
