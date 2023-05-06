# from servo import servo2040, Servo
#import plasma
#from plasma import WS2812
from time import sleep
import math

from inventorhatmini import SERVO_1, SERVO_2, SERVO_3, SERVO_4, InventorHATMini
from ioexpander import OUT
from inventorhatmini.plasma import Plasma
from ioexpander.servo import Servo

NUM_LEDS = 24
NUM_SERVOS = 3
LED_SERVO_PIN = 22

board = InventorHATMini(init_servos=False)

board.servos = [Servo(board.ioe, board.IOE_SERVO_PINS[i]) for i in range(NUM_SERVOS)]

# board.servo_pin_mode(SERVO_1, 
# mouth = Servo(servo2040.SERVO_1)

#mouth = board.servos[SERVO_1]

# cal = mouth.calibration()
# cal.first_value(-10)
# cal.last_value(+40)
# mouth.calibration(cal)

# left_eye = Servo(servo2040.SERVO_3)
# right_eye = Servo(servo2040.SERVO_2)

#left_eye = board.servos[SERVO_3]
#right_eye = board.servos[SERVO_2]

SPEED = 5           # The speed that the LEDs will cycle at
BRIGHTNESS = 0.4    # The brightness of the LEDs
UPDATES = 50        # How many times the LEDs will be updated per second

# Create the LED bar, using PIO 1 and State Machine 0
#led_bar = WS2812(NUM_LEDS, 1, 0, servo2040.SDA, color_order=plasma.COLOR_ORDER_RGB)
led_bar = Plasma(NUM_LEDS, LED_SERVO_PIN)

#led_bar.start()
SWEEPS = 3              # How many sweeps of the servo to perform
STEPS = 10              # The number of discrete sweep steps
STEPS_INTERVAL = 0.5    # The time in seconds between each step of the sequence
SWEEP_EXTENT = 50.0     # How far from zero to move the servo when sweeping

YELLOW = (255, 255, 0)
YELLOW_HUE = 0.2

def countdown(seconds):
    for n in range(seconds, 0, -1):
        print(f'{n} seconds remaining')
        sleep(1)

def rgb2hsv(r:int, g:int, b:int):
        h = 0
        s = 0
        v = 0
        # constrain the values to the range 0 to 1
        r_normal, g_normal, b_normal,  = r / 255, g / 255, b / 255
        cmax = max(r_normal, g_normal, b_normal)
        cmin = min(r_normal, g_normal, b_normal)
        delta = cmax - cmin
        
        # Hue calculation
        if(delta ==0):
            h = 0
        elif (cmax == r_normal):
            h = (60 * (((g_normal - b_normal) / delta) % 6))
        elif (cmax == g_normal):
            h = (60 * (((b_normal - r_normal) / delta) + 2))
        elif (cmax == b_normal):
            h = (60 * (((r_normal - g_normal) / delta) + 4))
        
        # Saturation calculation
        if cmax== 0:
            s = 0
        else:
            s = delta / cmax
            
        # Value calculation
        v = cmax
        
        h = h / 100
        
        print(f"normals are: {r_normal}, {g_normal}, {b_normal}, cmax is {cmax}, delta is {delta}")
        print(f"h:{h}, s:{s}, v:{v}")
        return h, s, v 

def rainbow_eyes(seconds):
    print('glow')
    eyes_open(0.25)
    updates = 100
    
    # The SPEED that the LEDs cycle at (1 - 255)
    SPEED = 20
    SPEED = min(255, max(1, SPEED))
    offset = 0.0    
    offset += float(SPEED) / 2000.0

    for i in range(NUM_LEDS):
        hue = float(i) / NUM_LEDS
        led_bar.set_hsv(i, hue + offset, 1.0, BRIGHTNESS)

        sleep(seconds / UPDATES /10)
    

def chirp(seconds):
    updates = 100
    extent = 40
    print('chirp')
    for j in range(SWEEPS):
        for i in range(360):
            value = math.sin(math.radians(i)) * extent
            mouth.value(value)
    #         left_eye.value(value)
    #         right_eye.value(-value)
            sleep(seconds/updates)
#     sleep(1)

def wink(seconds):
    print('wink')
    updates = 100
    left_eye.value(-60)
    for i in range(360):
        value = math.sin(math.radians(i)) * SWEEP_EXTENT
        right_eye.value(-value)
        sleep(seconds/updates)
    eyes_open(0.25)
        
def eyes_open(seconds):
    print('eyes_open')
    updates = 100
    value = 60
    for j in range(1,updates):
        val = value / (updates/j)
