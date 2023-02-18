from bubo.super_servo import Super_Servo
from time import sleep

pan_arm = Super_Servo(0)
s2 = Super_Servo(2)

cal = pan_arm.calibration()
cal.first_value(0)
cal.last_value(180)
pan_arm.calibration(cal)

START_POSITION = 0
END_POSITION = 180

pan_arm.duration_in_seconds = 5
pan_arm.start_angle = START_POSITION
pan_arm.target_angle = END_POSITION

pan_arm.transition = 'ease_in_circ'
# pan_arm.transition = 'linear_tween'
# pan_arm.transition = 'ease_out_circ'
# pan_arm.transition = 'ease_in_out_circ'

pan_arm.tick_start()
pan_arm.show()
print(f'pan_arm.duration = {pan_arm.duration_in_seconds}')
print(f'pan_arm.start_angle = {pan_arm.start_angle}')
print(f'pan_arm.target_angle = {pan_arm.target_angle}')
print(f'pan_elapsed_time_in_seconds = {pan_arm.elapsed_time_in_seconds}')

print(pan_arm.tick())

while not pan_arm.tick():
    pan_arm.tick()
pan_arm.show()
print(f"pan_arm.elapsed_time_in_seconds: {pan_arm.elapsed_time_in_seconds}")