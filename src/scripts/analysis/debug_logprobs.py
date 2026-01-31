import sys
import os
import math
import json

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.services.vllm.client import get_vllm_client

def test_scoring():
    client = get_vllm_client()
    
    title = "Câmara da Maia presente na Qualifica na era da IA"
    content = "O evento foca-se na era da inteligência artificial e no seu impacto orgânico no lado humano e no emprego."
    
    axis_name = "Opportunity vs. Risk"
    axis_desc = "1 is pure Opportunity/Hype. 9 is pure Risk/Fear."
    
    # Prompt mais simples para evitar tokens de sistema
    prompt = f"Article: {title}. {content}\nAxis: {axis_name} ({axis_desc})\nScore (1-9):"

    print(f"📡 Sending request to {client.model}...")
    
    try:
        response = client.client.chat.completions.create(
            model=client.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1, 
            temperature=0,
            logprobs=True,
            top_logprobs=20 # Pedimos 20 para garantir que apanhamos números
        )
        
        choice = response.choices[0]
        
        if choice.logprobs:
            token_data = choice.logprobs.content[0]
            print(f"\n🤖 Top token: '{token_data.token}'")
            print("📊 Top Candidates found:")
            
            found_numeric = False
            for top in token_data.top_logprobs:
                prob = math.exp(top.logprob)
                token = top.token.strip()
                if token.isdigit():
                    print(f"   ✅ Number '{token}' | Prob: {prob:.4f}")
                    found_numeric = True
                else:
                    print(f"   ◽ Other: '{token}' | Prob: {prob:.4f}")
            
            if not found_numeric:
                print("\n❌ No numbers in top 20 logprobs. The model is too distracted by system tokens.")
        else:
            print("\n❌ Logprobs not returned by the server.")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_scoring()
