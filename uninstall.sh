#!/bin/bash

# MDPDF Uninstall Script
# This script removes the mdpdf alias from your shell configuration

echo "🗑️  Uninstalling MDPDF..."

# Determine shell and config file
SHELL_CONFIG=""
if [ "$SHELL" = "/bin/zsh" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
elif [ "$SHELL" = "/bin/bash" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
else
    echo "⚠️  Warning: Unsupported shell ($SHELL). Please manually remove the alias from your shell config."
    exit 1
fi

# Remove mdpdf alias lines
if [ -f "$SHELL_CONFIG" ]; then
    echo "🔗 Removing mdpdf alias from $SHELL_CONFIG..."
    
    # Create backup
    cp "$SHELL_CONFIG" "$SHELL_CONFIG.backup.$(date +%Y%m%d_%H%M%S)"
    
    # Remove alias lines
    sed -i.bak '/^alias mdpdf=/d' "$SHELL_CONFIG"
    sed -i.bak '/^# MDPDF alias/d' "$SHELL_CONFIG"
    
    echo "✅ MDPDF alias removed from $SHELL_CONFIG"
    echo "📋 Backup created at $SHELL_CONFIG.backup.$(date +%Y%m%d_%H%M%S)"
else
    echo "❌ Shell config file $SHELL_CONFIG not found"
fi

echo ""
echo "To complete the uninstallation, you can also:"
echo "1. Delete the mdpdf directory: rm -rf $(pwd)"
echo "2. Restart your terminal or run: source $SHELL_CONFIG" 