#!/bin/bash

/bin/bash rebuild-app.sh

cd /home/ubuntu/blackout/blackout
python3 -m gunicorn --access-logfile - --workers 3 --bind 127.0.0.1:8000 blackout.wsgi
