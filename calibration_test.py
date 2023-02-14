from servo import servo2040, Servo
import plasma
from plasma import WS2812
from time import sleep
import math

mouth = Servo(servo2040.SERVO_1)

# cal = mouth.calibration()
# cal.first_value(-10)
# cal.last_value(+40)
# mouth.calibration(cal)

left_eye = Servo(servo2040.SERVO_3)
right_eye = Servo(servo2040.SERVO_2)

val = -40
left_eye.value(val)
right_eye.value(-val)

sleep(1)