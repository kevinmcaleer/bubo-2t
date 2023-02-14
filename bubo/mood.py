# Moods

# Moods:
# * Angry (red eyes, eyes half closed)
# * Happy (eyes wide, glowing white)
# * Sleepy (leds dim, eyes half open)
# * Sad (eyes half open, mouth half open, yellow lights dim)
# * Shocked mouth open eyes wide, eyes strobing)
# * Chatty (beak opens and closes a lot
# * Bored (one eye half open, one eye open)
# * Neutral (eyes open, blink every 10 seconds, yellow glow)
# * Quirky - one eye open, one eye half, beak half open, rainbow colours

class Mood():
    
    cycle = 0
    animate = False
    name = "empty"
    ticks = 10
    
    def __init__(self, bubo, name=None, ticks=None):
        self.bubo = bubo
        if name:
            self.name = name
        if ticks:
            self.ticks = ticks
            
    def tick(self):
        print(f'{self.name}: cycle {self.cycle}, animate {self.animate}')
        if self.cycle == 0:
            self.animate = True
            self.cycle += 1
        else:
            self.cycle += 1
        
        if self.cycle == self.ticks:
            self.animate = False
            self.cycle = 0
          
    def start(self):
        self.animate = True
        self.cycle = 0
    
class Angry_Mood(Mood):
    """
    Mood name: Angry
    Eye colour: red
    Eye Servos: both half closed
    Mouth: open and close
    """

    def __init__(self):
        self.super().__init__(name="angry", ticks=20)
        
        def tick(self):
            super().tick()

        
            
class Quirky_mood(Mood):
    def __init__(self):
        self.super().__init__(name="angry", ticks=20)
        self.bubo.left
        
        
    def tick(self):
        super().tick()
            
# class Bubo():
    
#     angry_mood = Mood("angry")
    
#     def __init__(self):
#         self.mood = "neutral"
