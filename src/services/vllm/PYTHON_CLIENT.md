# vLLM Python Integration Guide

This guide explains how to connect your analytical workflows (Jupyter, Python scripts) to the **vLLM Inference Engine** running on the cluster.

## 1. Prerequisites

You need the `openai` python package, as vLLM provides an OpenAI-compatible API.

```bash
uv add openai
# or
pip install openai
```

## 2. Basic Connection

You must authenticate using the **Basic Auth** credentials (`VLLM_USER` / `VLLM_PASSWORD`) managed in Doppler.

```python
import os
from openai import OpenAI

# Configuration (Replace with your Doppler secrets or Env Vars)
VLLM_HOST = "https://vllm.vectorized.pt/v1"
VLLM_USER = os.getenv("VLLM_USER", "admin")
VLLM_PASS = os.getenv("VLLM_PASSWORD", "your-password-here")

# Initialize Client
# Note: api_key is required by the library but ignored by vLLM
# Note: User-Agent spoofing may be required if Cloudflare blocks default library headers
client = OpenAI(
    base_url=VLLM_HOST,
    api_key="EMPTY",
    default_headers={
        "Authorization": f"Basic {base64.b64encode(f'{VLLM_USER}:{VLLM_PASS}'.encode()).decode()}",
        "User-Agent": "curl/8.5.0"
    }
)
```

**Alternative**: If using standard Basic Auth URL syntax (ensure headers still include User-Agent if Cloudflare is active):
```python
client = OpenAI(
    base_url=f"https://{VLLM_USER}:{VLLM_PASS}@vllm.vectorized.pt/v1",
    api_key="EMPTY",
    default_headers={"User-Agent": "curl/8.5.0"}
)
```

## 3. List Available Models

Check which models are currently loaded in the engine.

```python
models = client.models.list()
for model in models.data:
    print(f"🟢 Active Model: {model.id}")
```

## 4. Inference (Chat Completion)

Run inference using the standard Chat API.

```python
completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1-Distill-Llama-8B", # Use the ID from step 3
    messages=[
        {"role": "system", "content": "You are a helpful data analysis assistant."},
        {"role": "user", "content": "Explain the concept of Vector Embeddings in 3 bullet points."}
    ],
    temperature=0.7,
    max_tokens=512
)

print(completion.choices[0].message.content)
```

## 5. Batch Inference (Advanced)

For high-throughput analytical tasks (e.g., classifying 1000 rows in a DataFrame), use asynchronous requests.

```python
import asyncio
from openai import AsyncOpenAI

async def analyze_data():
    client = AsyncOpenAI(
        base_url=f"https://{VLLM_USER}:{VLLM_PASS}@vllm.vectorized.pt/v1",
        api_key="EMPTY"
    )
    
    tasks = [
        client.chat.completions.create(
            model="active-model-id",
            messages=[{"role": "user", "content": f"Classify this text: {text}"}]
        )
        for text in large_dataset
    ]
    
    results = await asyncio.gather(*tasks)
    return [r.choices[0].message.content for r in results]
```
