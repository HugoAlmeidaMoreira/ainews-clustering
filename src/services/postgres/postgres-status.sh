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
TUNNEL_HOSTNAME="postgres.hugomoreira.eu"
TUNNEL_PORT="5432"
TUNNEL_CMD="cloudflared access tcp --hostname $TUNNEL_HOSTNAME --url localhost:$TUNNEL_PORT"

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

# 1. Check if Tunnel is needed (are we local?)
# Simple heuristic: if we can't connect internally, we might be local.
# But usually we assume local if we are running this script manually.

echo -e "${BLUE}1. Checking Tunnel...${NC}"

if pgrep -f "$TUNNEL_HOSTNAME" > /dev/null; then
    echo -e "   ✅ Tunnel is ALREADY RUNNING."
    TUNNEL_ALREADY_RUNNING=true
else
    echo -e "   ⚠️  Tunnel NOT found."
    echo -e "   🚀 Starting temporary tunnel..."
    
    # Start tunnel in background
    $TUNNEL_CMD > /dev/null 2>&1 &
    TUNNEL_PID=$!
    TUNNEL_ALREADY_RUNNING=false
    
    # Wait for tunnel to establish
    sleep 3
    
    if kill -0 $TUNNEL_PID 2>/dev/null; then
         echo -e "   ✅ Tunnel started (PID: $TUNNEL_PID)"
    else
         echo -e "   ❌ Failed to start tunnel. Is cloudflared installed and authenticated?"
         exit 1
    fi
fi

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

# Cleanup
if [ "$TUNNEL_ALREADY_RUNNING" = false ]; then
    echo ""
    echo -e "${BLUE}3. Cleanup...${NC}"
    echo "   Stopping temporary tunnel..."
    kill $TUNNEL_PID
fi
