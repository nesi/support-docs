#!/usr/bin/env bash
# Runs the same WCAG audit as the AccessLint/audit@v0 GitHub Action, locally.
set -euo pipefail

MIN_IMPACT=$1

CACHE_DIR="${HOME}/.cache/accesslint-audit"
PORT="$(python3 -c 'import socket; s=socket.socket(); s.bind(("",0)); print(s.getsockname()[1]); s.close()')"

if [ ! -d "public" ]; then
  echo "Error: 'public' directory does not exist. Run a build first!" >&2
  exit 1
fi

if [ -n "${2:-}" ]; then
  PAGE=$2
  URLS="http://localhost:${PORT}/${PAGE}"
else
  # No URL given: audit every page from the built sitemap.
  URLS="$(sed -n 's#.*<loc>\(.*\)</loc>.*#\1#p' public/sitemap.xml \
    | sed "s#^https\?://[^/]*/#http://localhost:${PORT}/#")"
fi

if [ ! -d "$CACHE_DIR" ]; then
  git clone --depth 1 --branch v0 https://github.com/AccessLint/audit.git "$CACHE_DIR"
fi

READY_MARKER="$CACHE_DIR/.setup-complete"
if [ ! -f "$READY_MARKER" ]; then
  (cd "$CACHE_DIR" && npm ci --omit=dev --no-audit --no-fund --silent && npx --yes playwright install --only-shell chromium)
  touch "$READY_MARKER"
fi

python3 -m http.server "$PORT" --directory public &
SERVER_PID=$!
trap 'kill "$SERVER_PID" 2>/dev/null || true' EXIT
python3 -c "
import socket, time
for _ in range(50):
    try:
        s = socket.socket()
        s.connect(('127.0.0.1', $PORT))
        s.close()
        break
    except Exception:
        time.sleep(0.1)
"

NODE_BIN="$(command -v node || true)"
if [ -z "$NODE_BIN" ]; then
  NODE_BIN="$(ls -d "$HOME"/.nvm/versions/node/*/bin/node 2>/dev/null | sort -V | tail -1)"
fi
if [ -z "$NODE_BIN" ]; then
  echo "Error: 'node' not found. Install Node.js or run this from a shell with nvm loaded." >&2
  exit 1
fi

env \
  INPUT_URLS="$URLS" \
  INPUT_WCAG-LEVEL="AA" \
  INPUT_FAIL-ON="never" \
  INPUT_MIN-IMPACT="$MIN_IMPACT" \
  "$NODE_BIN" "$CACHE_DIR/dist/index.js"
