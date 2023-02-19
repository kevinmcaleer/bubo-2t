# Super Servo
# Kevin McAleer 14 Feb 2023
# Servos with easing and ticks

# from .transition import Transition
from .easing import Linear, Ease_in_circ, Ease_in_cubic, Ease_in_expo, Ease_in_quad, Ease_in_quart, Ease_in_quint, Ease_in_sine, Ease_in_out_circ, Ease_in_out_cubic, Ease_in_out_expo, Ease_in_out_quad, Ease_in_out_quart, Ease_in_out_quint, Ease_in_out_sine, Ease_out_circ, Ease_out_cubic, Ease_out_expo, Ease_out_quad, Ease_out_quart, Ease_out_quint, Ease_out_sine


from time import sleep, ticks_ms, ticks_diff
from servo import Servo, servo2040

SHORT_SLEEP = 0.0001

def map_angle(x, in_min, in_max, out_min, out_max):
    """ maps the value between the in and out ranges and returns a float"""
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

class Super_Servo():
    __name = ""
    __current_angle = 0
    __transition = "ease_in_sine"
    __duration = 0.5
    __max_angle = 180
    __min_angle = 00
    __target_angle = 0
    
    __current_time = 0
    __start_value = 0
    __change_in_value = 0
    __target_angle = 90
    __tick_start_time = 0
    ease = Linear(__start_value, __target_angle, __duration)

    def __init__(self, pin, name=None, min_angle=None, max_angle=None):
        if name:
            self.__name = name
        if min_angle:
            self.__min_angle = min_angle
        if max_angle:
            self.__max_angle = max_angle

        self.__servo = Servo(pin)

    def calibration(self, calibration=None):
        """ Set or get the calibration of the servo """
        if calibration:
            self.__servo.calibration(calibration)
        else:
            return self.__servo.calibration()
    
    def __str__(self):
        return f'{self.__name}, min_angle {self.__min_angle}, max_angle {self.__max_angle}, current_angle {self.__current_angle}, target_angle {self.__target_angle}'

    def value(self, value=None):
        """ Set or get the value of the servo """
        if value:
            self.__servo.value(value)
        else:
            return self.__servo.value()
    
    def pin(self):
        return self.__servo.pin()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def angle(self):
        return self.__current_angle

    @angle.setter
    def angle(self, value):
        """ Set the angle of the servo """
        self.__current_angle = value
        self.__servo.value(value)
        sleep(SHORT_SLEEP)

    @property
    def current_angle(self):
        return self.__current_angle

    @current_angle.setter
    def current_angle(self, value):
        self.__current_angle = value

    @property
    def transition(self):
        return self.__transition
    
    @transition.setter
    def transition(self, value):
        if value in ['linear_tween','ease_in_circ','ease_in_cubic','ease_in_expo','ease_in_quad','ease_in_quart','ease_in_quint','ease_in_sine',
                     'ease_in_out_circ', 'ease_in_out_cubic', 'ease_in_out_expo', 'ease_in_out_quad', 'ease_in_out_quart', 'ease_in_out_quint', 'ease_in_out_sine',
                     'ease_out_circ', 'ease_out_cubic', 'ease_out_expo', 'ease_out_quad', 'ease_out_quart', 'ease_out_quint', 'ease_out_sine']:
            self.__transition = value
        else:
            print(f"Value '{value}' is not a valid transition type")

        if value == 'linear_tween':        
            self.ease = Linear(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_in_circ':
            self.ease = Ease_in_circ(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_in_cubic':
            self.ease = Ease_in_cubic(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_in_expo':
            self.ease = Ease_in_expo(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_in_quad':
            self.ease = Ease_in_quad(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_in_quart':
            self.ease = Ease_in_quart(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_in_quint':
            self.ease = Ease_in_quint(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_in_sine':
            self.ease = Ease_in_sine(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_in_out_circ':
            self.ease = Ease_in_out_circ(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_in_out_cubic':
            self.ease = Ease_in_out_cubic(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_in_out_expo':
            self.ease = Ease_in_out_expo(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_in_out_quad':
            self.ease = Ease_in_out_quad(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_in_out_quart':
            self.ease = Ease_in_out_quart(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_in_out_quint':
            self.ease = Ease_in_out_quint(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_in_out_sine':
            self.ease = Ease_in_out_sine(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_out_circ':
            self.ease = Ease_out_circ(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_out_cubic':
            self.ease = Ease_out_cubic(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_out_expo':
            self.ease = Ease_out_expo(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_out_quad':
            self.ease = Ease_out_quad(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_out_quart':
            self.ease = Ease_out_quart(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_out_quint':
            self.ease = Ease_out_quint(self.start_angle,self.target_angle,self.duration)
        elif value =='ease_out_sine':
            self.ease = Ease_out_sine(self.start_angle,self.target_angle,self.duration)
        
    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value

    @property
    def duration_in_seconds(self):
        return self.__duration / 1000

    @duration_in_seconds.setter
    def duration_in_seconds(self, value):
        duration = (value * 1000)
        self.__duration = duration

    @property
    def elapsed_time(self):
        elapsed = ticks_diff(self.current_time,self.__tick_start_time)
        return elapsed

    @property
    def elapsed_time_in_seconds(self):
#         print(f'current time {self.current_time} - tick_start time {self.__tick_start_time} = {self.__current_time - self.__tick_start_time}')
        reported_elapsed = self.elapsed_time / 1000
#         print(f'reported elapsed time is {reported_elapsed}')
        return reported_elapsed

    @property
    def target_angle(self):
        return self.__target_angle

    @property
    def start_angle(self):
        return self.__start_value
    
    @start_angle.setter
    def start_angle(self, value):
        if value <= self.__max_angle and value >= self.__min_angle:
            self.__start_value = value
        else:
            print("error - angle provided is outside the valid range - Max Angle: ", self.__max_angle, " Min Angle: ", self.__min_angle, " Angle provided: ", value)

    @target_angle.setter
    def target_angle(self, value):
        if value <= self.__max_angle and value >= self.__min_angle:
            self.__target_angle = value
        else:
            print("error - angle provided is outside the valid range - Max Angle: ", self.__max_angle, " Min Angle: ", self.__min_angle, " Angle provided: ", value)
        
    @property
    def change_in_value(self):
        return self.__change_in_value

    @change_in_value.setter
    def change_in_value(self, value):
        self.__change_in_value = value

    @property
    def current_time(self):
        self.__current_time = ticks_ms()
        return self.__current_time

    def tick_start(self):
        self.change_in_value = self.target_angle - self.start_angle
        self.__tick_start_time = ticks_ms()
        self.ease.start = self.__start_value
        self.ease.end = self.__target_angle
        self.ease.duration = self.duration_in_seconds
        self.__current_time = ticks_ms()
         
    @property
    def current_time_in_seconds(self):
        return self.current_time / 1000
            
    def tick(self):
#         remaining_time = self.__duration - self.elapsed_time
        
        if self.elapsed_time_in_seconds > self.duration_in_seconds:
            self.__current_angle = self.target_angle
            self.__servo.value(self.target_angle)
            sleep(SHORT_SLEEP)
            return True

#         print(f"current_time_in_seconds is {self.current_time_in_seconds} duration {self.duration_in_seconds}, elapsed time is {self.elapsed_time_in_seconds}, angle {self.angle}")
   
        self.angle = self.ease(self.elapsed_time_in_seconds)

        if self.current_angle == self.target_angle:
            return True
        else:
            return False

    def show(self):
        print("name: ", self.name, 
              "Angle", self.current_angle, 
              "start time", self.__tick_start_time, 
              "elapsed time: ", self.elapsed_time,
              "target angle:", self.target_angle,
              "Transition type:", self.transition,
              "current angle:", self.__current_angle)