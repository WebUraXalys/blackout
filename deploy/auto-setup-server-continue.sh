#!/bin/bash

sudo ln -s /home/ubuntu/blackout/deploy/blackout.service /etc/systemd/system/blackout.service
sudo systemctl daemon-reload
sudo service blackout start

sudo lsof -i :8000

sudo rm -rf /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/default 

envsubst '$SERVER_IP' < /home/ubuntu/blackout/deploy/nginx.conf > /etc/nginx/nginx.conf

sudo service nginx restart
