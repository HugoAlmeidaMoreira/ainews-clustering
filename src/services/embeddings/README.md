# Embeddings Service Scripts

Management scripts for the **Embeddings** service running on **vLLM** with the **BGE-M3** model (OpenAI-compatible API).

## Prerequisites

- **curl** installed
- **Embeddings** service deployed in `cognition` namespace
- Access to `https://embeddings.vectorized.pt` (Public)

## Available Scripts

### `embeddings-client.sh`

Interact with the vLLM API via shell.

```bash
./embeddings-client.sh <command> [arguments]
```

| Command | Description | Example |
|---------|-------------|---------|
| `info` | Check service health and models | `./embeddings-client.sh info` |
| `embed <text>` | Generate embeddings for text | `./embeddings-client.sh embed "Hello world"` |

### `embeddings-status.sh`

Dashboard overview of the embeddings service (service health, pod status, node affinity).

```bash
./embeddings-status.sh
```

### Python Module (`client.py`)

A Python client for programmatic access to the embeddings service (wrapper around OpenAI-compatible API).

```python
from services.embeddings import get_embeddings_client

client = get_embeddings_client()
vector = client.generate("O futuro da infraestrutura é agentic.")
print(f"Generated vector length: {len(vector)}")
```

## Shell Aliases (Quick Access)

Add these to your `~/.zshrc` or `~/.bashrc`:

```bash
alias emb-status='/home/hugo/git/personal/control-plane-talos/services/embeddings/embeddings-status.sh'
alias emb-gen='/home/hugo/git/personal/control-plane-talos/services/embeddings/embeddings-client.sh embed'
```

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  Client (Local/CI/Cluster)                                   │
└───────────────────────────┬─────────────────────────────────┘
                            │ REST API (OpenAI Compatible)
                            │ POST /v1/embeddings
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  embeddings-client.sh / Python Client                       │
│  curl → https://embeddings.vectorized.pt/v1/*               │
└───────────────────────────┬─────────────────────────────────┘
                            │ Cloudflare Tunnel / Ingress
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  talos-node (GPU Worker)                                    │
│  vLLM Pod (BGE-M3) → Optimized Inference Engine on Blackwell │
└─────────────────────────────────────────────────────────────┘
```

