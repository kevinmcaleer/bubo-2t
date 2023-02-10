# Moods

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
# angry
# red eyes
# eyes half closed
# mouth open and close
    def __init__(self):
        self.super().__init__(name="angry", ticks=20)
        
        def tick(self):
            super().tick()
            
class Quirky_mood(Mood):
    def __init__(self):
        self.super().__init__(name="angry", ticks=20)
        self.bubo
        
        
    def tick(self):
        super().tick()
            
class Bubo():
    
    angry_mood = Mood("angry")
    
    def __init__(self):
        self.mood = "neutral"
