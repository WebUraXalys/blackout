# Server setup guide

System and network requirements:
- Ubuntu 18.04 LTS
- Public static IP address

### Prepeare system:
#### 1. Upgrade system packages
```sh
sudo apt update
sudo apt upgrade
```
#### 2. Install software dependencies
```sh
sudo apt install git python3 python3-pip nginx
```
#### 3. Install NodeJS v14
```sh
curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -
sudo apt install nodejs
```

### Set up gunicorn server
#### 1. Clone the codebase
```sh
cd ~
git clone https://github.com/WebUraXalys/blackout.git
```
#### 2. Select the desired branch
```sh
git switch <DESIRED BRANCH>
```
#### 3. Set up the virtual environment
```
python3 -m venv venv
./venv/bin/activate
```
#### 4. Install Python requirements
```sh
pip3 install -r ~/blackout/blackout/requirements.txt
```
#### 5. Set up SERVER_IP environment variable
```sh
echo < ~/blackout/deploy/bashrc-server-ip-environment >> ~/.bashrc
```
#### 6. Set up and run blackout app service
```sh 
sudo ln -s /home/ubuntu/blackout/deploy/blackout.service /etc/systemd/system/blackout.service
sudo systemctl daemon-reload
sudo service blackout start
```
#### 7. Check server started
```sh
sudo lsof -i :8000
```
Output should be like this (PID, DEVICE and FD may differ):
```
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
python3 29853 root    5u  IPv4  61322      0t0  TCP localhost:8000 (LISTEN)
python3 29864 root    5u  IPv4  61322      0t0  TCP localhost:8000 (LISTEN)
python3 29865 root    5u  IPv4  61322      0t0  TCP localhost:8000 (LISTEN)
python3 29869 root    5u  IPv4  61322      0t0  TCP localhost:8000 (LISTEN)
```

### Set up Nginx server
#### 1. Remove unnecessary configs
```sh
sudo rm -rf /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-enabled/default 
```
#### 2. Install nginx.conf
```sh
sudo ln -sf /home/ubuntu/blackot/deploy/nginx.conf /etc/nginx/nginx.conf
```
#### 3. Restart Nginx service
```sh
sudo service nginx restart
```
The website should appear on server's public IP at 80 port.


### How-to update app version manually
#### 1. Update codebase
```sh
cd ~/blackout
git pull
```
#### 2. Restart app server
```sh
sudo service blackout restart
```

### Set-up auto-deploy script
#### 1. Insert update-checking script task into crontab.

To do so, firstly open crontab with the following command:
```sh
sudo crontab -e
```
At the first run crontab might ask you to choose a preffered text editor.

Then, insert following into the crontab:
```crontab
*/5 * * * * /bin/bash /home/ubuntu/blackout/deploy/blackout-keeper.sh
```
#### 2. Check it works
Run script as a superuser:
```sh
sudo sh /home/ubuntu/blackout/deploy/blackout-keeper.sh
```
Check script was runned:
```sh
cat ~/blk-keeper-last-run
```
Output should be like this (not strictly the same):
```
Sat Jan 21 19:20:01 UTC 2023
```