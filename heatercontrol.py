import encoder
from data import Data
import RPi.GPIO as GPIO

test_encoder = encoder.RotaryEncoder()
test_encoder.start()

hemax = 12
hemin = 0
powval = 12

HEATER_GPIO = 26
PWM_FREQUENCY = 8.333

GPIO.setmode(GPIO.BCM)
GPIO.setup(HEATER_GPIO, GPIO.OUT)
heater = GPIO.PWM(HEATER_GPIO, PWM_FREQUENCY)
heater.start(0)
heater.ChangeDutyCycle(100)


def update():
    global powval
    delta = test_encoder.get_cycles()
    if delta != 0:
        # compute new power value
        powval = powval + delta
        if powval > hemax:
            powval = hemax
        if powval < hemin:
            powval = hemin
        # translate to percent
        percent = (powval * 100) / hemax
        Data.instance().heater_power = powval
        Data.instance().heater_power_perc = percent
        heater.ChangeDutyCycle(percent)