#         print(f'val = {val}')
        left_eye.value(val)
        right_eye.value(-val)
        sleep(seconds/updates)
    
def glow(glow_hue, seconds):
    print('glow')
    updates = 100
    for j in range(1,updates):
        for i in range(NUM_LEDS):
            
            hue = glow_hue
            sat = 1.0
            val = (j/updates) * BRIGHTNESS 
#             print(f'val {val}')
            led_bar.set_hsv(i, hue, sat, val)
        sleep(seconds/updates)

def reverse_glow(glow_hue, seconds):
    print('reverse glow')
    updates = 100
    for j in range(updates,1, -1):
        for i in range(NUM_LEDS):
            
            hue = glow_hue
            sat = 1.0
            val = (j/updates) * BRIGHTNESS 
            
            led_bar.set_hsv(i, hue, sat, val)
        sleep(seconds/updates)    
            
def neutral():
    print('neutral')
    left_eye.value(-60)
    right_eye.value(60)

    for i in range(NUM_LEDS):
        
        hue = 0.2
        sat = 1.0
        val = 0.4
        
        led_bar.set_hsv(i, hue, sat, val)
    for i in range(360):
        value = math.sin(math.radians(i)) * 50
        left_eye.value(value)
        right_eye.value(-value)
        sleep(0.002)

    mouth_close(0.5)
    glow(YELLOW_HUE, 2)
    
def eyes_half_closed():
    print('eyes half closed')
    left_eye.value(-60)
    right_eye.value(60)

    for i in range(180):
        value = math.sin(math.radians(i)) * SWEEP_EXTENT
        left_eye.value(value)
        right_eye.value(-value)
        sleep(0.002)

def in_love(seconds):
    print('in love')
    val = 20
    left_eye.value(val)
    right_eye.value(-val)
    mouth_open(0.25)
    updates = 100
    for n in range(4):
        glow(0.4, 0.1)
        reverse_glow(0.4, 0.1)

def mouth_open(seconds):
    print('mouth open')
    mouth.value(-20)
    sleep(seconds)

def mouth_close(seconds):
    print('mouth close')
    mouth.value(-2)
    sleep(seconds)
    
def eyes_closed(seconds):
    print('eyes closed')
    updates = 50
    for i in range(updates):
        left_eye.value(-i)
        right_eye.value(i)
        sleep(0.002)

def wake_up(seconds):
    print('wake up')
    updates = 100
    for j in range(updates):
        for i in range(NUM_LEDS):
            
            hue = 0.2 # 0.4 is pink
            sat = 1.0
            val = 0.4 * (j / updates)
            
            led_bar.set_hsv(i, hue, sat, val)

        sleep(seconds/updates)
    eyes_open(3)

def tired(seconds):
    print('tired')
    updates = 100
    servo_val = 60
    for j in range(updates,0,-1):
        for i in range(NUM_LEDS):
            
            hue = 0.2 # 0.4 is pink
            sat = 1.0
            val = 0.4 * (j / updates)
            
            led_bar.set_hsv(i, hue, sat, val)
        eye_val = j-servo_val
        left_eye.value(eye_val)
        right_eye.value(-eye_val)
        print(f'j {j}, val {val}, eye_val {eye_val}')
        sleep(seconds/updates)
    
    mouth_open(1)
    sleep(1)
    mouth_close(1)
    eyes_closed(1)


def angry(seconds):
    print('angry')
    for i in range(NUM_LEDS):
        
        hue = 0.3 # 0.4 is pink
        sat = 1.0
        val = 0.4
        
        led_bar.set_hsv(i, hue, sat, val)

    updates = 10
#     for j in range(updates):

    left_eye.value(-60)
    right_eye.value(60)

    for i in range(360):
        value = math.sin(math.radians(i)) * 25
#         print(f'val = {value}')
        left_eye.value(value)
        right_eye.value(-value)
        sleep(0.002)
    mouth_open(2)
    
eye_val = 40    
left_eye.value(-eye_val)
right_eye.value(eye_val)
sleep(2)
# eyes_closed(1)
# mouth_close(0.25)

while True:
    rainbow_eyes(30)
    # chirp(0.5)
    
#     countdown(30)

    in_love(5)

    neutral()
    countdown(20)
    
    tired(5)
    countdown(10)
     
    wake_up(4)
    
    neutral()
    countdown(20)
        
    angry(2)
    countdown(5)
    neutral()

    wink(1)
    
    neutral()
    countdown(20)
    
    chirp(1)
    
    neutral()
    countdown(20)

led_bar.clear()
eyes_closed(0.5)
mouth_close(0.25)