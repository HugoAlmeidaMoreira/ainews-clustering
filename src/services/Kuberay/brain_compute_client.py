#!/usr/bin/env python3
"""
Brain Node Compute Client (ADR-040)
=====================================

Example client showing how Data Scientists can offload heavy compute
to the Brain Node (HW-BRAIN-01) using Ray.

Usage:
    # From your local machine or analytics repo:
    python brain_compute_client.py

Requirements:
    pip install ray[client]

Connection:
    The Ray Client connects to the cluster head via port 10001.
    Ensure you have network access (VPN/port-forward if needed).
"""

import ray
import numpy as np
from typing import List, Dict, Any
import time


# ============================================================================
# CONFIGURATION
# ============================================================================

# Direct connection (if internal network access)
RAY_HEAD_ADDRESS = "ray://ray-client.cognition.svc.cluster.local:10001"

# Alternative: Port-forward for local development
# kubectl port-forward -n cognition svc/ray-client 10001:10001
RAY_LOCAL_ADDRESS = "ray://localhost:10001"


# ============================================================================
# REMOTE FUNCTIONS (Executed on Brain Node)
# ============================================================================

@ray.remote
def heavy_embedding_task(texts: List[str]) -> np.ndarray:
    """
    Example: Generate embeddings on the Brain Node.
    This runs on the Blackwell GPU, not your local machine.
    """
    import os
    # Force use of writable temp directory to avoid /mnt/models permission errors
    os.environ["HF_HOME"] = "/tmp/huggingface_cache"
    
    from sentence_transformers import SentenceTransformer
    
    # Model is loaded from the shared /mnt/models cache
    model = SentenceTransformer("BAAI/bge-m3")
    embeddings = model.encode(texts, normalize_embeddings=True)
    
    return embeddings


@ray.remote(num_gpus=1)
def gpu_intensive_umap(embeddings: np.ndarray, n_components: int = 2) -> np.ndarray:
    """
    Example: Run UMAP dimensionality reduction on GPU.
    The @ray.remote(num_gpus=1) decorator reserves GPU resources.
    """
    import cuml  # GPU-accelerated ML library
    from cuml.manifold import UMAP
    
    reducer = UMAP(n_components=n_components, n_neighbors=15, min_dist=0.1)
    reduced = reducer.fit_transform(embeddings)
    
    return reduced


@ray.remote
def cpu_parallel_task(data_chunk: np.ndarray) -> Dict[str, Any]:
    """
    Example: CPU-bound parallel processing across Ray workers.
    """
    return {
        "mean": float(np.mean(data_chunk)),
        "std": float(np.std(data_chunk)),
        "shape": data_chunk.shape,
    }


# ============================================================================
# CLIENT USAGE PATTERNS
# ============================================================================

def example_1_simple_offload():
    """Pattern 1: Simple function offload."""
    
    texts = [
        "Quantum computing advances",
        "Machine learning breakthroughs",
        "Sustainable energy solutions",
    ]
    
    # This runs on the Brain Node, not locally
    future = heavy_embedding_task.remote(texts)
    embeddings = ray.get(future)
    
    print(f"Got embeddings shape: {embeddings.shape}")
    return embeddings


def example_2_parallel_processing():
    """Pattern 2: Parallel processing with multiple workers."""
    
    # Create 10 chunks of data
    chunks = [np.random.randn(1000, 100) for _ in range(10)]
    
    # Submit all tasks in parallel
    futures = [cpu_parallel_task.remote(chunk) for chunk in chunks]
    
    # Collect results
    results = ray.get(futures)
    
    print(f"Processed {len(results)} chunks in parallel")
    return results


def example_3_gpu_pipeline():
    """Pattern 3: GPU pipeline (embeddings → UMAP)."""
    
    texts = [f"Document {i}" for i in range(1000)]
    
    # Step 1: Generate embeddings on GPU
    embeddings_future = heavy_embedding_task.remote(texts)
    
    # Step 2: Run UMAP (waits for embeddings automatically)
    # Using ray.get() inside the pipeline passes data efficiently
    embeddings = ray.get(embeddings_future)
    reduced_future = gpu_intensive_umap.remote(embeddings, n_components=2)
    
    reduced = ray.get(reduced_future)
    print(f"Reduced {len(texts)} documents to shape: {reduced.shape}")
    return reduced


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("🧠 Connecting to Brain Node Ray Cluster...")
    
    # Initialize Ray Client (connects to remote cluster)
    # Use runtime_env to install additional packages on workers
    ray.init(
        RAY_LOCAL_ADDRESS,  # Change to RAY_HEAD_ADDRESS for direct connection
        runtime_env={
            "pip": ["sentence-transformers", "numpy"],
            # "env_vars": {"HF_HOME": "/mnt/models/huggingface"}, # Commented out to fix permissions
        },
    )
    
    print(f"✅ Connected to cluster with {ray.cluster_resources()}")
    
    # Run examples
    print("\n--- Example 1: Simple Offload ---")
    start = time.time()
    example_1_simple_offload()
    print(f"⏱️ Time: {time.time() - start:.2f}s")
    
    print("\n--- Example 2: Parallel Processing ---")
    start = time.time()
    example_2_parallel_processing()
    print(f"⏱️ Time: {time.time() - start:.2f}s")
    
    # Note: Example 3 requires cuML which may not be pre-installed
    # print("\n--- Example 3: GPU Pipeline ---")
    # example_3_gpu_pipeline()
    
    ray.shutdown()
    print("\n🔌 Disconnected from cluster.")
