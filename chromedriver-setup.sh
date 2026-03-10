#!/bin/bash

echo "🔧 Setting up ChromeDriver for Prince E2EE Bot..."

# Install Chromium and ChromeDriver
sudo apt-get update
sudo apt-get install -y chromium chromium-chromedriver

# Create symlinks
sudo ln -sf /usr/bin/chromium /usr/bin/chromium-browser
sudo ln -sf /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver

# Set permissions
sudo chmod +x /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromium-browser

# Verify installation
echo "✅ Chromium version:"
chromium-browser --version
echo "✅ ChromeDriver version:"
chromedriver --version

echo "🎉 ChromeDriver setup completed!"
