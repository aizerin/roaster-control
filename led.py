import RPi.GPIO as GPIO
import threading
import time
from singleton import Singleton

bcm_red = 17
bcm_green = 27
bcm_blue = 22


@Singleton
class Led:

    def __init__(self):
        GPIO.setup(bcm_red, GPIO.OUT)
        GPIO.setup(bcm_green, GPIO.OUT)
        GPIO.setup(bcm_blue, GPIO.OUT)
        self.__red = 0
        self.__green = 0
        self.__blue = 0
        self.__run = 0
        self.__pin_stop = threading.Event()
        self.__thread = threading.Thread(target=self.__blinker)
        self.__thread.start()

    def flash_red(self):
        self.__red = 1
        self.__run = 1

    def clean(self):
        self.__pin_stop.set()
        self.__thread.join()

    def __turn_on(self):
        GPIO.output(bcm_red, self.__red)
        GPIO.output(bcm_green, self.__green)
        GPIO.output(bcm_blue, self.__blue)

    def __turn_off(self):
        GPIO.output(bcm_red, 0)
        GPIO.output(bcm_green, 0)
        GPIO.output(bcm_blue, 0)

    def __blinker(self):
        while not self.__pin_stop.is_set():
            if self.__run:
                self.__turn_on()
                time.sleep(0.05)
                self.__turn_off()
                self.__red = 0
                self.__green = 0
                self.__blue = 0
                self.__run = 0
            else:
                self.__turn_off()
