import time
# from pimoroni import Button
from plasma import WS2812, COLOR_ORDER_RGB, COLOR_ORDER_RBG, \
                   COLOR_ORDER_GRB, COLOR_ORDER_GBR, COLOR_ORDER_BGR, COLOR_ORDER_BRG,

from servo import servo2040

NUM_LEDS = 24
SPEED = 5           # The speed that the LEDs will cycle at
BRIGHTNESS = 0.3    # The brightness of the LEDs
UPDATES = 50        # How many times the LEDs will be updated per second

# Create the LED bar, using PIO 1 and State Machine 0
led_bar = WS2812(24, 1, 0, servo2040.SDA) #GBR

led_bar.start()

offset = 0.0

YELLOW = (255,255,0)
RED = (255,0,0)
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


while True:
    
    hue = 0.17 #0.15
    sat = 1.0
    val = 0.4
    
    for i in range(NUM_LEDS):
#         hue,sat,val = rgb2hsv(YELLOW[0],YELLOW[1],YELLOW[2])
#         hue, sat, val = rgb2hsv(255,255,0)

        led_bar.set_hsv(i, hue, sat, val)
    
    time.sleep(0.5)
    
#     for i in range(NUM_LEDS):
#         hue,sat,val = rgb2hsv(RED[0],RED[1],RED[2])
# 
# 
#         led_bar.set_hsv(i, hue, sat, val)
#     time.sleep(0.5)

led_bar.clear()
