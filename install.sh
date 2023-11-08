#!/bin/bash
# install.sh
# This script installs ToolBuilder and asks the user for the installation path.

TOOL_NAME="toolbuilder"
REPO_URL="https://github.com/m-c-frank/toolbuilder/raw/main/toolbuilder.sh"

# Ask the user for the installation directory
read -p "Enter the installation directory (default is $HOME/.local/bin): " INSTALL_DIR
INSTALL_DIR=${INSTALL_DIR:-$HOME/.local/bin}

# Create install directory if it doesn't exist
mkdir -p "$INSTALL_DIR"

# Download the toolbuilder script
curl -s "$REPO_URL" -o "$INSTALL_DIR/$TOOL_NAME"

# Make the toolbuilder script executable
chmod +x "$INSTALL_DIR/$TOOL_NAME"

echo "ToolBuilder has been installed to $INSTALL_DIR"
echo "Please ensure that $INSTALL_DIR is in your PATH."

