#!/bin/bash

# Universal File Converter Installation Script
# This script properly installs the convert tool and creates a persistent alias

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

# Determine shell and config file
SHELL_CONFIG=""
if [ "$SHELL" = "/bin/zsh" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
elif [ "$SHELL" = "/bin/bash" ]; then
    # On macOS, bash typically uses .bash_profile instead of .bashrc
    if [[ "$OSTYPE" == "darwin"* ]]; then
        SHELL_CONFIG="$HOME/.bash_profile"
    else
        SHELL_CONFIG="$HOME/.bashrc"
    fi
else
    echo "⚠️  Warning: Unsupported shell ($SHELL). Please manually add the alias to your shell config."
    echo "Add this line to your shell config file:"
    echo "alias convert='$SCRIPT_DIR/venv/bin/python3 $SCRIPT_DIR/convert.py'"
    exit 0
fi

# Remove any existing convert alias
if [ -f "$SHELL_CONFIG" ]; then
    # Remove existing convert alias lines
    sed -i.bak '/^alias convert=/d' "$SHELL_CONFIG" 2>/dev/null || true
    sed -i.bak '/^# Universal File Converter alias/d' "$SHELL_CONFIG" 2>/dev/null || true
fi

# Add the new alias
echo "🔗 Adding convert alias to $SHELL_CONFIG..."
echo "" >> "$SHELL_CONFIG"
echo "# Universal File Converter alias - added by install script" >> "$SHELL_CONFIG"
echo "alias convert='$SCRIPT_DIR/venv/bin/python3 $SCRIPT_DIR/convert.py'" >> "$SHELL_CONFIG"

# Reload shell config
echo "🔄 Reloading shell configuration..."
if [ "$SHELL" = "/bin/zsh" ]; then
    source "$SHELL_CONFIG"
elif [ "$SHELL" = "/bin/bash" ]; then
    source "$SHELL_CONFIG"
fi

echo "✅ Installation complete!"
echo ""
echo "You can now use convert from anywhere:"
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
echo ""
echo "If the command doesn't work immediately, please restart your terminal or run:"
echo "  source $SHELL_CONFIG" 