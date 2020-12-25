import threading
from singleton import Singleton
import time
from data import Data
from board import SCL, SDA
import busio
from oled_text import OledText

@Singleton
class Display:

    def __init__(self):
        i2c = busio.I2C(SCL, SDA)
        self.__oled = OledText(i2c, 128, 64)
        self.__oled.auto_show = False

        self.__pin_stop = threading.Event()
        self.__thread = threading.Thread(target=self.__draw)
        self.__thread.start()

    def clear_screen(self):
        self.__oled.clear()

    def __draw(self):
        while not self.__pin_stop.is_set():
            self.__oled.text(f'Battery {Data.instance().battery:d}%', 1)
            self.__oled.text(f'BT:{Data.instance().bean_temp:.0f}°', 2)
            self.__oled.text(f'ET:{Data.instance().drum_temp:.0f}°', 3)
            self.__oled.text(f'PID°C:{Data.instance().pid_temp:.0f}°', 4)
            self.__oled.text(f'MOT:%{Data.instance().heater_power_perc:.0f}', 5)
            self.__oled.show()
            time.sleep(1)
