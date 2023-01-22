#!/bin/bash

# Migrate backend
cd /home/ubuntu/blackout/blackout
python3 manage.py migrate

# Build frontend
cd ../frontend
npm i
npm run build
