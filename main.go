package main

import (
	"fmt"
	"time"

	"github.com/nathan-osman/go-sunrise"
	"github.com/stianeikeland/go-rpio/v4"
)

func Get7am(t time.Time) time.Time {
	year, month, day := t.Date()
	return time.Date(year, month, day, 7, 0, 0, 0, t.Location())
}

func main() {

	lightToggle := false

	err := rpio.Open()
	if err != nil {
		fmt.Println(err)
		panic(-1)
	}

	pin := rpio.Pin(2)

	for {

		today := time.Now()

		year, month, day := time.Now().Date()

		_, set := sunrise.SunriseSunset(
			51.5074, 0.1278, // London
			year, month, day,
		)

		// if time after sunset then send half_brightness
		// set light to false
		if time.Now().Sub(set) > 0 {
			if lightToggle == false {
				lightToggle = !lightToggle
				pin.Toggle()
			}
		}

		// if past 7am and less than sunset
		// turn off light
		if Get7am(today).Sub(time.Now()) > 0 && time.Now().Sub(set) < 0 {
			if lightToggle == true {
				lightToggle = !lightToggle
				pin.Toggle()
			}
		}

		time.Sleep(1 * time.Minute)
	}

}
