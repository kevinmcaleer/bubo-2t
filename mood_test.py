# Mood test

from mood import Bubo, Mood

bubo = Bubo()
bubo.mood = "angry"
bubo.angry_mood.start()

while bubo.angry_mood.animate:
    bubo.angry_mood.tick()

print('done')