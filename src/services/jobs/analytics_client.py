"""
Analytics Job Gateway Client (ADR-041)
--------------------------------------
Single-file client to submit jobs to the Vectorized Job Gateway.
Dependency: `pip install requests`

Usage:
    from analytics_client import JobGateway

    gateway = JobGateway()
    gateway.submit("semantics", {"type": "embedding", "texts": ["Hello"]})
"""

import os
import json
import uuid
import logging
from typing import Dict, Any, Optional, Union, List

try:
    import requests
except ImportError:
    print("❌ Missing dependency: pip install requests")
    exit(1)

# Configure logging
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger("JobGateway")

class JobGateway:
    def __init__(self, base_url: str = "https://jobs.vectorized.pt", api_key: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key or os.getenv("JOB_GATEWAY_KEY")
        self._session = requests.Session()
        
        # Headers (prepared for future auth)
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Analytics-Repo/1.0"
        }
        if self.api_key:
            self.headers["Authorization"] = f"Bearer {self.api_key}"

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Internal request handler with error management."""
        url = f"{self.base_url}{endpoint}"
        try:
            response = self._session.request(
                method, url, headers=self.headers, timeout=10, **kwargs
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ConnectionError:
            logger.error(f"❌ Could not connect to {self.base_url}. Is the cluster/VPN active?")
            raise
        except requests.exceptions.HTTPError as e:
            logger.error(f"❌ HTTP Error {e.response.status_code}: {e.response.text}")
            raise
        except Exception as e:
            logger.error(f"❌ Unexpected error: {e}")
            raise

    def check_health(self) -> bool:
        """Check if the gateway is reachable and healthy."""
        try:
            data = self._request("GET", "/health")
            status = data.get("status") == "healthy"
            redis = data.get("redis") == "connected"
            if status and redis:
                logger.info(f"✅ Gateway Healthy @ {self.base_url}")
                return True
            logger.warning(f"⚠️ Gateway Unhealthy: {data}")
            return False
        except:
            return False

    def get_queue_length(self, queue_name: str) -> int:
        """Get the number of pending jobs in a specific queue."""
        data = self._request("GET", f"/queue/{queue_name}")
        return data.get("length", 0)

    def submit_job(
        self, 
        queue: str, 
        job_type: str, 
        payload: Dict[str, Any], 
        job_id: Optional[str] = None
    ) -> str:
        """
        Submit a job to the cluster.
        
        Args:
            queue: Target queue (e.g., 'semantics', 'ocr')
            job_type: Type of work (e.g., 'embedding', 'chat')
            payload: The actual data (texts, messages, etc.)
            job_id: Optional custom UUID (auto-generated if None)
            
        Returns:
            job_id (str): The ID of the submitted job.
        """
        # Construct full payload as expected by ai-worker
        full_payload = {
            "type": job_type,
            **payload
        }
        
        # Create submission envelope matches Gateway API
        submission = {
            "queue": queue,
            "payload": full_payload
        }
        
        # Note: If gateway accepts ID in body, we could add connection here.
        # Current v1 API generates ID server-side unless modified.
        
        data = self._request("POST", "/submit", json=submission)
        jid = data.get("job_id")
        logger.debug(f"🚀 Job Queued: {jid} -> {queue}")
        return jid

# === CLI for Quick Testing ===
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Job Gateway CLI")
    parser.add_argument("--check", action="store_true", help="Health check")
    parser.add_argument("--queue", type=str, help="Check queue length")
    parser.add_argument("--test-embedding", action="store_true", help="Submit test embedding job")
    
    args = parser.parse_args()
    
    client = JobGateway()
    
    if args.check:
        client.check_health()
    
    if args.queue:
        length = client.get_queue_length(args.queue)
        print(f"Queue '{args.queue}' length: {length}")
        
    if args.test_embedding:
        print("Submitting test job...")
        client.submit_job(
            queue="semantics",
            job_type="embedding",
            payload={
                "texts": ["This is a test from the analytics client."],
                "model": "mesolitica/Qwen2.5-72B-Instruct-FP8"
            }
        )
