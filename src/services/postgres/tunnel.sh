#!/usr/bin/env bash
# services/postgres/tunnel.sh
# Manage the Cloudflare Tunnel for local Postgres access

PID_FILE="/tmp/postgres_tunnel.pid"
LOG_FILE="/tmp/postgres_tunnel.log"
HOSTNAME="postgres.hugomoreira.eu"
PORT="5432"

start_tunnel() {
    if [ -f "$PID_FILE" ] && kill -0 $(cat "$PID_FILE") 2>/dev/null; then
        echo "✅ Tunnel is already running (PID: $(cat "$PID_FILE"))"
    else
        echo "🚀 Starting tunnel to $HOSTNAME..."
        cloudflared access tcp --hostname "$HOSTNAME" --url "localhost:$PORT" > "$LOG_FILE" 2>&1 &
        echo $! > "$PID_FILE"
        sleep 2
        if kill -0 $(cat "$PID_FILE") 2>/dev/null; then
            echo "✅ Tunnel started (PID: $(cat "$PID_FILE"))"
            echo "   Logs at: $LOG_FILE"
        else
            echo "❌ Failed to start tunnel. Check logs:"
            cat "$LOG_FILE"
        fi
    fi
}

stop_tunnel() {
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if kill -0 "$PID" 2>/dev/null; then
            echo "🛑 Stopping tunnel (PID: $PID)..."
            kill "$PID"
            rm "$PID_FILE"
            echo "✅ Tunnel stopped."
        else
            echo "⚠️  Tunnel process $PID not found. Cleaning up pid file."
            rm "$PID_FILE"
        fi
    else
        # Try to find by name just in case
        PIDS=$(pgrep -f "cloudflared.*$HOSTNAME")
        if [ -n "$PIDS" ]; then
            echo "🛑 Stopping orphaned tunnel processes: $PIDS"
            echo "$PIDS" | xargs kill
        else
            echo "ℹ️  No tunnel appears to be running."
        fi
    fi
}

status_tunnel() {
    if [ -f "$PID_FILE" ] && kill -0 $(cat "$PID_FILE") 2>/dev/null; then
        echo "🟢 Tunnel is ACTIVE (PID: $(cat "$PID_FILE"))"
    elif pgrep -f "cloudflared.*$HOSTNAME" > /dev/null; then
        echo "🟢 Tunnel is ACTIVE (Managed externally/orphaned)"
    else
        echo "🔴 Tunnel is STOPPED"
    fi
}

case "${1:-status}" in
    start)  start_tunnel ;;
    stop)   stop_tunnel ;;
    status) status_tunnel ;;
    restart) stop_tunnel; sleep 1; start_tunnel ;;
    *)      echo "Usage: $0 {start|stop|status|restart}" ;;
esac
