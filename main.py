import RPi.GPIO as GPIO
from astral.sun import sun 
from astral import LocationInfo
from datetime import datetime

def setup_astral():
    city = LocationInfo("London", "England", "Europe/London", 51.5, -0.116)
    return city

def main():
    print("LED Controller Starting...")

    city = setup_astral()
    s = sun(city.observer, date=datetime.now())
    
    print(s["sunrise"])
    print(s["sunset"])

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)

    while True:
        t = datetime.now()

        if sunrise < t < sunset:
            GPIO.output(18, GPIO.HIGH)
        if t < sunrise || t > sunset:
            GPIO.output(18, GPIO.LOW) 

if __name__ == "__main__":
    main

