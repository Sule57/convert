#!/bin/bash

# MDPDF Installation Script
# This script properly installs mdpdf and creates a persistent alias

set -e  # Exit on any error

echo "🚀 Installing MDPDF..."

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if we're in the right directory
if [ ! -f "$SCRIPT_DIR/mdpdf.py" ]; then
    echo "❌ Error: mdpdf.py not found in current directory"
    echo "Please run this script from the mdpdf directory"
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

# Determine shell and config file
SHELL_CONFIG=""
if [ "$SHELL" = "/bin/zsh" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
elif [ "$SHELL" = "/bin/bash" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
else
    echo "⚠️  Warning: Unsupported shell ($SHELL). Please manually add the alias to your shell config."
    echo "Add this line to your shell config file:"
    echo "alias mdpdf='$SCRIPT_DIR/venv/bin/python3 $SCRIPT_DIR/mdpdf.py'"
    exit 0
fi

# Remove any existing mdpdf alias
if [ -f "$SHELL_CONFIG" ]; then
    # Remove existing mdpdf alias lines
    sed -i.bak '/^alias mdpdf=/d' "$SHELL_CONFIG" 2>/dev/null || true
    sed -i.bak '/^# MDPDF alias/d' "$SHELL_CONFIG" 2>/dev/null || true
fi

# Add the new alias
echo "🔗 Adding mdpdf alias to $SHELL_CONFIG..."
echo "" >> "$SHELL_CONFIG"
echo "# MDPDF alias - added by install script" >> "$SHELL_CONFIG"
echo "alias mdpdf='$SCRIPT_DIR/venv/bin/python3 $SCRIPT_DIR/mdpdf.py'" >> "$SHELL_CONFIG"

# Reload shell config
echo "🔄 Reloading shell configuration..."
if [ "$SHELL" = "/bin/zsh" ]; then
    source "$SHELL_CONFIG"
elif [ "$SHELL" = "/bin/bash" ]; then
    source "$SHELL_CONFIG"
fi

echo "✅ Installation complete!"
echo ""
echo "You can now use mdpdf from anywhere:"
echo "  mdpdf \"Your markdown text here\""
echo "  mdpdf -f input.md"
echo "  mdpdf -f input.md -o output.pdf"
echo ""
echo "If the command doesn't work immediately, please restart your terminal or run:"
echo "  source $SHELL_CONFIG" 