#!/usr/bin/env bash
# Runs the same WCAG audit as the AccessLint/audit@v0 GitHub Action, locally.
#
# Usage: run_a11y_check.sh MIN_IMPACT [FILE...]
#   FILE  path(s) to source markdown pages under docs/ to audit. If omitted,
#         every page in the built sitemap is audited.
set -euo pipefail

MIN_IMPACT=$1
shift

# AccessLint/audit commit to run (v0.3.3). Pinned rather than following the
# moving 'v0' tag, because its Playwright version must match the container
# image in .github/workflows/checks.yml. When changing this, update the image.
ACCESSLINT_REF="d56a0efa8fc5d78391a29dd593c8f3bc91f32c26"
CACHE_DIR="${HOME}/.cache/accesslint-audit"
# Use a browser that is already installed (CI sets this to the Playwright
# image's /ms-playwright). Otherwise keep the downloaded browser under
# CACHE_DIR, so caching that one directory covers the expensive part.
export PLAYWRIGHT_BROWSERS_PATH="${PLAYWRIGHT_BROWSERS_PATH:-${CACHE_DIR}/browsers}"
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

# Re-fetch if the cached copy is missing or at a different commit.
if [ "$(git -C "$CACHE_DIR" rev-parse HEAD 2>/dev/null)" != "$ACCESSLINT_REF" ]; then
  rm -rf "$CACHE_DIR"
  git init -q "$CACHE_DIR"
  git -C "$CACHE_DIR" fetch -q --depth 1 https://github.com/AccessLint/audit.git "$ACCESSLINT_REF"
  git -C "$CACHE_DIR" -c advice.detachedHead=false checkout -q FETCH_HEAD
fi

READY_MARKER="$CACHE_DIR/.setup-complete"
if [ ! -f "$READY_MARKER" ]; then
  # 'playwright install' is a no-op if the browser is already in
  # PLAYWRIGHT_BROWSERS_PATH. The timeout stops a stalled download or
  # extraction from hanging until the CI job limit.
  (cd "$CACHE_DIR" && npm ci --omit=dev --no-audit --no-fund --silent \
    && timeout 600 npx --yes playwright install --only-shell chromium) >&2
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

env \
  -u GITHUB_STEP_SUMMARY \
  INPUT_URLS="$URLS" \
  INPUT_WCAG-LEVEL="AA" \
  INPUT_FAIL-ON="never" \
  INPUT_MIN-IMPACT="$MIN_IMPACT" \
  "$NODE_BIN" "$CACHE_DIR/dist/index.js" >&2

cat accesslint-report.json
