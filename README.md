Tally Lights for Camera Control
===============================

The tally lights are status lights for the cameras that tell the camera operators
when their camera is live. In this configuration, red meanns the camera is live
blue means the camera is being previewed. This is intended to work with our 24
neopixel strip (with 8 pixels per camera). If the strip is yellow, it means
there is a connection issue.

Set up and Running
------------------

The neopixel strip must be plugged into the control Pi and an external 5V converter.
The strip needs to connect to the Pi's GND pin (pin #6) and GPIO18 (pin #12). The
diagram below shows what this looks like:

![Pi pinout and wiring](https://cdn-learn.adafruit.com/assets/assets/000/063/928/original/led_strips_raspi_NeoPixel_powered_bb.jpg)

Running the script is simple; however, you must use sudo permissions in order to allow the Pi to control the GPIO.

```bash
sudo python3 tally-lights.py
```

How it Works
------------

The script connects to Vmix via a TCP socket. Vmix sends a message any time the
output/preview gets updated. The script parses this for the camera statuses and
displays it on the appropriate strip.

