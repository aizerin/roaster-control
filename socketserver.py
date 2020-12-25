import threading
import socket
from data import Data

# server values
HOST = ''  # Symbolic name meaning all available interfaces
PORT = 60016  # Arbitrary non-privileged port


class SocketServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._stopevent = threading.Event()
        self.socket = 0
        self.conn = 0

    def run(self):
        print("thread Server is ready!")

        # -------- Program Loop 1 -----------
        while not self._stopevent.isSet():
            self.socket = 0
            print("TaskServer loop1 - start server")
            # listen to socket
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.socket.bind((HOST, PORT))
                self.socket.listen(1)
                break
            except socket.error as e:
                print("TaskServer loop1 - Socket error : {0}".format(e))
                if self.socket != 0:
                    self.socket.close()
            # wait 1 second before new attempt
            self._stopevent.wait(1)

        # --------  Program Loop 2 -----------
        while not self._stopevent.isSet():
            self.conn = 0

            try:
                self.conn, addr = self.socket.accept()
                print('TaskServer loop2 - connected by', addr)
                data = Data.instance()
                data = str(data.drum_temp) + ',' + str(data.bean_temp) + ',' + str(
                    data.pid_temp) + ',' + f'{Data.instance().heater_power_perc:.0f}'
                self.conn.sendall(data.encode())

            except socket.error as e:
                print("TaskServer loop2 - Socket error : {0}".format(e))
            finally:
                if self.conn != 0:
                    # print "TaskServer loop2 - close socket"
                    self.conn.close()

    def stop(self):
        print("stopping thread Server")
        self._stopevent.set()
        if self.conn != 0:
            self.conn.close()
            print("connection closed")
        if self.socket != 0:
            self.socket.close()
            print("socket closed")
