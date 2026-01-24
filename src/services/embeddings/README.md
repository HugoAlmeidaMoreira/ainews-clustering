# Embeddings Service Scripts

Management scripts for the **Text Embeddings Inference (TEI)** service running the **BGE-M3** model.

## Prerequisites

- **curl** installed
- **Embeddings** service deployed in `cognition` namespace
- Access to `https://embeddings.vectorized.pt` (Public) or internal cluster access.

## Available Scripts

### `embeddings-client.sh`

Interact with the TEI API.

```bash
./embeddings-client.sh <command> [arguments]
```

| Command | Description | Example |
|---------|-------------|---------|
| `health` | Check service health | `./embeddings-client.sh health` |
| `embed <msg>` | Generate embeddings for text | `./embeddings-client.sh embed "Hello world"` |
| `info` | Show model information | `./embeddings-client.sh info` |

### `embeddings-status.sh`

Overview of the embeddings service status (service health, pod status, node affinity).

```bash
./embeddings-status.sh
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
                            │ curl
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  embeddings-client.sh                                       │
│  curl → https://embeddings.vectorized.pt/v1/*               │
└───────────────────────────┬─────────────────────────────────┘
                            │ Cloudflare Tunnel / Ingress
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  talos-2wq-80j (Worker - x86_64)                            │
│  TEI Pod (cpu-1.2) → BGE-M3                                 │
└─────────────────────────────────────────────────────────────┘
```
