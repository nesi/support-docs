#!/usr/bin/env bash
# Runs the same WCAG audit as the AccessLint/audit@v0 GitHub Action, locally.
#
# Usage: run_a11y_check.sh MIN_IMPACT [FILE...]
#   FILE  path(s) to source markdown pages under docs/ to audit. If omitted,
#         every page in the built sitemap is audited.
set -euo pipefail

MIN_IMPACT=$1
shift

CACHE_DIR="${HOME}/.cache/accesslint-audit"
# Keep the downloaded browser binary under CACHE_DIR too, so caching that one
# directory (e.g. actions/cache in CI) actually covers the expensive part.
export PLAYWRIGHT_BROWSERS_PATH="${CACHE_DIR}/browsers"
PORT="$(python3 -c 'import socket; s=socket.socket(); s.bind(("",0)); print(s.getsockname()[1]); s.close()')"

if [ ! -d "public" ]; then
  echo "Error: 'public' directory does not exist. Run a build first!" >&2
  exit 1
fi

if [ "$#" -eq 0 ]; then
  # No pages given: audit every page from the built sitemap.
  URLS="$(sed -n 's#.*<loc>\(.*\)</loc>.*#\1#p' public/sitemap.xml \
    | sed "s#^https\?://[^/]*/#http://localhost:${PORT}/#")"
else
  # Map each docs/*.md source path to the site-relative URL mkdocs builds it
  # to (docs_dir=docs, site_dir=public, directory urls), then audit just those.
  DOCS_DIR="$(pwd)/docs"
  URLS=""
  for f in "$@"; do
    file_abs="$(readlink -f "$f")"
    if [[ "$file_abs" != "$DOCS_DIR"/*.md ]]; then
      echo "Error: '$f' is not a markdown file under docs/." >&2
      exit 1
    fi
    rel="${file_abs#"$DOCS_DIR"/}"
    rel="${rel%.md}"
    if [ "$(basename "$rel")" = "index" ]; then
      rel="$(dirname "$rel")"
      [ "$rel" = "." ] && rel=""
    fi
    [ -n "$rel" ] && rel="${rel}/"
    URLS="${URLS}http://localhost:${PORT}/${rel}"$'\n'
  done
fi

if [ ! -d "$CACHE_DIR" ]; then
  git clone --depth 1 --branch v0 https://github.com/AccessLint/audit.git "$CACHE_DIR"
fi

READY_MARKER="$CACHE_DIR/.setup-complete"
if [ ! -f "$READY_MARKER" ]; then
  (cd "$CACHE_DIR" && npm ci --omit=dev --no-audit --no-fund --silent && npx --yes playwright install --only-shell chromium)
  touch "$READY_MARKER"
fi

# Redirected to avoid polluting this script's stdout, which callers pipe
# straight into a JSON parser (its access-log lines aren't valid JSON).
python3 -m http.server "$PORT" --directory public >/dev/null 2>&1 &
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

# AccessLint's own progress output and (source-mapless, so always empty here)
# annotations go to stderr, leaving stdout free to carry just the JSON report -
# so this script's output can be piped straight into parse_a11y_report.py.
env \
  INPUT_URLS="$URLS" \
  INPUT_WCAG-LEVEL="AA" \
  INPUT_FAIL-ON="never" \
  INPUT_MIN-IMPACT="$MIN_IMPACT" \
  "$NODE_BIN" "$CACHE_DIR/dist/index.js" >&2

cat accesslint-report.json
