#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Ensure correct directory structure and permissions
chmod -R 755 ./portfolio-website

echo "Build completed successfully"
