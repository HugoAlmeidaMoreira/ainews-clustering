# vLLM Service Scripts

Management scripts for the **vLLM** High-Performance Inference Engine via OpenAI-compatible API.

## Prerequisites

- **Doppler CLI** installed and authenticated
- Doppler Project: `talos-cluster`, Config: `prd`
- **vLLM** deployed in `cognition` namespace

## Available Scripts

### `vllm-client.sh`

Interact with the vLLM OpenAI-compatible API.

```bash
./vllm-client.sh <command> [arguments]
```

| Command | Description | Example |
|---------|-------------|---------|
| `models` | List loaded models | `./vllm-client.sh models` |
| `health` | Check service health | `./vllm-client.sh health` |
| `chat <msg>` | Send a chat message | `./vllm-client.sh chat "Hello world"` |

### `vllm-status.sh`

Dashboard overview of the vLLM service (service health, loaded model, pod status, GPU stats).

```bash
./vllm-status.sh
```

### Python Module (`client.py`)

A Python client for programmatic access to vLLM.

```python
from services.vllm import get_vllm_client

client = get_vllm_client()
joke = client.get_joke("programming")
print(joke)
```

## Shell Aliases (Quick Access)

Add these to your `~/.bashrc`:

```bash
alias vllm-status='/home/hugo/git/personal/control-plane-talos/services/vllm/vllm-status.sh'
alias vllm-chat='/home/hugo/git/personal/control-plane-talos/services/vllm/vllm-client.sh chat'
alias vllm-models='/home/hugo/git/personal/control-plane-talos/services/vllm/vllm-client.sh models'
```

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  Doppler (talos-cluster/prd)                                │
│  VLLM_USER, VLLM_PASSWORD                                   │
└───────────────────────────┬─────────────────────────────────┘
                            │ doppler run
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  vllm-client.sh                                             │
│  curl → https://vllm.vectorized.pt/v1/*                     │
└───────────────────────────┬─────────────────────────────────┘
                            │ Cloudflare Tunnel + Basic Auth
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  HW-BRAIN-01 (GB10 Blackwell)                               │
│  vLLM Pod → GPU Unified Memory                              │
└─────────────────────────────────────────────────────────────┘
```
