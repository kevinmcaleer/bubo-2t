from bubo import Bubo2t
from time import sleep

bubo = Bubo2t()


bubo.eyes_close(duration=1)
while not bubo.tick():
    bubo.tick()

bubo.eyes_open(duration=.5)
while not bubo.tick():
    bubo.tick()

bubo.eyes_close(duration=.5)
while not bubo.tick():
    bubo.tick()
    
bubo.eyes_open(duration=.5)
while not bubo.tick():
    bubo.tick()

bubo.eyes_close(duration=.5)
while not bubo.tick():
    bubo.tick()