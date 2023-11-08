#!/bin/bash
# install.sh
# This script installs ToolBuilder to the user's local bin directory.

TOOL_NAME="toolbuilder"
INSTALL_DIR="$HOME/.local/bin"
REPO_URL="https://raw.githubusercontent.com/m-c-frank/toolbuilder/main/toolbuilder.sh"

# Create install directory if it doesn't exist
mkdir -p "$INSTALL_DIR"

# Download the toolbuilder script
curl -s "$REPO_URL" -o "$INSTALL_DIR/$TOOL_NAME"

# Make the toolbuilder script executable
chmod +x "$INSTALL_DIR/$TOOL_NAME"

# Check if the install directory is in PATH
if ! echo "$PATH" | grep -q "$INSTALL_DIR"; then
    # Add the install directory to PATH
    echo "Adding $INSTALL_DIR to PATH"
    
    # Detect profile file based on current shell
    if [ -n "$BASH_VERSION" ]; then
        PROFILE="$HOME/.bashrc"
    elif [ -n "$ZSH_VERSION" ]; then
        PROFILE="$HOME/.zshrc"
    elif [ -n "$FISH_VERSION" ]; then
        PROFILE="$HOME/.config/fish/config.fish"
        echo "set -U fish_user_paths $INSTALL_DIR \$fish_user_paths" >> "$PROFILE"
    else
        echo "Unknown shell. Please manually add $INSTALL_DIR to your PATH."
        exit 1
    fi

    # For bash and zsh, update the profile file
    if [ -z "$FISH_VERSION" ]; then
        echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> "$PROFILE"
    fi

    echo "Please restart your terminal or source your profile to update your PATH."
fi

echo "ToolBuilder installation complete."

