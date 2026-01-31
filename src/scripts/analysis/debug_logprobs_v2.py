import sys
import os
import math

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.services.vllm.client import get_vllm_client

def test_scoring_v2():
    client = get_vllm_client()
    
    title = "IA nas escolas da Maia"
    content = "Projeto inovador traz tutores de IA para alunos do ensino básico."
    
    # Tentando "enganar" o ChatML do gpt-oss-20b
    prompt = f"""<|im_start|>system
You are a categorical scorer. Respond ONLY with a single digit 1-9. No other text.<|im_end|>
<|im_start|>user
Article: {title}
Axis: Opportunity (1) vs Risk (9)
Score:<|im_end|>
<|im_start|>assistant
"""

    print(f"📡 Sending ChatML tuned request...")
    
    try:
        response = client.client.chat.completions.create(
            model=client.model,
            messages=[{"role": "user", "content": prompt}], # Mandamos no user mas com os tags lá dentro
            max_tokens=1, 
            temperature=0,
            logprobs=True,
            top_logprobs=10
        )
        
        token_data = response.choices[0].logprobs.content[0]
        print(f"\n🤖 Top token: '{token_data.token}'")
        for top in token_data.top_logprobs:
            prob = math.exp(top.logprob)
            print(f"   Token: '{top.token}' | Prob: {prob:.4f}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_scoring_v2()
