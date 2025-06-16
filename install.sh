#!/bin/bash

# Universal File Converter Installation Script
# This script installs the convert tool dependencies

set -e  # Exit on any error

echo "🚀 Installing Universal File Converter..."

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if we're in the right directory
if [ ! -f "$SCRIPT_DIR/convert.py" ]; then
    echo "❌ Error: convert.py not found in current directory"
    echo "Please run this script from the converter directory"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "$SCRIPT_DIR/venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv "$SCRIPT_DIR/venv"
fi

# Install dependencies using the virtual environment's pip directly
echo "📥 Installing Python dependencies..."
"$SCRIPT_DIR/venv/bin/pip" install -r "$SCRIPT_DIR/requirements.txt"

echo "✅ Installation complete!"
echo ""
echo "Next steps:"
echo "1. Set up the alias in your shell configuration (see README.md for instructions)"
echo "2. Restart your terminal or reload your shell configuration"
echo ""
echo "Example usage after setting up the alias:"
echo "  # Markdown to PDF"
echo "  convert -f input.md -t pdf"
echo "  convert -f input.md -t pdf -o output.pdf"
echo "  convert -f input.md -o output.pdf"
echo ""
echo "  # Image format conversion"
echo "  convert -f image.png -t jpg"
echo "  convert -f image.png -t jpg -o new_image.jpg"
echo "  convert -f image.png -o new_image.jpg"
echo "  convert -f logo.svg -t png -o logo.png" 