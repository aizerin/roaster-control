from singleton import Singleton


@Singleton
class Data:

    def __init__(self):
        self.__battery = 0
        self.__room_temp = 0
        self.__humidity = 0
        self.__bean_temp = 0
        self.__drum_temp = 0
        self.__pid_temp = 0
        self.__heater_power = 12
        self.__heater_power_perc = 100

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    @property
    def room_temp(self):
        return self.__room_temp

    @room_temp.setter
    def room_temp(self, value):
        self.__room_temp = value

    @property
    def humidity(self):
        return self.__humidity

    @humidity.setter
    def humidity(self, value):
        self.__humidity = value

    @property
    def bean_temp(self):
        return self.__bean_temp

    @bean_temp.setter
    def bean_temp(self, value):
        self.__bean_temp = value

    @property
    def drum_temp(self):
        return self.__drum_temp

    @drum_temp.setter
    def drum_temp(self, value):
        self.__drum_temp = value

    @property
    def pid_temp(self):
        return self.__pid_temp

    @pid_temp.setter
    def pid_temp(self, value):
        self.__pid_temp = value

    @property
    def heater_power(self):
        return self.__heater_power

    @heater_power.setter
    def heater_power(self, value):
        self.__heater_power = value

    @property
    def heater_power_perc(self):
        return self.__heater_power_perc

    @heater_power_perc.setter
    def heater_power_perc(self, value):
        self.__heater_power_perc = value
