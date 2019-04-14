#!/bin/sh

remote_loc="pi@192.168.0.103:/home/pi/ros2_walkaround"
#rsync -azv --delete .  --exclude='./.git' --filter="dir-merge,- .gitignore"

fswatch -0 -o -e .git/ -e .pyc -e $(pwd)/static . | \
xargs -0 -I {} rsync -avz -e "ssh" . $remote_loc --exclude='.git' --filter="dir-merge,- .gitignore"