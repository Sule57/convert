#!/bin/bash

# Universal File Converter Uninstall Script
# This script removes the convert alias from your shell configuration

echo "🗑️  Uninstalling Universal File Converter..."

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
    echo "⚠️  Warning: Unsupported shell ($SHELL). Please manually remove the alias from your shell config."
    exit 1
fi

# Remove convert alias lines
if [ -f "$SHELL_CONFIG" ]; then
    echo "🔗 Removing convert alias from $SHELL_CONFIG..."
    
    # Create backup
    cp "$SHELL_CONFIG" "$SHELL_CONFIG.backup.$(date +%Y%m%d_%H%M%S)"
    
    # Remove alias lines
    sed -i.bak '/^alias convert=/d' "$SHELL_CONFIG"
    sed -i.bak '/^# Universal File Converter alias/d' "$SHELL_CONFIG"
    
    echo "✅ convert alias removed from $SHELL_CONFIG"
    echo "📋 Backup created at $SHELL_CONFIG.backup.$(date +%Y%m%d_%H%M%S)"
else
    echo "❌ Shell config file $SHELL_CONFIG not found"
fi

echo ""
echo "To complete the uninstallation, you can also:"
echo "1. Delete the converter directory: rm -rf $(pwd)"
echo "2. Restart your terminal or run: source $SHELL_CONFIG" 