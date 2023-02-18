# Bubo-2T the tooting robot
# 2T will take a photo if you do specific hand gestures in front of it
# It will then toot those pictures to mastodon.social

from time import sleep
# from gpiozero import Servo
from .toot_randomiser import RandomToots
from .super_servo import Super_Servo
from servo import servo2040
import plasma
from plasma import WS2812
import math

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Set GPIO pins for the servos
LEFT_EYE_PIN = servo2040.SERVO_3  # GPIO pin
RIGHT_EYE_PIN = servo2040.SERVO_2 # GPIO pin
MOUTH_PIN = servo2040.SERVO_1     # GPIO pin

# Calibration allows us to limit the angle of the servo between and upper and lower value
# We need to provide the lower pulse width, upper pulse width and the lower and upper angles
MOUTH_MIN_PULSE = 1000
MOUTH_MAX_PULSE = 2000
MOUTH_MIN_ANGLE = -45
MOUTH_MAX_ANGLE = 45

EYE_MIN_PULSE = 1000
EYE_MAX_PULSE = 2000
EYE_MIN_ANGLE = -30
EYE_MAX_ANGLE = 14

class Bubo2t():
    __mouth_open = MOUTH_MIN_ANGLE # open
    __mouth_close = MOUTH_MAX_ANGLE # closed
    __eyes_open =  EYE_MIN_ANGLE # open
    __eyes_close = EYE_MAX_ANGLE # closed

    def __init__(self, left_eye_pin=LEFT_EYE_PIN, right_eye_pin=RIGHT_EYE_PIN, mouth_pin=MOUTH_PIN):
        self.toot_randomiser = RandomToots()

        # Setup the Servos
        self.left_eye = Super_Servo(left_eye_pin)
        self.right_eye = Super_Servo(right_eye_pin)
        self.mouth = Super_Servo(mouth_pin)
        self.left_eye.name = "Left Eye"
        self.right_eye.name = "Right Eye"
        self.mouth.name = "Mouth"
        
        print('Bubo2t init')
        print(f'mouth pin = {self.mouth.pin()}')
        print(f'left eye pin = {self.left_eye.pin()}')
        print(f'right eye pin = {self.right_eye.pin()}')
        self.left_eye.value(0)
        self.right_eye.value(0)
        self.mouth.value(0)
        print('-'*10)

        # Apply the calibration to Mouth, Left Eye and Right Eye
        mouth_cal = self.mouth.calibration()
        mouth_cal.apply_two_pairs(MOUTH_MIN_PULSE, MOUTH_MAX_PULSE, MOUTH_MIN_ANGLE, MOUTH_MAX_ANGLE)
        self.mouth.calibration(mouth_cal)

        eye_cal = self.left_eye.calibration()
        eye_cal.apply_two_pairs(EYE_MIN_PULSE, EYE_MAX_PULSE, EYE_MIN_ANGLE, EYE_MAX_ANGLE)
        self.left_eye.calibration(eye_cal)

        eye_cal = self.right_eye.calibration()
        eye_cal.apply_two_pairs(EYE_MIN_PULSE, EYE_MAX_PULSE, EYE_MIN_ANGLE, EYE_MAX_ANGLE)
        self.right_eye.calibration(eye_cal)
        
    def tick(self):
        """ Perform a tick """
        # print('tick')

        # TODO check for new action

        if (not self.left_eye.tick()) or (not self.right_eye.tick()) or (not self.mouth.tick()):
            self.left_eye.tick()
            self.right_eye.tick()
            self.mouth.tick()
            return False
        else:
            return True
        
    def blink(self, duration):
        "blink eyes"

        self.left_eye.transition = 'ease_in_sine'
        self.right_eye.transition = 'ease_in_sine'
        self.left_eye.duration_in_seconds = duration
        self.right_eye.duration_in_seconds = duration

        self.left_eye.target_angle = - self.__eyes_close
        self.right_eye.target_angle = self.__eyes_close
        self.left_eye.change_in_angle = self.left_eye.target_angle - self.left_eye.start_angle
        self.right_eye.change_in_angle = self.right_eye.target_angle - self.right_eye.start_angle

        self.left_eye.tick_start()
        self.right_eye.tick_start()
        sleep(0.1)

    def mouth_open(self):
        """ Open the mouth """

        print('mouth_open')

        # Move the servos to different angles
        from_val = self.mouth.value()
        val = self.__mouth_open
        print(f'moving mouth from {from_val} to {val}')
        self.mouth.value(val)
        sleep(0.1)

    def mouth_close(self):
        """ Close the mouth """

        print('mouth_close')

        # Move the servos to different angles
        from_val = float(self.mouth.value())
        val = float(self.__mouth_close)
        print(f'moving mouth from {from_val} to {val}')
        self.mouth.value(val)
        sleep(0.1)

    def eyes_open(self, duration):
        """ Open the eyes """

        "open eyes"

        self.left_eye.transition = 'ease_in_sine'
        self.right_eye.transition = 'ease_in_sine'
        self.left_eye.duration_in_seconds = duration
        self.right_eye.duration_in_seconds = duration

        self.left_eye.target_angle = - self.__eyes_open
        self.right_eye.target_angle = self.__eyes_open
        self.left_eye.change_in_value = self.left_eye.target_angle - self.left_eye.current_angle
        self.right_eye.change_in_value = self.right_eye.target_angle - self.right_eye.current_angle

        self.left_eye.tick_start()
        self.right_eye.tick_start()
        # sleep(0.1)

    def eyes_close(self, duration):
        """ Close the eyes """
        
        "close eyes"

        self.left_eye.transition = 'ease_in_sine'
        self.right_eye.transition = 'ease_in_sine'
        self.left_eye.duration_in_seconds = duration
        self.right_eye.duration_in_seconds = duration

        self.left_eye.target_angle = - self.__eyes_close
        self.right_eye.target_angle = self.__eyes_close
        self.left_eye.change_in_value = self.left_eye.target_angle - self.left_eye.current_angle
        self.right_eye.change_in_value = self.right_eye.target_angle - self.right_eye.current_angle

        self.left_eye.tick_start()
        self.right_eye.tick_start()
        # sleep(0.1)
    
    def open_left_eye(self):
        """ Open the left eye """
        self.left_eye.value(self.__eyes_open)
        sleep(0.1)

    def close_left_eye(self):
        """ Close the left eye """
        self.left_eye.value(self.__eyes_close)
        sleep(0.1)
    
    def open_right_eye(self):
        """ Open the right eye """
        self.right_eye.value(self.__eyes_open)
        sleep(0.1)

    def close_right_eye(self):
        """ Close the right eye """
        self.right_eye.value(self.__eyes_close)
        sleep(0.1)
        
    def eyes_colour(self, colour):
        """ Set the colour of the eyes """
        # colour is a tuple of RGB values
        # Set the neopixel strip to the colour using set rgb
        pass
