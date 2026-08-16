#!/bin/bash
set -e

echo "📦 Bundling React app to single HTML artifact..."

# Check if we're in a project directory
if [ ! -f "package.json" ]; then
  echo "❌ Error: No package.json found. Run this script from your project root."
  exit 1
fi

# Check if index.html exists
if [ ! -f "index.html" ]; then
  echo "❌ Error: No index.html found in project root."
  echo "   This script requires an index.html entry point."
  exit 1
fi

# Install bundling dependencies
echo "📦 Installing bundling dependencies..."
pnpm add -D parcel @parcel/config-default parcel-resolver-tspaths html-inline

# Create Parcel config with tspaths resolver
if [ ! -f ".parcelrc" ]; then
  echo "🔧 Creating Parcel configuration with path alias support..."
  cat > .parcelrc << 'EOF'
{
  "extends": "@parcel/config-default",
  "resolvers": ["parcel-resolver-tspaths", "..."]
}
EOF
fi

# Clean previous build
echo "🧹 Cleaning previous build..."
rm -rf dist bundle.html

# Parcel resolves root-absolute hrefs from the project root, while Vite serves
# them from public/. Drop the favicon link for the build so Parcel doesn't fail
# on it, then restore index.html afterwards.
BUNDLE_INDEX_BACKUP=""
if grep -q '<link[^>]*rel="icon"' index.html; then
  echo "🔧 Removing public/ favicon link for the Parcel build..."
  BUNDLE_INDEX_BACKUP=$(mktemp)
  cp index.html "$BUNDLE_INDEX_BACKUP"
  trap 'if [ -n "$BUNDLE_INDEX_BACKUP" ]; then cp "$BUNDLE_INDEX_BACKUP" index.html; rm -f "$BUNDLE_INDEX_BACKUP"; fi' EXIT
  sed -i '/<link[^>]*rel="icon"/d' index.html
fi

# Build with Parcel
echo "🔨 Building with Parcel..."
pnpm exec parcel build index.html --dist-dir dist --no-source-maps

# Inline everything into single HTML
echo "🎯 Inlining all assets into single HTML file..."
pnpm exec html-inline dist/index.html > bundle.html

# Get file size
FILE_SIZE=$(du -h bundle.html | cut -f1)

echo ""
echo "✅ Bundle complete!"
echo "📄 Output: bundle.html ($FILE_SIZE)"
echo ""
echo "You can now use this single HTML file as an artifact in Claude conversations."
echo "To test locally: open bundle.html in your browser"