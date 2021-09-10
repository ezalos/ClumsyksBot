import RPi.GPIO as GPIO
from time import sleep

# 0/1 used to signify clockwise or counterclockwise.
CW = 1
CCW = 0

class Nema():
        QUARTER_STEPS = 200
        def __init__(self):
                # Direction pin from controller
                self.pin_dir = 10
                # Step pin from controller
                self.pin_step = 8
                self.__direction = None
                # Setup pin layout on PI
                GPIO.setmode(GPIO.BOARD)
                # Establish Pins in software
                GPIO.setup(self.pin_dir, GPIO.OUT)
                GPIO.setup(self.pin_step, GPIO.OUT)
                print("Nema initialized pi pins")

        @property
        def direction(self):
                return self.__direction

        @direction.setter
        def direction(self, direction):
                if self.__direction != direction:
                        GPIO.output(self.pin_dir, direction)
                        self.__direction = direction

        def turn(self, direction, nb_quarters=1, sleep_time=.0001):
                self.direction = direction
                print(f"Doing {nb_quarters}/4 ", end="")
                for _ in range(Nema.QUARTER_STEPS * nb_quarters):
                    GPIO.output(self.pin_step,GPIO.HIGH)
                    sleep(sleep_time)
                    GPIO.output(self.pin_step,GPIO.LOW)
                    sleep(sleep_time)
                print("turns!")

        def __delete__(self):
            GPIO.cleanup()


def absolute_turn(n, q_turns, direction, time):
    n.turn(direction, nb_quarters=q_turns, sleep_time=(time / q_turns))

if __name__ == "__main__":
        n = Nema()
        while True:
                break
                n.turn(CW, 1, 0.001)
                n.turn(CCW, 2, 0.002)
                n.turn(CW, 3, 0.003)
                n.turn(CCW, 4, 0.004)
        
        while True:
            for q_t in range(1, 5):
                direction = q_t % 2
                absolute_turn(n, q_t, direction, 1e-9)

