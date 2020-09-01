LED Controller
===============

## Setup:

```
$ git clone https://github.com/elliotforbes/led-controller.git

$ sudo crontab -e

# add this line to the bottom of the file
@reboot bash /home/pi/led-controller/startup.sh >/home/pi/led-controller/logs.log 2>&1

$ sudo reboot
```