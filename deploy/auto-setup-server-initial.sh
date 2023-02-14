#!/bin/bash

sudo apt update -y
sudo apt upgrade -y

sudo apt install -y git python3 python3-pip python3-venv nginx

curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -
sudo apt install -y nodejs

cd ~

python3 -m venv venv
. venv/bin/activate

cd blackout
git checkout deploy-ready

sudo /home/ubuntu/venv/bin/pip3 install gevent
pip3 install -r ~/blackout/blackout/requirements.txt

sudo /bin/bash -c "cat ~/blackout/deploy/bashrc-server-ip-environment >> ~/.bashrc"

sudo reboot
