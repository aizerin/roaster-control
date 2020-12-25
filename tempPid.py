import RPi.GPIO as GPIO
import time
from data import Data

sck = 21
so = 19
unit = 1
cs = 6
GPIO.setup(cs, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(sck, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(so, GPIO.IN)


def update():
    GPIO.output(cs, GPIO.LOW)
    time.sleep(0.002)
    GPIO.output(cs, GPIO.HIGH)
    time.sleep(0.22)

    GPIO.output(cs, GPIO.LOW)
    GPIO.output(sck, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(sck, GPIO.LOW)
    Value = 0
    for i in range(11, -1, -1):
        GPIO.output(sck, GPIO.HIGH)
        Value = Value + (GPIO.input(so) * (2 ** i))
        GPIO.output(sck, GPIO.LOW)

    GPIO.output(sck, GPIO.HIGH)
    error_tc = GPIO.input(so)
    GPIO.output(sck, GPIO.LOW)

    for i in range(2):
        GPIO.output(sck, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(sck, GPIO.LOW)

    GPIO.output(cs, GPIO.HIGH)

    temp = Value * 0.25
    Data.instance().pid_temp = temp