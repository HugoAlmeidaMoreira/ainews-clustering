#!/usr/bin/env python3
"""Check available vLLM models"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.services.vllm.client import get_vllm_client

try:
    client = get_vllm_client()
    print("🔍 Checking available vLLM models...\n")
    
    models = client.list_models()
    print(f"✅ Found {len(models)} model(s):\n")
    for model in models:
        print(f"  - {model}")
    
    print(f"\n📌 Current default model: {client.model}")
    
    if client.model not in models:
        print(f"\n⚠️  WARNING: Default model '{client.model}' is NOT in the available models!")
        print(f"   You should update VLLM_MODEL environment variable to one of the available models.")
    else:
        print(f"\n✅ Default model is available!")
        
except Exception as e:
    print(f"❌ Error connecting to vLLM: {e}")
