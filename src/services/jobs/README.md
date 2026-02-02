# Job Queue System (ADR-041)

> **Status**: 🟢 **LIVE** at `https://jobs.vectorized.pt`

This directory contains the complete job queue infrastructure for submitting analytics workloads to the Kubernetes cluster.

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           EXTERNAL (Analytics Repos)                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Option A: HTTP (Recommended)          Option B: Direct Redis              │
│   ─────────────────────────────         ────────────────────────            │
│   import requests                       from client import JobClient        │
│                                                                             │
│   requests.post(                        client = JobClient()                │
│     "https://jobs.vectorized.pt/submit" job_id = client.submit(...)         │
│     json={"queue": "semantics", ...}                                        │
│   )                                                                         │
│                                                                             │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    │
                                    ▼
┌───────────────────────────────────────────────────────────────────────────────┐
│                           KUBERNETES CLUSTER                                  │
│                                                                               │
│  ┌─────────────────────┐      ┌──────────────────┐      ┌─────────────────┐  │
│  │    Job Gateway      │      │      Redis       │      │   ai-worker     │  │
│  │  (FastAPI @ :8000)  │─────▶│  (Queue Store)   │─────▶│   (Consumer)    │  │
│  │                     │      │                  │      │   [TODO]        │  │
│  │  jobs.vectorized.pt │      │  infrastructure  │      │    cognition    │  │
│  └─────────────────────┘      └──────────────────┘      └────────┬────────┘  │
│                                        ▲                         │           │
│                                        │                         ▼           │
│                                   ┌────┴─────┐          ┌────────────────┐   │
│                                   │   KEDA   │          │     vLLM       │   │
│                                   │  (0→N)   │          │   (GPU/LLM)    │   │
│                                   └──────────┘          └────────────────┘   │
└───────────────────────────────────────────────────────────────────────────────┘
```

## Directory Structure

```
services/jobs/
├── README.md              # This file
├── client.py              # Python client for direct Redis access (optional)
└── gateway/               # HTTP Gateway (deployed in Kubernetes)
    ├── Dockerfile
    ├── main.py            # FastAPI application
    └── requirements.txt
```


## Usage

### Option A: HTTP API (Recommended)

The simplest way — no Redis credentials needed, just HTTP:

```python
import requests

response = requests.post(
    "https://jobs.vectorized.pt/submit",
    json={
        "queue": "semantics",
        "payload": {
            "type": "embedding",
            "texts": ["Hello world", "Goodbye world"]
        }
    }
)

job_id = response.json()["job_id"]
print(f"Submitted: {job_id}")
```

#### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/submit` | Submit a job to a queue |
| `GET` | `/queue/{name}` | Get queue length |
| `GET` | `/health` | Health check |
| `GET` | `/docs` | Swagger UI (interactive docs) |

#### Request/Response Examples

**Submit Job:**
```bash
curl -X POST https://jobs.vectorized.pt/submit \
  -H "Content-Type: application/json" \
  -d '{"queue": "semantics", "payload": {"type": "embedding", "text": "Hello"}}'
```

Response:
```json
{"job_id": "550e8400-e29b-41d4-a716-446655440000", "queue": "semantics", "status": "queued"}
```

**Check Queue:**
```bash
curl https://jobs.vectorized.pt/queue/semantics
```

Response:
```json
{"queue": "semantics", "length": 42}
```

### Option B: Direct Redis Client

For advanced use cases where you need more control:

```python
from client import JobClient

client = JobClient()  # Reads REDIS_HOST, REDIS_PASSWORD from env

job_id = client.submit("semantics", {
    "type": "embedding",
    "texts": ["Hello world", "Goodbye world"]
})

# Optionally wait for result
result = client.wait_result(job_id, timeout=300)
```

#### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `REDIS_HOST` | Redis server hostname | `localhost` |
| `REDIS_PORT` | Redis server port | `6379` |
| `REDIS_PASSWORD` | Redis auth password | (required) |

## Queue Contract

| Queue | Direction | Purpose |
|-------|-----------|---------|
| `cognition:jobs:semantics` | IN | Semantic analysis jobs (embeddings, classification) |
| `cognition:jobs:ocr` | IN | OCR processing jobs |
| `cognition:results:{job_id}` | OUT | Per-job result queue |

### Job Payload Schema

```json
{
  "id": "uuid",           // Auto-generated if using client/gateway
  "payload": {
    "type": "embedding",  // Job type
    // ... custom fields
  }
}
```

## Monitoring

Use the monitoring script to observe queue depths and worker status:

```bash
./scripts/watch-jobs.sh
```

Output:
```
=== 🧠 Brain Node Job Monitor (ADR-041) ===
Time: Fri Jan 31 18:40:00 UTC 2026

--- Redis Queues ---
Queue Name                               Length
----------                               ------
cognition:jobs:semantics                 42
cognition:jobs:ocr                       5

--- Worker Pools ---
ai-worker-7b8c9d-abc12   1/1   Running   cognition

--- Compute Engine (vLLM) ---
vllm-5f6g7h-xyz89        1/1   Running   cognition
```

## Deployment

The gateway is **already deployed** and running at `https://jobs.vectorized.pt`.

### Updating the Gateway

If you need to rebuild and redeploy:

```bash
# Login to GHCR (uses Doppler for token)
doppler secrets get GH_PAT --plain -p talos-cluster -c prd | docker login ghcr.io -u hugoalmeidamoreira --password-stdin

# Build
cd services/jobs/gateway
docker build -t ghcr.io/hugoalmeidamoreira/job-gateway:latest .

# Push
docker push ghcr.io/hugoalmeidamoreira/job-gateway:latest

# Force pod restart (Flux will pull new image)
kubectl delete pod -n cognition -l app=job-gateway
```

Kubernetes manifests are in `manifests/tenants/cognition/base/job-gateway/`.

## TODO

- [ ] **ai-worker**: Create the Python consumer that processes jobs from Redis and calls vLLM.
- [ ] **Authentication**: Add API key or OAuth to the gateway (currently open).

## References

- [ADR-041: Analytics Job Submission](../../robot/architecture-decision-records/adr-041-analytics-job-submission.md)
- [ADR-039: Redis and KEDA](../../robot/architecture-decision-records/adr-039-redis-keda-queue-management.md)
