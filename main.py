import time
import sys
import RPi.GPIO as GPIO

from display import Display
import mqtt
import socketserver
import tempPid
import heatercontrol

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

mqtt.setup()

socket_server = socketserver.SocketServer()
socket_server.start()


def quit_application():
    print("Exitting")
    Display.instance().clear_screen()
    GPIO.cleanup()
    socket_server.stop()
    sys.exit(0)


Display.instance()

def main():
    try:
        while True:
            tempPid.update()
            heatercontrol.update()
            time.sleep(0.1)

    except KeyboardInterrupt:
        # Reset GPIO settings
        quit_application()


main()
