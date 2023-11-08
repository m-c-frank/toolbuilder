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

# Add the install directory to PATH if it's not already there
if ! echo "$PATH" | grep -q "$INSTALL_DIR"; then
    echo "Adding $INSTALL_DIR to PATH"

    # Detect the shell and choose the appropriate profile file
    if [ -n "$BASH_VERSION" ]; then
        PROFILE="$HOME/.bashrc"
        echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> "$PROFILE"
    elif [ -n "$ZSH_VERSION" ]; then
        PROFILE="$HOME/.zshrc"
        echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> "$PROFILE"
    elif [ -n "$FISH_VERSION" ]; then
        # For fish shell, use fish_user_paths universal variable
        fish -c "set -U fish_user_paths $INSTALL_DIR \$fish_user_paths"
    else
        echo "Unknown shell. Please manually add $INSTALL_DIR to your PATH."
        exit 1
    fi

    echo "Please restart your terminal or source your profile to update your PATH."
else
    echo "$INSTALL_DIR is already in PATH"
fi

echo "ToolBuilder installation complete."

