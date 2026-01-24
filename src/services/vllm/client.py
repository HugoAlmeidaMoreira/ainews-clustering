import os
import base64
from typing import List, Optional, Dict, Any
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class VLLMClient:
    """
    Client for interacting with the vLLM inference engine.
    Uses OpenAI-compatible API with Basic Authentication.
    """
    
    DEFAULT_HOST = "https://vllm.vectorized.pt/v1"
    DEFAULT_MODEL = "openai/gpt-oss-20b"

    def __init__(
        self, 
        base_url: Optional[str] = None, 
        user: Optional[str] = None, 
        password: Optional[str] = None,
        default_model: Optional[str] = None
    ):
        self.base_url = base_url or os.getenv("VLLM_HOST", self.DEFAULT_HOST)
        self.user = user or os.getenv("VLLM_USER", "admin")
        self.password = password or os.getenv("VLLM_PASSWORD")
        self.model = default_model or os.getenv("VLLM_MODEL", self.DEFAULT_MODEL)

        if not self.password:
            raise ValueError("VLLM_PASSWORD environment variable is not set")

        # Initialize OpenAI client with Basic Auth
        # We use headers because the base_url with credentials can sometimes be tricky with some libs
        auth_str = f"{self.user}:{self.password}"
        encoded_auth = base64.b64encode(auth_str.encode()).decode()
        
        self.client = OpenAI(
            base_url=self.base_url,
            api_key="EMPTY", # Required by library but ignored by vLLM
            default_headers={
                "Authorization": f"Basic {encoded_auth}",
                "User-Agent": "curl/8.5.0"
            }
        )

    def list_models(self) -> List[str]:
        """List all available models."""
        models = self.client.models.list()
        return [model.id for model in models.data]

    def chat_completion(
        self, 
        messages: List[Dict[str, str]], 
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 512,
        **kwargs
    ) -> str:
        """
        Send a chat completion request.
        """
        response = self.client.chat.completions.create(
            model=model or self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )
        return response.choices[0].message.content

    def get_joke(self, topic: str = "programming") -> str:
        """Helper method to get a joke."""
        messages = [
            {"role": "system", "content": "You are a witty comedian."},
            {"role": "user", "content": f"Tell me a funny joke about {topic}."}
        ]
        return self.chat_completion(messages)

def get_vllm_client() -> VLLMClient:
    """Factory function to get a configured VLLMClient."""
    return VLLMClient()
