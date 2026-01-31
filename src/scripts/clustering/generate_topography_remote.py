#!/usr/bin/env python3
import ray
import numpy as np
import os
import psycopg2
from psycopg2.extras import execute_values
import time
import sys

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from src.modules.database import get_datascience_db

# ============================================================================
# CONFIGURATION
# ============================================================================

RAY_HEAD_ADDRESS = "ray://localhost:10001"

# ============================================================================
# LOCAL FUNCTIONS (IO / Orchestration)
# ============================================================================

def fetch_data_local():
    print("🐘 [Local] Fetching embeddings from Postgres...")
    start = time.time()
    
    with get_datascience_db() as db:
        # Use simple raw SQL for speed
        query = """
            SELECT n.guid, n.embedding_qwen_8b
            FROM ai_news n
            WHERE n.embedding_qwen_8b IS NOT NULL
        """
        # Using pandas read_sql might be cleaner but let's stick to raw for consistency
        # Assuming db.read_sql is available or use cursor
        # Let's use the raw connection from the engine/conn usually provided by get_datascience_db wrapper
        # If it returns a connection object:
        df = db.read_sql(query)
        
    print(f"✅ [Local] Loaded {len(df)} rows in {time.time() - start:.2f}s")
    
    # Convert to ready-to-ship numpy arrays
    guids = df['guid'].tolist()
    
    # Check if embeddings are strings or lists (pgvector usually returns string if not parsed)
    # But since we use sqlalchemy/pandas possibly handled. 
    # Let's assume it needs parsing if it's string.
    sample = df['embedding_qwen_8b'].iloc[0]
    if isinstance(sample, str):
        # Fallback parsing
        import json
        embeddings = np.array([json.loads(x) if '[' in x else np.fromstring(x.strip('[]'), sep=',') for x in df['embedding_qwen_8b'].values], dtype=np.float32)
    else:
        # Already list/array
        embeddings = np.stack(df['embedding_qwen_8b'].values).astype(np.float32)
        
    return guids, embeddings

def save_results_local(guids, umap_2d, labels_hdbscan, labels_kmeans):
    print(f"💾 [Local] Saving topography results for {len(guids)} items...")
    
    data = []
    for i, guid in enumerate(guids):
        data.append((
            guid,
            float(umap_2d[i][0]),
            float(umap_2d[i][1]),
            int(labels_hdbscan[i]),
            int(labels_kmeans[i])
        ))
    
    with get_datascience_db() as db:
         # 1. Create table
        db.execute("""
            CREATE TABLE IF NOT EXISTS ai_news_topography (
                guid TEXT PRIMARY KEY,
                umap_x FLOAT,
                umap_y FLOAT,
                cluster_hdbscan INTEGER,
                cluster_kmeans INTEGER,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # 2. Bulk Upsert
        # We need raw cursor for execute_values efficiency
        # Assuming db exposes an engine or connection
        with db.engine.connect() as conn:
             # Using sqlalchemy text or raw cursor
             # Simplified: Let's use pandas to_sql or raw iter execution if simple.
             # Ideally execute_values is best.
             pass 
             # Re-implementing raw psycopg2 for maximum compatibility with previous logic
        
    # Re-connect purely for the bulk insert to avoid ORM overhead
    # (Creating a fresh connection using helper)
    from src.modules.database import get_database_url
    conn = psycopg2.connect(get_database_url(database="datascience"))
    cur = conn.cursor()
    
    sql = """
        INSERT INTO ai_news_topography (guid, umap_x, umap_y, cluster_hdbscan, cluster_kmeans)
        VALUES %s
        ON CONFLICT (guid) DO UPDATE SET
            umap_x = EXCLUDED.umap_x,
            umap_y = EXCLUDED.umap_y,
            cluster_hdbscan = EXCLUDED.cluster_hdbscan,
            cluster_kmeans = EXCLUDED.cluster_kmeans,
            updated_at = CURRENT_TIMESTAMP
    """
    execute_values(cur, sql, data)
    conn.commit()
    conn.close()
    
    print("🎉 [Local] Saved successfully!")

# ============================================================================
# REMOTE FUNCTIONS (Compute Only)
# ============================================================================

@ray.remote
def run_umap_compute(embeddings, n_components=5):
    """
    Run UMAP dimensionality reduction on the server.
    """
    print(f"� [Remote] Running UMAP (N={n_components})...")
    import umap
    
    # n_jobs=-1 uses all available cores on the Ray Worker
    reducer = umap.UMAP(
        n_neighbors=15,
        n_components=n_components,
        min_dist=0.1,
        metric='cosine',
        random_state=42,
        low_memory=False, # We have RAM!
        n_jobs=-1 
    )
    result = reducer.fit_transform(embeddings)
    return result

@ray.remote
def run_hdbscan_compute(embeddings_5d):
    print("🤖 [Remote] Running HDBSCAN...")
    from sklearn.cluster import HDBSCAN
    
    # cluster_selection_method='eom' usually yields more granular clusters suitable for news
    clusterer = HDBSCAN(min_cluster_size=30, min_samples=10, cluster_selection_method='eom')
    labels = clusterer.fit_predict(embeddings_5d)
    return labels

@ray.remote
def run_kmeans_compute(embeddings_5d, k=15):
    print(f"🤖 [Remote] Running K-Means (K={k})...")
    from sklearn.cluster import KMeans
    
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(embeddings_5d)
    return labels

# ============================================================================
# MAIN
# ============================================================================

def main():
    # 1. Local IO
    guids, embeddings = fetch_data_local()
    
    # 2. Upload to Cluster
    print(f"🚀 Uploading {embeddings.nbytes / 1024 / 1024:.2f} MB to Brain Node...")
    ray.init(
        RAY_HEAD_ADDRESS, 
        runtime_env={"pip": ["umap-learn", "scikit-learn", "numpy"]}
    )
    
    # Put input data in Object Store once
    embeddings_ref = ray.put(embeddings)
    
    # 3. Remote Compute
    print("📡 Submit UMAP 5D...")
    vectors_5d_ref = run_umap_compute.remote(embeddings_ref, n_components=5)
    
    print("📡 Submit UMAP 2D...")
    vectors_2d_ref = run_umap_compute.remote(embeddings_ref, n_components=2)
    
    print("📡 Submit Clustering...")
    hdbscan_ref = run_hdbscan_compute.remote(vectors_5d_ref)
    kmeans_ref = run_kmeans_compute.remote(vectors_5d_ref, k=15)
    
    # 4. Gather Results
    print("⏳ Waiting for results...")
    vectors_2d = ray.get(vectors_2d_ref)
    labels_hdbscan = ray.get(hdbscan_ref)
    labels_kmeans = ray.get(kmeans_ref)
    
    print(f"✅ Computation Complete! Saving...")
    
    # 5. Local Save
    save_results_local(guids, vectors_2d, labels_hdbscan, labels_kmeans)
    
    ray.shutdown()

if __name__ == "__main__":
    main()
