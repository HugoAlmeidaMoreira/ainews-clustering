#!/usr/bin/env bash
# services/embeddings/embeddings-status.sh
# Quick Embeddings status overview

# Main Header
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║             🧠 EMBEDDINGS (BGE-M3)                           ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

set -euo pipefail

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

HOST="https://embeddings.vectorized.pt"

echo "🔌 SERVICE"
echo "────────────────────────────────────────"
printf "   Endpoint: %s\n" "$HOST"

# 1. API Health Check
# Note: Using -L to follow redirects and -f to fail on non-2xx
if curl -s -f -L "$HOST/health" > /dev/null; then
    printf "   Status:   🟢 Online\n"
else
    printf "   Status:   🔴 Offline (Internal error or redirect loop)\n"
fi
echo ""

# 2. Kubernetes Pod Status
echo "🐳 POD STATUS"
echo "────────────────────────────────────────"
# Get the youngest Running pod
pod_info=$(kubectl get pods -n cognition -l app=embeddings --field-selector=status.phase=Running --no-headers 2>/dev/null | \
    sort -k5,5 | \
    head -1)

if [ -n "$pod_info" ]; then
    pod_name=$(echo "$pod_info" | awk '{print $1}')
    pod_status=$(echo "$pod_info" | awk '{print $3}')
    pod_age=$(echo "$pod_info" | awk '{print $5}')
    
    printf "   Pod:      %s\n" "$pod_name"
    printf "   Status:   %s\n" "$pod_status"
    printf "   Age:      %s\n" "$pod_age"
    
    # Node Info
    node_name=$(kubectl get pod "$pod_name" -n cognition -o jsonpath='{.spec.nodeName}')
    printf "   Node:     %s\n" "$node_name"
fi

echo ""
echo "────────────────────────────────────────"
echo "📅 $(date '+%Y-%m-%d %H:%M:%S')"
