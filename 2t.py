# Bubo-2T the tooting robot
# 2T will take a photo if you do specific hand gestures in front of it
# It will then toot those pictures to mastodon.social

import time
import picamera
import os
import subprocess
import RPi.GPIO as GPIO
import mastodon


# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up camera
camera = picamera.PiCamera()
camera.resolution = (1024, 768)

# Set up mastodon
m = mastodon.Mastodon(
    client_id = 'clientcred.secret',
)

# Set up the loop
while True:
    # Wait for button press
    input_state = GPIO.input(18)
    if input_state == False:
        # Take a photo
        camera.capture('image.jpg')
        # Toot the photo
        m.toot_media(media_file='image.jpg', status='I am Bubo-2T the tooting robot')
        # Wait for 2 seconds
        time.sleep(2)

# End of script
