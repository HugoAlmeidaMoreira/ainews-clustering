#!/usr/bin/env bash
# services/postgres/postgres-status.sh
# Check connection to the PostgreSQL database (via Cloudflare Tunnel if local)

set -u

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Configuration
# (Now handled via tunnel.sh)

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║             🐘 POSTGRESQL STATUS                             ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Helper to check python connection
check_db_connection() {
    uv run python3 -c "
import sys
from src.modules.database import get_engine, text
try:
    engine = get_engine()
    with engine.connect() as conn:
        ver = conn.execute(text('SELECT version()')).scalar()
        db_name = engine.url.database
        print(f'   ✅ Connected to {db_name}')
        print(f'   ℹ️  Version: {ver.split()[0]} {ver.split()[1]}')
except Exception as e:
    print(f'   ❌ Connection Failed: {str(e).split(maxsplit=1)[0]} ...')
    sys.exit(1)
"
}

# 1. Check/Start Tunnel
echo -e "${BLUE}1. Ensuring Tunnel is running...${NC}"
"$(dirname "$0")/tunnel.sh" start

echo ""
echo -e "${BLUE}2. Database Connectivity...${NC}"

# Run connection check
if check_db_connection; then
    echo ""
    echo -e "   ${GREEN}System is HEALTHY${NC}"
else
    echo ""
    echo -e "   ${RED}System is UNHEALTHY${NC}"
fi
