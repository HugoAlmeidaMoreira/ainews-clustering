import sys
import os
from dotenv import load_dotenv

# Ensure we can import from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from services.vllm import get_vllm_client

def main():
    # Load environment variables from .env
    load_dotenv()
    
    print("🚀 Initializing vLLM Connectivity Test")
    print("--------------------------------------")
    
    try:
        # Get client
        client = get_vllm_client()
        
        # Check models
        print("🔍 Querying available models...")
        models = client.list_models()
        if models:
            print(f"✅ Connection successful!")
            print(f"📦 Active Models: {', '.join(models)}")
        else:
            print("⚠️ Connected, but no models found.")

        # Request a joke
        print("\n🤖 Requesting AI-generated humor...")
        joke = client.get_joke("data science and neural networks")
        
        print("\n" + "="*50)
        print("THE JOKE:")
        print("="*50)
        print(joke)
        print("="*50 + "\n")
        
    except Exception as e:
        print(f"\n❌ FAILED: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Ensure 'VLLM_USER' and 'VLLM_PASSWORD' are set in your .env file.")
        print("2. Check if the Cloudflare Tunnel to 'vllm.vectorized.pt' is active.")
        print("3. Verify your internet connection.")

if __name__ == "__main__":
    main()
