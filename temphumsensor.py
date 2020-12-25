import board
import busio
import adafruit_sht31d
from data import Data

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)


def update():
    Data.instance().humidity = sensor.relative_humidity
    Data.instance().room_temp = sensor.temperature
