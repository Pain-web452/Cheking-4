#!/bin/bash

echo "🚀 Devil E2EE Bot Setup Starting..."

# Update system
sudo apt-get update
sudo apt-get install -y chromium chromium-chromedriver xvfb python3-pip python3-venv wget curl unzip

# Create symlinks
sudo ln -sf /usr/bin/chromium /usr/bin/chromium-browser
sudo ln -sf /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver

# Set permissions
sudo chmod +x /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromium-browser

# Install Python packages
pip3 install -r requirements.txt

# Verify installations
echo "✅ Installation Verification:"
echo "Chromium: $(chromium-browser --version)"
echo "ChromeDriver: $(chromedriver --version)"
echo "Python: $(python3 --version)"
echo "Pip: $(pip3 --version)"

echo "🎉 Devil E2EE Bot Setup Completed!"
