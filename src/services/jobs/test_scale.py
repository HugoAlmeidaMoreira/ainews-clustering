"""
Tests scaling trigger by sending a single job to the queue.
"""
from analytics_client import JobGateway
import time
import sys

def main():
    gateway = JobGateway()
    
    # 1. Check current queue
    q = "semantics"
    initial = gateway.get_queue_length(q)
    print(f"📊 Initial queue length for '{q}': {initial}")
    
    # 2. Submit ONE job
    print(f"📤 Submitting 1 test job...")
    job_id = gateway.submit_job(
        queue=q,
        job_type="test_scale",
        payload={"message": "Wake up worker!", "timestamp": time.time()}
    )
    
    # 3. Watch queue for 60 seconds
    print(f"👀 Watching queue '{q}' to see if it drains (worker wakeup)...")
    for i in range(12):
        time.sleep(5)
        current = gateway.get_queue_length(q)
        print(f"   [{i*5}s] Queue length: {current}")
        
        if current > initial + 1:
             # Should not happen if we only sent 1
             pass
        elif current < initial + 1:
             print("🎉 Queue drained! Worker must be running.")
             return

    print("⚠️ Timeout. Queue did not drain. Worker might not be scaling up.")

if __name__ == "__main__":
    main()
