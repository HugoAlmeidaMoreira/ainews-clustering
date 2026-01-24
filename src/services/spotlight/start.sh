#!/usr/bin/env bash
# services/spotlight/start.sh
# Start the Renumics Spotlight visualization service

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}🔍 Starting Renumics Spotlight...${NC}"

# Ensure we are in the project root if run from the script location
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$(dirname "$(dirname "$SCRIPT_DIR")")")"

cd "$PROJECT_ROOT"

# Run via uv/python
echo -e "   Host: http://localhost:7000"
echo -e "   (Use Ctrl+C to stop)"
echo ""

uv run python src/services/spotlight/viewer.py
