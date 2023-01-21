#!/bin/bash

cd /home/ubuntu/

echo $(date) > blk-keeper-last-run

cd blackout

git fetch

CURR_BRANCH=$(git symbolic-ref --short HEAD)
LOCAL=$(git rev-parse $CURR_BRANCH)
REMOTE=$(git rev-parse origin/$CURR_BRANCH)

if [ $LOCAL != $REMOTE ]; then
  git pull -f
  service blackout restart
else
  echo "No update needed"
fi