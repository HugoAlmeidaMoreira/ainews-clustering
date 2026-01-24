#!/usr/bin/env bash
# =============================================================================
# vLLM Client - OpenAI API Compatible Client
# Usage: ./vllm-client.sh <command> [args]
# =============================================================================

set -euo pipefail

# Doppler config
PROJECT=${DOPPLER_PROJECT:-talos-cluster}
CONFIG=${DOPPLER_CONFIG:-prd}

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

# Get Config from Doppler
get_secret() {
    doppler run -p "$PROJECT" -c "$CONFIG" -- printenv "$1"
}

HOST="https://vllm.vectorized.pt"
USER=$(get_secret "VLLM_USER")
PASS=$(get_secret "VLLM_PASSWORD")

# Helper to call API
api_call() {
    local endpoint="$1"
    local data="${2:-}"
    
    if [ -n "$data" ]; then
        curl -s -X POST -u "$USER:$PASS" "$HOST$endpoint" \
            -H "Content-Type: application/json" \
            -d "$data"
    else
        curl -s -u "$USER:$PASS" "$HOST$endpoint"
    fi
}

# Commands

cmd_models() {
    echo -e "${BLUE}Available Models (vLLM):${NC}"
    api_call "/v1/models" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    for m in d.get('data', []):
        print(f\"  • {m.get('id', 'unknown')}\")
except:
    print('  (Error parsing response)')
"
}

cmd_chat() {
    local msg="$1"
    local model="$2"
    
    # Auto-detect model if not provided
    if [ -z "$model" ]; then
        model=$(api_call "/v1/models" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('data',[{}])[0].get('id',''))" 2>/dev/null)
    fi
    
    echo -e "${BLUE}Sending to ${GREEN}$model${BLUE}...${NC}"
    
    payload=$(cat <<EOF
{
  "model": "$model",
  "messages": [{"role": "user", "content": "$msg"}],
  "max_tokens": 512,
  "temperature": 0.7
}
EOF
)
    api_call "/v1/chat/completions" "$payload" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    print(d['choices'][0]['message']['content'])
except:
    print('Error:', sys.stdin.read())
"
}

cmd_health() {
    echo -e "${BLUE}Checking Health...${NC}"
    status=$(api_call "/health")
    echo "$status"
}

show_help() {
    echo -e "${BLUE}vLLM Client${NC} - OpenAI API Wrapper"
    echo ""
    echo "Usage: $0 <command> [args]"
    echo ""
    echo "Commands:"
    echo -e "  ${GREEN}models${NC}           List loaded models"
    echo -e "  ${GREEN}chat${NC} \"msg\"      Send a chat message"
    echo -e "  ${GREEN}health${NC}           Check /health endpoint"
    echo ""
}

case "${1:-help}" in
    models) cmd_models ;;
    chat)   cmd_chat "$2" "${3:-}" ;;
    health) cmd_health ;;
    *)      show_help ;;
esac
