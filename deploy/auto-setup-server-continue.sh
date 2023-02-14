#!/bin/bash

sudo ln -s /home/ubuntu/blackout/deploy/blackout.service /etc/systemd/system/blackout.service
sudo systemctl daemon-reload
sudo service blackout start

sudo lsof -i :8000

sudo rm -rf /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/default 

cd ~/blackout/deploy
envsubst '$SERVER_IP' < nginx.conf | tee nginx.conf.e
sudo mv nginx.conf.e /etc/nginx/nginx.conf

sudo service nginx restart
