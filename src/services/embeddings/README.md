# Embeddings Service Scripts

Management scripts for the **Text Embeddings Inference (TEI)** engine running the **BGE-M3** model.

## Prerequisites

- **curl** installed
- **Embeddings** service deployed in `cognition` namespace
- Access to `https://embeddings.vectorized.pt` (Public)

## Available Scripts

### `embeddings-client.sh`

Interact with the TEI API via shell.

```bash
./embeddings-client.sh <command> [arguments]
```

| Command | Description | Example |
|---------|-------------|---------|
| `health` | Check service health | `./embeddings-client.sh health` |
| `embed <text>` | Generate embeddings for text | `./embeddings-client.sh embed "Hello world"` |
| `info` | Show model information | `./embeddings-client.sh info` |

### `embeddings-status.sh`

Dashboard overview of the embeddings service (service health, pod status, node affinity).

```bash
./embeddings-status.sh
```

### Python Module (`client.py`)

A Python client for programmatic access to the embeddings service.

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
                            │ REST API (JSON)
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  embeddings-client.sh / Python Client                       │
│  curl → https://embeddings.vectorized.pt/v1/*               │
└───────────────────────────┬─────────────────────────────────┘
                            │ Cloudflare Tunnel / Ingress
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  talos-2wq-80j (Worker Node)                                │
│  TEI Pod (BGE-M3) → Optimized Inference Engine               │
└─────────────────────────────────────────────────────────────┘
```

