#!/usr/bin/env bash
# The script sets up webservers for deployment of web_static

# this installs Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi
# this creates the necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# thos creates a fake HTML file
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# this creates or update the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# this gives ownership of /data/ to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# this updates Nginx configuration to serve the content
config_file="/etc/nginx/sites-available/default"
config_content="location /hbnb_static/ {\n    alias /data/web_static/current/;\n}\n"
sudo sed -i "/location \/ {/ a $config_content" "$config_file"

# Restarts Nginx
sudo service nginx restart

exit 0

