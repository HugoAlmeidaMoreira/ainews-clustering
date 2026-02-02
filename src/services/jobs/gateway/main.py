"""
Job Gateway API (ADR-041)

Minimal FastAPI service that bridges HTTP → Redis for job submission.
Runs inside Kubernetes, exposes jobs.vectorized.pt/submit endpoint.

Endpoints:
    POST /submit       - Submit a job to a queue
    GET  /status/{id}  - Check job status (optional)
    GET  /health       - Health check
"""

import json
import os
import uuid
from typing import Optional

import redis
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Job Gateway",
    description="HTTP bridge for Redis job queues (ADR-041)",
    version="1.0.0",
)

# Redis connection (reads from env)
REDIS_HOST = os.getenv("REDIS_HOST", "redis.infrastructure.svc.cluster.local")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
QUEUE_PREFIX = os.getenv("QUEUE_PREFIX", "cognition:jobs")
RESULTS_PREFIX = os.getenv("RESULTS_PREFIX", "cognition:results")

_redis: Optional[redis.Redis] = None


def get_redis() -> redis.Redis:
    global _redis
    if _redis is None:
        _redis = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD,
            decode_responses=True,
        )
    return _redis


# === Request/Response Models ===

class JobSubmission(BaseModel):
    queue: str  # e.g., "semantics"
    payload: dict  # Arbitrary JSON payload


class JobResponse(BaseModel):
    job_id: str
    queue: str
    status: str = "queued"


class QueueStatus(BaseModel):
    queue: str
    length: int


# === Endpoints ===

@app.post("/submit", response_model=JobResponse)
async def submit_job(job: JobSubmission):
    """Submit a job to the specified queue."""
    r = get_redis()
    
    job_id = str(uuid.uuid4())
    job_data = {
        "id": job_id,
        "payload": job.payload,
    }
    
    queue_key = f"{QUEUE_PREFIX}:{job.queue}"
    
    try:
        r.lpush(queue_key, json.dumps(job_data))
    except redis.ConnectionError as e:
        raise HTTPException(status_code=503, detail=f"Redis unavailable: {e}")
    
    return JobResponse(job_id=job_id, queue=job.queue)


@app.get("/queue/{queue_name}", response_model=QueueStatus)
async def get_queue_status(queue_name: str):
    """Get the number of pending jobs in a queue."""
    r = get_redis()
    queue_key = f"{QUEUE_PREFIX}:{queue_name}"
    
    try:
        length = r.llen(queue_key)
    except redis.ConnectionError as e:
        raise HTTPException(status_code=503, detail=f"Redis unavailable: {e}")
    
    return QueueStatus(queue=queue_name, length=length)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    r = get_redis()
    try:
        r.ping()
        return {"status": "healthy", "redis": "connected"}
    except redis.ConnectionError:
        raise HTTPException(status_code=503, detail="Redis unavailable")


@app.get("/")
async def root():
    """Root endpoint with API info."""
    return {
        "service": "Job Gateway",
        "version": "1.0.0",
        "docs": "/docs",
        "submit": "POST /submit",
    }
