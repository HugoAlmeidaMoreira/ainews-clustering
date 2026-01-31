import os
import requests
from typing import List, Union, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class EmbeddingsClient:
    """
    Client for interacting with the vLLM Embeddings service (OpenAI-compatible).
    """
    
    DEFAULT_HOST = "https://embeddings.vectorized.pt"
    DEFAULT_MODEL = "BAAI/bge-m3"

    def __init__(self, base_url: Optional[str] = None, model: Optional[str] = None):
        self.base_url = base_url or os.getenv("EMBEDDINGS_HOST", self.DEFAULT_HOST)
        # Remove trailing slash if present
        self.base_url = self.base_url.rstrip("/")
        self.model = model or os.getenv("EMBEDDINGS_MODEL", self.DEFAULT_MODEL)

    def generate(self, inputs: Union[str, List[str]]) -> Union[List[float], List[List[float]]]:
        """
        Generate embeddings for the given inputs using OpenAI-compatible API.
        
        Args:
            inputs: A single string or a list of strings to embed.
            
        Returns:
            If a single string is provided, returns a list of floats (the embedding).
            If a list of strings is provided, returns a list of lists of floats.
        """
        is_single = isinstance(inputs, str)
        # OpenAI API expects "input" field, can be string or array of strings
        payload = {
            "model": self.model,
            "input": inputs
        }
        
        response = requests.post(f"{self.base_url}/v1/embeddings", json=payload)
        response.raise_for_status()
        
        data = response.json()
        
        # OpenAI format: {"object": "list", "data": [{"embedding": [...], "index": 0}, ...]}
        results = sorted(data["data"], key=lambda x: x["index"])
        embeddings = [item["embedding"] for item in results]
        
        if is_single:
            return embeddings[0]
        return embeddings

    def health(self) -> bool:
        """Check if the service is healthy (basic reachability via models endpoint)."""
        try:
            response = requests.get(f"{self.base_url}/v1/models")
            return response.status_code == 200
        except:
            return False

    def info(self) -> dict:
        """Get model information."""
        response = requests.get(f"{self.base_url}/v1/models")
        response.raise_for_status()
        return response.json()

def get_embeddings_client() -> EmbeddingsClient:
    """Factory function to get a configured EmbeddingsClient."""
    return EmbeddingsClient()
