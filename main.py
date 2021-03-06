import RPi.GPIO as GPIO
from datetime import datetime, timezone
import time
from suntime import Sun, SunTimeException

latitude = 51.5074
longitude = 0.1278

def main():
    print("LED Controller Starting...")

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    GPIO.output(18,GPIO.HIGH)
    while True:

        sun = Sun(latitude, longitude)
        sunrise = sun.get_sunrise_time()
        sunset = sun.get_sunset_time()
        print(sunrise)
        print(sunset)

        t = datetime.now(timezone.utc)
        print(t)

        seven_am = datetime.now(timezone.utc).replace(hour=6,minute=0,second=0,microsecond=0)
        if seven_am < t < sunset:
            print("Time is greater than sunrise but less than sunset")
            GPIO.output(18,GPIO.HIGH)
        else:
            print("Before Sunrise or after Sunset")
            GPIO.output(18,GPIO.LOW)

        time.sleep(60)

if __name__ == "__main__":
    main()