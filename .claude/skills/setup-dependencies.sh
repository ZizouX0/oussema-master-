#!/usr/bin/env bash
# Install the runtime dependencies the bundled skills need.
#
# Only a handful of the 60 skills ship executable tooling; the rest are pure
# instructions and need nothing. Run this once per machine/container:
#
#   bash .claude/skills/setup-dependencies.sh
#
# Skip sections you don't need — each is independent.

set -euo pipefail

echo "==> System packages (docx/pptx/xlsx/pdf skills)"
# LibreOffice core alone has no import filters; the writer/calc/impress packages
# are what make --convert-to work. pandoc reads .docx, poppler renders PDF pages.
sudo_if_needed() { if [ "$(id -u)" -eq 0 ]; then "$@"; else sudo "$@"; fi; }
sudo_if_needed apt-get update -qq
sudo_if_needed apt-get install -y -qq \
  libreoffice-writer libreoffice-calc libreoffice-impress \
  pandoc poppler-utils

echo "==> Python packages"
# cffi first: a broken system `cryptography` otherwise breaks pypdf imports.
pip3 install --quiet cffi
pip3 install --quiet \
  pillow lxml defusedxml \
  python-docx python-pptx openpyxl markitdown \
  pypdf pdfplumber pdf2image reportlab \
  numpy imageio imageio-ffmpeg

echo "==> mcp-builder (pinned: the scripts target the 1.x MCP SDK)"
pip3 install --quiet -r "$(dirname "$0")/mcp-builder/scripts/requirements.txt"

echo "==> webapp-testing (Playwright)"
# Match the Python package to the browser build already on the machine rather
# than downloading a second copy. In Claude Code web/cloud containers the
# browsers live in PLAYWRIGHT_BROWSERS_PATH and `playwright install` is a no-op
# you should not run; pin the version that matches instead.
pip3 install --quiet playwright
if ! python3 -c "from playwright.sync_api import sync_playwright
with sync_playwright() as p: p.chromium.launch().close()" 2>/dev/null; then
  echo "    installed Playwright build mismatches the local browsers"
  echo "    -> pin to match, e.g. pip3 install 'playwright==1.56.0'"
  echo "    -> or launch with executablePath=/opt/pw-browsers/chromium"
fi

echo "==> Node packages"
npm install -g docx pptxgenjs        # docx / pptx document generation
npm install -g firecrawl-cli@1.19.6  # firecrawl* skills (then: firecrawl login)

echo
echo "Done. Two things still need your own credentials:"
echo "  - firecrawl login            (or export FIRECRAWL_API_KEY=...)"
echo "  - export ANTHROPIC_API_KEY   (skill-creator evals, mcp-builder evaluation)"
