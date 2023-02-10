# Bubo-2T the tooting robot
# 2T will take a photo if you do specific hand gestures in front of it
# It will then toot those pictures to mastodon.social

import time
from gpiozero import Servo
from toot_randomiser import TootRandomiser

def Super_Servo(Servo):
    def __init__(self, pin, min_angle, max_angle):
        super().__init__(pin)
        self.min_angle = min_angle
        self.max_angle = max_angle
    
    @property
    def angle(self):
        return self.value * 180

    @angle.setter
    def angle(self, angle):
        if angle < self.min_angle:
            angle = self.min_angle
        elif angle > self.max_angle:
            angle = self.max_angle
        self.value = angle / 180    


GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

class Bubo2t():

    mouth_open = -45 # open
    mouth_close = 45 # closed
    mouth = mouth_close
    eyes_open = -45 # open
    eyes_close = 45 # closed

    # Set GPIO pins for the servos
    left_eye_servo_pin = 11 # GPIO pin
    right_eye_servo_pin = 13 # GPIO pin
    mouth_servo_pin = 15 # GPIO pin

    def __init__(self):
        self.toot_randomiser = TootRandomiser()

        self.left_eye = Super_Servo(self.left_eye_servo_pin)
        self.right_eye = Super_Servo(self.right_eye_servo_pin)
        self.mouth_servo = Super_Servo(self.mouth_servo_pin)
        
    def mouth_open(self):
        """ Open the mouth """

        # Move the servos to different angles
        self.mouth.angle = self.mouth_open
        time.sleep(0.1)

    def mouth_close(self):
        """ Close the mouth """

        self.mouth.angle = self.mouth_close
        time.sleep(0.1)

    def eyes_open(self, speed:None):
        """ Open the eyes """

        self.right_eye.angle = self.eyes_open
        self.left_eye.angle = self.eyes_open
        time.sleep(0.1)

    def eyes_close(self):
        """ Close the eyes """
        
        self.right_eye.angle = self.eyes_close
        self.left_eye.angle = self.eyes_close
        time.sleep(0.1)
    
    def open_left_eye(self):
        """ Open the left eye """
        self.left_eye.angle = self.eyes_open
        time.sleep(0.1)

    def close_left_eye(self):
        """ Close the left eye """
        self.left_eye.angle = self.eyes_close
        time.sleep(0.1)
    
    def open_right_eye(self):
        """ Open the right eye """
        self.right_eye.angle = self.eyes_open
        time.sleep(0.1)

    def close_right_eye(self):
        """ Close the right eye """
        self.right_eye.angle = self.eyes_close
        time.sleep(0.1)
        
    def eyes_colour(self, colour):
        """ Set the colour of the eyes """
        # colour is a tuple of RGB values
        # Set the neopixel strip to the colour using set rgb
        pass
