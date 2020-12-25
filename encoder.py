import math
import threading
import RPi.GPIO as GPIO

class RotaryEncoder:

    def __init__(self):
        self.a_pin = 17
        self.b_pin = 27
        self.lokE = threading.Lock()

        GPIO.setup(self.a_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.b_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self.steps = 0
        self.last_delta = 0
        self.r_seq = self.rotation_sequence()

        self.steps_per_cycle = 4
        self.remainder = 0

    def rotation_sequence(self):
        a_state = GPIO.input(self.a_pin)
        b_state = GPIO.input(self.b_pin)
        r_seq = (a_state ^ b_state) | b_state << 1
        return r_seq

    def update(self):
        delta = 0
        r_seq = self.rotation_sequence()
        if r_seq != self.r_seq:
            delta = (r_seq - self.r_seq) % 4
            if delta == 3:
                delta = -1
            elif delta == 2:
                delta = int(math.copysign(delta, self.last_delta))  # same direction as previous, 2 steps

            self.last_delta = delta
            self.r_seq = r_seq
        self.lokE.acquire()
        self.steps += delta
        self.lokE.release()

    def get_steps(self):
        self.lokE.acquire()
        steps = self.steps
        self.steps = 0
        self.lokE.release()
        return steps

    def get_cycles(self):
        self.remainder += self.get_steps()
        cycles = self.remainder // self.steps_per_cycle
        self.remainder %= self.steps_per_cycle  # remainder always remains positive
        return cycles

    def start(self):
        def isr(arg):
            self.update()

        GPIO.add_event_detect(self.a_pin, GPIO.BOTH, callback=isr)
        GPIO.add_event_detect(self.b_pin, GPIO.BOTH, callback=isr)
