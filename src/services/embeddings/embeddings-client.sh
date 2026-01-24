#!/usr/bin/env bash
# =============================================================================
# Embeddings Client - TEI API Client
# Usage: ./embeddings-client.sh <command> [args]
# =============================================================================

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

HOST="https://embeddings.vectorized.pt"

# Helper to call API
api_call() {
    local endpoint="$1"
    local data="${2:-}"
    
    if [ -n "$data" ]; then
        curl -s -X POST "$HOST$endpoint" \
            -H "Content-Type: application/json" \
            -d "$data"
    else
        curl -s "$HOST$endpoint"
    fi
}

# Commands

cmd_info() {
    echo -e "${BLUE}Model Info (TEI):${NC}"
    api_call "/" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    print(json.dumps(d, indent=2))
except:
    print('  (Error parsing response or root endpoint is just empty)')
"
}

cmd_embed() {
    local msg="$1"
    
    echo -e "${BLUE}Generating embedding for: ${NC}\"$msg\""
    
    payload=$(cat <<EOF
{
  "inputs": "$msg"
}
EOF
)
    api_call "/embed" "$payload" | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    # Most TEI implementations return a list of lists or just a list
    if isinstance(d, list):
        if len(d) > 0 and isinstance(d[0], list):
             vec = d[0]
        else:
             vec = d
        print(f\"  Vector (first 5 dims): {vec[:5]}... [Length: {len(vec)}]\")
    else:
        print(json.dumps(d, indent=2))
except Exception as e:
    print('Error:', e)
    print(sys.stdin.read())
"
}

cmd_health() {
    echo -e "${BLUE}Checking Health...${NC}"
    status=$(api_call "/health")
    if [ "$status" == "null" ] || [ -z "$status" ]; then
        # Some TEI versions return empty or null for OK
        echo -e "${GREEN}Service is UP (Status: OK)${NC}"
    else
        echo "$status"
    fi
}

show_help() {
    echo -e "${BLUE}Embeddings Client${NC} - TEI API Wrapper"
    echo ""
    echo "Usage: $0 <command> [args]"
    echo ""
    echo "Commands:"
    echo -e "  ${GREEN}info${NC}             Show model details"
    echo -e "  ${GREEN}embed${NC} \"text\"      Generate vector for text"
    echo -e "  ${GREEN}health${NC}           Check /health endpoint"
    echo ""
}

case "${1:-help}" in
    info)   cmd_info ;;
    embed)  cmd_embed "$2" ;;
    health) cmd_health ;;
    *)      show_help ;;
esac
