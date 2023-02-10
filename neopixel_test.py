import time
# from pimoroni import Button
from plasma import WS2812
from servo import servo2040

NUM_LEDS = 24
SPEED = 5           # The speed that the LEDs will cycle at
BRIGHTNESS = 0.4    # The brightness of the LEDs
UPDATES = 50        # How many times the LEDs will be updated per second

# Create the LED bar, using PIO 1 and State Machine 0
led_bar = WS2812(24, 1, 0, servo2040.SDA)

print(f'starting up led_bar')
# Start updating the LED bar
led_bar.start()

print(f'led_bar complete')
offset = 0.0 
while True:
    for j in range(0.0,1.0):
        for i in range(NUM_LEDS):
            hue = float(i) / NUM_LEDS
            led_bar.set_hsv(i, hue + j, 1.0, BRIGHTNESS)
        
        time.sleep(1.0 / UPDATES)
        print(f"I is {i}, hue is {hue}, j is {j}")
    time.sleep(1.0 / UPDATES)

led_bar.clear()