import os
import requests
from typing import List, Union, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class EmbeddingsClient:
    """
    Client for interacting with the Text Embeddings Inference (TEI) service.
    """
    
    DEFAULT_HOST = "https://embeddings.vectorized.pt"

    def __init__(self, base_url: Optional[str] = None):
        self.base_url = base_url or os.getenv("EMBEDDINGS_HOST", self.DEFAULT_HOST)

    def generate(self, inputs: Union[str, List[str]]) -> Union[List[float], List[List[float]]]:
        """
        Generate embeddings for the given inputs.
        
        Args:
            inputs: A single string or a list of strings to embed.
            
        Returns:
            If a single string is provided, returns a list of floats (the embedding).
            If a list of strings is provided, returns a list of lists of floats.
        """
        is_single = isinstance(inputs, str)
        payload = {"inputs": inputs}
        
        response = requests.post(f"{self.base_url}/embed", json=payload)
        response.raise_for_status()
        
        data = response.json()
        
        # TEI usually returns a list of embeddings. 
        # If we sent a single string, it might still return [[...]] or just [...] depending on TEI config.
        # But usually it's consistent with the input shape.
        return data

    def health(self) -> bool:
        """Check if the service is healthy."""
        try:
            response = requests.get(f"{self.base_url}/health")
            # TEI /health often returns 200 OK with null or empty body
            return response.status_code == 200
        except:
            return False

    def info(self) -> dict:
        """Get model information."""
        response = requests.get(self.base_url)
        response.raise_for_status()
        return response.json()

def get_embeddings_client() -> EmbeddingsClient:
    """Factory function to get a configured EmbeddingsClient."""
    return EmbeddingsClient()
