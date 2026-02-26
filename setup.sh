#!/bin/bash
# Save as setup_crawler.sh → chmod +x → ./setup_crawler.sh

echo "Installing Web Crawler"
sudo apt update
sudo apt install -y python3 python3-pip

pip3 install --user requests beautifulsoup4 lxml urllib3

echo "Ready! then Run: python3 crawler.py"

