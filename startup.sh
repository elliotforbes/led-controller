#!/bin/bash -e

echo "Starting LED Controller"

cd /home/pi/led-controller
pwd

/usr/bin/python3 -m pip install -r requirements.txt

echo "Starting script"
/usr/bin/python3 main.py > logs.log 2>&1 &