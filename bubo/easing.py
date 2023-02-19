import math

class TransitionBase:
    limit = (0, 1)

    def __init__(self, start:float = 0, end:float = 0, duration:float = 1):
        self.start = start
        self.end = end
        self.duration = duration

    def func(self, t:float) -> float:
        return NotImplementedError

    def ease(self, alpha: float) -> float:
        t = self.limit[0] * (1 - alpha) + self.limit[1] * alpha
        t /= self.duration
        a = self.func(t)
        return self.end * a + self.start * (1 - a)

    def __call__(self, alpha: float) -> float:
        return self.ease(alpha)

# Linear easing functions

class Linear(TransitionBase):
    def func(self, t:float) -> float:
        return t

# Quadratic easing functions

class Ease_in_quad(TransitionBase):
    def func(self, t: float) -> float:
        return t * t
    
class Ease_out_quad(TransitionBase):
    def func(self, t: float) -> float:
        return -(t * (t - 2))

class Ease_in_out_quad(TransitionBase):
    def func(self, t: float) -> float:
        t *= 2
        if t < 1:
            return 0.5 * t * t
        t -= 1
        return -0.5 * (t * (t - 2) - 1)

# Cubic easing functions

class Ease_in_cubic(TransitionBase):
    def func(self, t: float) -> float:
        return t * t * t
    
class Ease_out_cubic(TransitionBase):
    def func(self, t: float) -> float:
        t -= 1
        return t * t * t + 1

class Ease_in_out_cubic(TransitionBase):
    def func(self, t: float) -> float:
        t *= 2
        if t < 1:
            return 0.5 * t * t * t
        t -= 2
        return 0.5 * (t * t * t + 2)
        
# Quartic easing functions

class Ease_in_quart(TransitionBase):
    def func(self, t: float) -> float:
        return t * t * t * t

class Ease_out_quart(TransitionBase):
    def func(self, t: float) -> float:
        t -= 1
        return -(t * t * t * t - 1)

class Ease_in_out_quart(TransitionBase):
    def func(self, t: float) -> float:
        t *= 2
        if t < 1:
            return 0.5 * t * t * t * t
        t -= 2
        return -0.5 * (t * t * t * t - 2)

# Quintic easing functions

class Ease_in_quint(TransitionBase):
    def func(self, t: float) -> float:
        return t * t * t * t * t

class Ease_out_quint(TransitionBase):
    def func(self, t: float) -> float:
        t -= 1
        return t * t * t * t * t + 1

class Ease_in_out_quint(TransitionBase):
    def func(self, t: float) -> float:
        t *= 2
        if t < 1:
            return 0.5 * t * t * t * t * t
        t -= 2
        return 0.5 * (t * t * t * t * t + 2)

# Sinusoidal easing functions

class Ease_in_sine(TransitionBase):
    def func(self, t: float) -> float:
        return -math.cos(t * (math.pi / 2)) + 1

class Ease_out_sine(TransitionBase):
    def func(self, t: float) -> float:
        return math.sin(t * (math.pi / 2))

class Ease_in_out_sine(TransitionBase):
    def func(self, t: float) -> float:
        return -0.5 * (math.cos(math.pi * t) - 1)

# Exponential easing functions

class Ease_in_expo(TransitionBase):
    def func(self, t: float) -> float:
        return math.pow(2, 10 * (t - 1))

class Ease_out_expo(TransitionBase):
    def func(self, t: float) -> float:
        return -math.pow(2, -10 * t) + 1

class Ease_in_out_expo(TransitionBase):
    def func(self, t: float) -> float:
        t *= 2
        if t < 1:
            return 0.5 * math.pow(2, 10 * (t - 1))
        t -= 1
        return 0.5 * (-math.pow(2, -10 * t) + 2)

# Circular easing functions

class Ease_in_circ(TransitionBase):
    def func(self, t: float) -> float:
#         print(f't is {t}')
        return -(math.sqrt(1 - t * t) - 1)

class Ease_out_circ(TransitionBase):
    def func(self, t: float) -> float:
        t -= 1
        return math.sqrt(1 - t * t)
    
class Ease_in_out_circ(TransitionBase):
    def func(self, t: float) -> float:
        t *= 2
        if t < 1:
            return -0.5 * (math.sqrt(1 - t * t) - 1)
        t -= 2
        return 0.5 * (math.sqrt(1 - t * t) + 1)

# Elastic easing functions

class Ease_in_elastic(TransitionBase):
    limit = (-1, 1)
    def func(self, t: float) -> float:
        if t == 0:
            return 0
        if t == 1:
            return 1
        t -= 1
        return -math.pow(2, 10 * t) * math.sin((t - 0.3 / 4) * (2 * math.pi) / 0.3)

class Ease_out_elastic(TransitionBase):
    limit = (-1, 1)
    def func(self, t: float) -> float:
        if t == 0:
            return 0
        if t == 1:
            return 1
        return math.pow(2, -10 * t) * math.sin((t - 0.3 / 4) * (2 * math.pi) / 0.3) + 1

class Ease_in_out_elastic(TransitionBase):
    limit = (-1, 1)
    def func(self, t: float) -> float:
        if t == 0:
            return 0
        if t == 1:
            return 1
        t *= 2
        if t < 1:
            t -= 1
            return -0.5 * math.pow(2, 10 * t) * math.sin((t - 0.3 / 4) * (2 * math.pi) / 0.3)
        t -= 1
        return math.pow(2, -10 * t) * math.sin((t - 0.3 / 4) * (2 * math.pi) / 0.3) * 0.5 + 1

# Back easing functions

class Ease_in_back(TransitionBase):
    limit = (-1, 1)
    def func(self, t: float) -> float:
        s = 1.70158
        return t * t * ((s + 1) * t - s)

class Ease_out_back(TransitionBase):
    limit = (-1, 1)
    def func(self, t: float) -> float:
        t -= 1
        s = 1.70158
        return t * t * ((s + 1) * t + s) + 1

class Ease_in_out_back(TransitionBase):
    limit = (-1, 1)
    def func(self, t: float) -> float:
        s = 1.70158 * 1.525
        t *= 2
        if t < 1:
            return 0.5 * (t * t * ((s + 1) * t - s))
        t -= 2
        return 0.5 * (t * t * ((s + 1) * t + s) + 2)
