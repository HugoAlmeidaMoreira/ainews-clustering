import sys
import os
import math
import json
from typing import Dict, List

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.services.vllm.client import get_vllm_client

def calculate_probabilistic_score(logprobs_content) -> float:
    """
    Calculates the weighted average score from logprobs.
    We look for tokens '1' through '9'.
    """
    token_probs = {}
    total_relevant_prob = 0.0
    
    # logprobs_content is the first token's logprob data
    for item in logprobs_content.top_logprobs:
        token = item.token.strip()
        # Convert logprob to linear probability
        prob = math.exp(item.logprob)
        
        # We handle case where token might be a single digit
        if token in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            val = int(token)
            token_probs[val] = prob
            total_relevant_prob += prob
            
    if total_relevant_prob == 0:
        return None
        
    # Re-normalize probabilities among the numeric tokens we found
    weighted_sum = 0.0
    for val, prob in token_probs.items():
        normalized_prob = prob / total_relevant_prob
        weighted_sum += val * normalized_prob
        
    # Convert 1-9 scale to 0.0-1.0 scale
    # (val - 1) / 8
    final_score = (weighted_sum - 1) / 8
    return final_score

def test_scoring():
    client = get_vllm_client()
    # Explicitly set the model if not default
    client.model = "Qwen/Qwen2.5-7B-Instruct"
    
    # Sample News: Clearly an opportunity/tech-positive story
    title = "IA nas escolas da Maia: Alunos vão ter tutores inteligentes"
    content = "O projeto inovador traz tutores de IA para alunos do ensino básico, prometendo acelerar a aprendizagem e personalizar o ensino de forma revolucionária."
    
    axis_name = "Opportunity vs. Risk"
    axis_desc = "Evaluate the tone regarding AI. 1 means Pure Opportunity/Hype/Benefit. 9 means Pure Risk/Threat/Alarmism."
    
    # Using a format that Qwen likes
    messages = [
        {"role": "system", "content": "You are a precise linguistic analyst. Respond ONLY with a single digit from 1 to 9."},
        {"role": "user", "content": f"Classify this news on the axis '{axis_name}' ({axis_desc}).\n\nArticle: {title}\n{content}\n\nScore (1-9):"}
    ]

    print(f"📡 Sending request to {client.model}...")
    
    try:
        response = client.client.chat.completions.create(
            model=client.model,
            messages=messages,
            max_tokens=1,
            temperature=0,
            logprobs=True,
            top_logprobs=10
        )
        
        choice = response.choices[0]
        token = choice.message.content
        
        if not choice.logprobs:
            print("❌ No logprobs in response.")
            return

        first_token_logprobs = choice.logprobs.content[0]
        
        print(f"\n🤖 Model's Top Choice: '{token}'")
        print("📊 Top Token Probabilities:")
        for item in first_token_logprobs.top_logprobs:
            prob = math.exp(item.logprob)
            print(f"   Token: '{item.token}' | Prob: {prob:.4f}")
            
        score = calculate_probabilistic_score(first_token_logprobs)
        
        if score is not None:
            print(f"\n✅ Calculated Continuous Score: {score:.4f} (on 0.0-1.0 scale)")
            print(f"   Interpretation: {score*100:.1f}% towards 'Risk'")
            print(f"   (0% = Total Opportunity, 100% = Total Risk)")
        else:
            print("\n❌ Could not calculate score (no numeric tokens '1'-'9' found in top logprobs).")

    except Exception as e:
        print(f"❌ Error during request: {e}")

if __name__ == "__main__":
    test_scoring()
