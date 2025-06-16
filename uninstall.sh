#!/bin/bash

# Universal File Converter Uninstall Script
# This script provides instructions for uninstalling the convert tool

echo "🗑️  Uninstalling Universal File Converter..."

echo "To completely uninstall the convert tool:"
echo ""
echo "1. Remove the alias from your shell configuration:"
echo "   - For zsh: Remove the convert alias from ~/.zshrc"
echo "   - For bash on macOS: Remove the convert alias from ~/.bash_profile"
echo "   - For bash on Linux: Remove the convert alias from ~/.bashrc"
echo "   - For PowerShell: Remove the convert function from your PowerShell profile"
echo ""
echo "2. Delete the converter directory:"
echo "   rm -rf $(pwd)"
echo ""
echo "3. Restart your terminal or reload your shell configuration"
echo ""
echo "Note: The install script no longer automatically manages aliases."
echo "You'll need to manually remove any aliases you added." 