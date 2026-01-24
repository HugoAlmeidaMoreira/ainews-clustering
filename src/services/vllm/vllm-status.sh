#!/usr/bin/env bash
# services/vllm/vllm-status.sh
# Quick vLLM status overview
# Usage: ./services/vllm/vllm-status.sh

# Main Header
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║             🧪 vLLM INFERENCE ENGINE                         ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

set -e

# Doppler config
PROJECT=${DOPPLER_PROJECT:-talos-cluster}
CONFIG=${DOPPLER_CONFIG:-prd}

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

HOST="https://vllm.vectorized.pt"

# Get secrets for Auth
eval $(doppler run -p "$PROJECT" -c "$CONFIG" -- bash -c 'echo "export VLLM_USER=$VLLM_USER VLLM_PASSWORD=$VLLM_PASSWORD"')

echo "🔌 SERVICE"
echo "────────────────────────────────────────"
printf "   Endpoint: %s\n" "$HOST"

# 1. API Health Check
if curl -s -u "$VLLM_USER:$VLLM_PASSWORD" "$HOST/health" > /dev/null; then
    printf "   Status:   🟢 Online\n"
else
    printf "   Status:   🔴 Offline (503/Conn refused)\n"
fi
echo ""

# 2. Loaded Model
echo "🔥 LOADED MODEL"
echo "────────────────────────────────────────"
response=$(curl -s -u "$VLLM_USER:$VLLM_PASSWORD" "$HOST/v1/models")
if echo "$response" | grep -q "id"; then
    echo "$response" | python3 -c "
import sys, json
d = json.load(sys.stdin)
for m in d.get('data', []):
    id = m.get('id', 'unknown')
    print(f'   🟢 {id}')
"
else
    echo "   (No model information available)"
fi
echo ""
# Kubernetes Pod Status
echo "🐳 POD STATUS"
echo "────────────────────────────────────────"
# Get all pods, sort by status (Running first), then pick the first one
pod_info=$(kubectl get pods -n cognition -l app=vllm --no-headers 2>/dev/null | \
    awk '{ print $0 }' | \
    sort -k3,3r | \
    head -1)

if [ -n "$pod_info" ]; then
    pod_name=$(echo "$pod_info" | awk '{print $1}')
    pod_status=$(echo "$pod_info" | awk '{print $3}')
    pod_age=$(echo "$pod_info" | awk '{print $5}')
    
    printf "   Pod:      %s\n" "$pod_name"
    printf "   Status:   %s\n" "$pod_status"
    printf "   Age:      %s\n" "$pod_age"
fi
echo ""

# 4. GPU Status (HW-BRAIN-01)
echo "🎮 GPU STATUS (GB10)"
echo "────────────────────────────────────────"
BRAIN_KEY="$HOME/.ssh/brain_key"
if [ -f "$BRAIN_KEY" ]; then
    ssh -i "$BRAIN_KEY" -o BatchMode=yes -o ConnectTimeout=2 hugo@192.168.1.181 "nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.total --format=csv,noheader,nounits" 2>/dev/null | while IFS=, read -r util used total; do
        printf "   GPU Util: %s%%\n" "$util"
        printf "   VRAM:     %s / %s MiB\n" "$used" "$total"
    done
else
    echo "   (SSH Key not found)"
fi
echo ""
echo "────────────────────────────────────────"
echo "📅 $(date '+%Y-%m-%d %H:%M:%S')"
