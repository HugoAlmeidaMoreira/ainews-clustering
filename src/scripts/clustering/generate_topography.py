import sys
import os
import pandas as pd
import numpy as np
import umap
from sklearn.cluster import KMeans, HDBSCAN
from sklearn.preprocessing import StandardScaler
import time

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.modules.database import get_datascience_db

def load_data():
    print("🐘 Fetching embeddings and semantic scores from Postgres...")
    with get_datascience_db() as db:
        # Join news with their semantics (using Qwen model scores as default)
        query = """
            SELECT 
                n.guid, 
                n.embedding_qwen_8b,
                s.s_opp_risk, s.s_reg, s.s_econ, s.s_eth_util, s.s_tech, s.s_geo, s.s_urgency
            FROM ai_news n
            JOIN ai_news_semantics s ON n.guid = s.guid
            WHERE n.embedding_qwen_8b IS NOT NULL
              AND s.model_name = 'Qwen/Qwen2.5-7B-Instruct'
        """
        df = db.read_sql(query)
    
    print(f"✅ Loaded {len(df)} articles.")
    return df

import gc
from sklearn.decomposition import PCA

def process_topography(df):
    # 1. Prepare Embeddings in float32 (50% less memory)
    print("🧪 Preparing 4096D embeddings (float32)...")
    embeddings = np.stack(df['embedding_qwen_8b'].values).astype(np.float32)
    
    # Free memory from the original dataframe column
    del df['embedding_qwen_8b']
    gc.collect()
    
    # 2. Scaling
    print("⚖️ Scaling data...")
    scaler = StandardScaler()
    embeddings_scaled = scaler.fit_transform(embeddings)
    del embeddings
    gc.collect()

    # 3. PCA Pre-reduction (4096D -> 100D)
    print("📉 Running PCA Pre-reduction (4096D -> 100D)...")
    pca = PCA(n_components=100, random_state=42)
    embeddings_100d = pca.fit_transform(embeddings_scaled)
    del embeddings_scaled
    gc.collect()
    print(f"   Explained variance ratio (total): {np.sum(pca.explained_variance_ratio_):.4f}")
    
    # 4. UMAP Reduction
    print("📉 Running UMAP (100D -> 5D for clustering)...")
    reducer_5d = umap.UMAP(
        n_neighbors=15,
        min_dist=0.1,
        n_components=5,
        metric='cosine',
        random_state=42,
        low_memory=True
    )
    embeddings_5d = reducer_5d.fit_transform(embeddings_100d)
    
    print("📉 Running UMAP (100D -> 2D for visualization)...")
    reducer_2d = umap.UMAP(
        n_neighbors=15,
        min_dist=0.1,
        n_components=2,
        metric='cosine',
        random_state=42,
        low_memory=True
    )
    embeddings_2d = reducer_2d.fit_transform(embeddings_100d)
    del embeddings_100d
    gc.collect()
    
    # 3. K-Means Clustering (Strategy A)
    # Using K=15 as a reasonable starting point for news categories
    K = 15
    print(f"🤖 Clustering with K-Means (K={K})...")
    kmeans = KMeans(n_clusters=K, random_state=42, n_init=10)
    df['cluster_kmeans'] = kmeans.fit_predict(embeddings_5d)
    
    # 4. HDBSCAN Clustering (Strategy B)
    print("🤖 Clustering with HDBSCAN (Density-based)...")
    hdb = HDBSCAN(min_cluster_size=50, min_samples=10, cluster_selection_method='eom')
    df['cluster_hdbscan'] = hdb.fit_predict(embeddings_5d)
    
    # Store coordinates
    df['umap_x'] = embeddings_2d[:, 0]
    df['umap_y'] = embeddings_2d[:, 1]
    
    return df

def save_results(df):
    print("💾 Saving topography to database...")
    with get_datascience_db() as db:
        # Create table for topography
        db.execute("""
            CREATE TABLE IF NOT EXISTS ai_news_topography (
                guid TEXT PRIMARY KEY,
                umap_x FLOAT,
                umap_y FLOAT,
                cluster_kmeans INTEGER,
                cluster_hdbscan INTEGER,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Insert/Update results
        for _, row in df.iterrows():
            db.execute("""
                INSERT INTO ai_news_topography (guid, umap_x, umap_y, cluster_kmeans, cluster_hdbscan)
                VALUES (:guid, :umap_x, :umap_y, :cluster_kmeans, :cluster_hdbscan)
                ON CONFLICT (guid) DO UPDATE SET
                    umap_x = EXCLUDED.umap_x,
                    umap_y = EXCLUDED.umap_y,
                    cluster_kmeans = EXCLUDED.cluster_kmeans,
                    cluster_hdbscan = EXCLUDED.cluster_hdbscan,
                    updated_at = CURRENT_TIMESTAMP
            """, params={
                'guid': row['guid'],
                'umap_x': row['umap_x'],
                'umap_y': row['umap_y'],
                'cluster_kmeans': int(row['cluster_kmeans']),
                'cluster_hdbscan': int(row['cluster_hdbscan'])
            })
    
    print("🎉 Topography saved successfully!")

def main():
    start_time = time.time()
    
    df = load_data()
    if df.empty:
        print("❌ No data to process. Make sure embeddings and semantics are generated.")
        return
        
    df = process_topography(df)
    save_results(df)
    
    end_time = time.time()
    print(f"⏱️ Total time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
