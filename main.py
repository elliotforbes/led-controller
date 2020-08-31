import RPi.GPIO as GPIO
from astral import LocationInfo
from astral.sun import sun
from datetime import datetime, timezone
import time

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
    GPIO.setup(18,GPIO.OUT)

    while True:
        t = datetime.now(timezone.utc)

        if s["sunrise"] < t < s["sunset"]:
            print("Time is greater than sunrise but less than sunset")
            GPIO.output(18,GPIO.LOW)
        elif t < s["sunrise"] or t > s["sunset"]:
            GPIO.output(18,GPIO.HIGH)

        time.sleep(60)

if __name__ == "__main__":
    main()