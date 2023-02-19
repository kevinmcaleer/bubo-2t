from bubo.super_servo import Super_Servo
from time import sleep

pan_arm = Super_Servo(0)
s2 = Super_Servo(2)

cal = pan_arm.calibration()
cal.first_value(0)
cal.last_value(180)
pan_arm.calibration(cal)

START_POSITION = 120
END_POSITION = 50

pan_arm.duration_in_seconds = 0.25
# pan_arm.duration_in_seconds = 5
s2.duration_in_seconds = 3


pan_arm.start_angle = START_POSITION
pan_arm.target_angle = END_POSITION

s2.start_angle = START_POSITION
s2.target_angle = END_POSITION
# pan_arm.transition = 'ease_in_circ'
# pan_arm.transition = 'linear_tween'
# pan_arm.transition = 'ease_out_circ'
# pan_arm.transition = 'ease_in_out_circ'
# pan_arm.transition = 'ease_in_back'
# pan_arm.transition = 'ease_out_back'
# pan_arm.transition = 'ease_in_out_back'
# pan_arm.transition = 'ease_in_elastic'
# pan_arm.transition = 'ease_out_elastic'
# pan_arm.transition = 'ease_in_out_elastic'
# pan_arm.transition = 'ease_in_bounce'
# pan_arm.transition = 'ease_out_bounce'
# pan_arm.transition = 'ease_in_out_bounce'
# pan_arm.transition = 'ease_in_sine'
# pan_arm.transition = 'ease_out_sine'
# pan_arm.transition = 'ease_in_out_sine'
# pan_arm.transition = 'ease_in_expo'
# pan_arm.transition = 'ease_out_expo'
# pan_arm.transition = 'ease_in_out_expo'
# pan_arm.transition = 'ease_in_cubic'
# pan_arm.transition = 'ease_out_cubic'
# pan_arm.transition = 'ease_in_out_cubic'
# pan_arm.transition = 'ease_in_quart'
# pan_arm.transition = 'ease_out_quart'
# pan_arm.transition = 'ease_in_out_quart'
# pan_arm.transition = 'ease_in_quad'
# pan_arm.transition = 'ease_out_quad'
# pan_arm.transition = 'ease_in_out_quad'
pan_arm.transition = 'ease_in_quint' # This one works
# pan_arm.transition = 'ease_out_quint'
# pan_arm.transition = 'ease_in_out_quint'
s2.transiton = 'ease_in_out_sine'

s2.angle = 50

pan_arm.tick_start()
s2.tick_start()

pan_arm.show()
print(f'pan_arm.duration = {pan_arm.duration_in_seconds}')
print(f'pan_arm.start_angle = {pan_arm.start_angle}')
print(f'pan_arm.target_angle = {pan_arm.target_angle}')
print(f'pan_elapsed_time_in_seconds = {pan_arm.elapsed_time_in_seconds}')

print(pan_arm.tick())

while not s2.tick():
    pan_arm.tick()
    s2.tick()
pan_arm.show()
print(f"pan_arm.elapsed_time_in_seconds: {pan_arm.elapsed_time_in_seconds}")