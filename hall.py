import time
import datetime
import RPi.GPIO as GPIO
from led import Led

bcm_hall = 23


def callback(channel):
    # Called if sensor output changes
    timestamp = time.time()
    stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
    if GPIO.input(channel):
        # No magnet
        print("Sensor HIGH " + stamp)
    else:
        # Magnet
        print("Sensor LOW " + stamp)
        Led.instance().flash_red()


def setup():
    GPIO.setup(bcm_hall, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(bcm_hall, GPIO.BOTH, callback=callback)
