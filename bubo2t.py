from bubo import Bubo2t
from time import sleep

bubo = Bubo2t()

bubo.mouth_open()
sleep(0.5)

bubo.mouth_close()
sleep(0.5)

bubo.mouth.to_mid()
