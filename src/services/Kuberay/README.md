# Brain Compute Client (Ray)

This directory contains the client-side code for offloading heavy compute tasks to the **Brain Node (HW-BRAIN-01)** using the Ray distributed runtime.

## Overview
Instead of running heavy data science workloads (like UMAP, HDBSCAN, or bulk embeddings) on your local machine (Control Plane), we use Ray to transparently execute these functions on the cluster's high-performance hardware (NVIDIA Blackwell + 128GB RAM).

## Prerequisites
1.  **Python Environment**: Ensure you have Python 3.10+ installed.
2.  **Dependencies**: Install the Ray client and standard libraries.
    ```bash
    pip install "ray[client]" numpy sentence-transformers
    ```
3.  **Network Access**: You must be able to reach the Ray Head service.
    *   **Internal**: Use `ray://ray-client.cognition.svc.cluster.local:10001`
    *   **Local Dev**: Use `kubectl port-forward` to tunnel port 10001.

## Usage

### 1. Establish Connection
First, open a tunnel to the cluster if you are working locally:
```bash
kubectl port-forward -n cognition svc/ray-cluster-kuberay-head-svc 10001:10001
```

### 2. Run the Client
Execute the example script to verify connectivity and run a test payload:
```bash
python src/services/Kuberay/brain_compute_client.py
```

## Code Pattern
To offload a function, simply decorate it with `@ray.remote`:

```python
import ray

# Connect to the Brain Node
ray.init("ray://localhost:10001")

@ray.remote
def heavy_task(data):
    # This runs on the 128GB RAM server!
    return complex_processing(data)

# Trigger remote execution
future = heavy_task.remote(my_data)
result = ray.get(future)
```

## References
*   [ADR-040: Brain Node Distributed Compute](../dev/ADR/cluster-adrs/adr-040-brain-node-distributed-compute.md)
*   [Ray Client Documentation](https://docs.ray.io/en/latest/cluster/running-applications/job-submission/ray-client.html)
