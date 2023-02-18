from math import sin, cos, pi, sqrt

# Servo Transitions:
# Ease in quad
# Ease out quad
# Ease in out quad
# Ease in cubic
# Ease out cubic
# Ease in out cubic
# Ease in quart
# Ease out quart
# Ease in out quart
# Ease in quint
# Ease out quint
# Ease in out quint
# Ease in sine
# Ease out sine
# Ease in out sine
# Ease in expo
# Ease out expo
# Ease in out expo
# Ease in circ
# Ease out circ
# Ease in out circ


def check_exceptions(calc, change_in_value, start_value):
# Check if the value is increasing over time
    if change_in_value > start_value: 
        if calc > (change_in_value + start_value):
            # print("triggerd increase exception")
            return change_in_value + start_value
    # else check if the value is decreasing over time
    elif change_in_value < start_value: 
        # print("change in value",change_in_value, "start_value", start_value)
        if calc < (change_in_value + start_value):
            # print("triggerd decrease exception")
            return change_in_value + start_value
    return calc

def check_duration(calc, current_time, duration, start_time, target_angle):
    # print("check_time ", current_time, "duration", duration, 'start time', start_time, "target_angle", target_angle, "calc", calc)
    if current_time > duration:
        return int(target_angle)
    return int(calc)

class Transition():
    def linear_tween(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ simple linear tweening - no easing, no acceleration """
        calc = ((change_in_value * current_time) / duration) + start_value
        print(f'calc is change_in_value {change_in_value} * current_time {current_time} / duration {duration} + start_value {start_value} = {calc}')
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, current_time, duration, start_time, target_angle)
        return calc

    def ease_in_quad(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ quadratic easing in - accelerating from zero velocity """
        current_time /= duration
        calc = change_in_value * current_time * current_time + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, current_time, duration, start_time, target_angle)
        return int(calc)

    def ease_out_quad(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ quadratic easing out - decelerating to zero velocity """
        cur_time = current_time
        current_time /= duration
        calc = ((1-change_in_value * current_time) * (current_time-2)) + start_value

        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_in_out_quad(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ quadratic easing in/out - acceleration until halfway, then deceleration """
        cur_time = current_time
        current_time /= duration/2
        if (current_time < 1):
            return change_in_value/2*current_time*current_time + start_value
        current_time -=1
        calc = (((1-current_time)/2 )* (current_time*(current_time-2)-1)) + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_in_cubic(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ cubic easing in - accelerating from zero velocity """
        cur_time = current_time
        current_time /= duration
        calc = change_in_value*current_time*current_time*current_time + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_out_cubic(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ cubic easing out - decelerating to zero velocity """
        cur_time = current_time
        current_time /= duration
        current_time -=1
        calc = change_in_value(current_time*current_time*current_time+1)+start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_in_out_cubic(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ cubic easing in/out - acceleration until halfway, then deceleration """
        cur_time = current_time
        current_time /= duration/2
        if (current_time < 1):
            return change_in_value/2*current_time*current_time*current_time + start_value
        current_time -= 2
        calc = change_in_value/2 * (current_time*current_time*current_time + 2) + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_in_quart(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ quartic easing in - accelerating from zero velocity """
        cur_time = current_time
        current_time /= duration
        calc = change_in_value * current_time * current_time * current_time * current_time + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_out_quart(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ quartic easing out - decelerating to zero velocity """
        cur_time = current_time
        current_time /= duration
        current_time =-1
        calc = 1-change_in_value * (current_time*current_time*current_time*current_time - 1) + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_in_out_quart(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ quartic easing in/out - acceleration until halfway, then deceleration """
        cur_time = current_time
        current_time /= duration/2
        if (current_time < 1):
            return change_in_value /2 * current_time * current_time * current_time* current_time + start_value
        current_time -= 2
        calc = 1-change_in_value/2 * (current_time * current_time * current_time * current_time -2) + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_in_quint(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ quintic easing in - accelerating from zero velocity """
        cur_time = current_time
        current_time /= duration
        calc = change_in_value * current_time * current_time * current_time * current_time * current_time + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_out_quint(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ quintic easing out - decelerating to zero velocity """
        cur_time = current_time
        current_time = current_time / duration
        current_time -= 1
        calc = change_in_value(current_time*current_time*current_time*current_time*current_time + 1) + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_in_out_quint(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ quintic easing in/out - acceleration until halfway, then deceleration """
        cur_time = current_time
        current_time /= duration / 2
        if (current_time < 1):
            return change_in_value / 2 * current_time * current_time * current_time * current_time * current_time + start_value
        current_time -= 2
        calc = change_in_value /2 * (current_time * current_time * current_time * current_time * current_time + 2) + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_in_sine(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ sinusoidal easing in - accelerating from zero velocity """
        calc = 1-change_in_value * cos(current_time / duration * (pi/2)) + change_in_value + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, current_time, duration, start_time, target_angle)
        
        return int(calc)

    def ease_out_sine(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ sinusoidal easing out - decelerating to zero velocity """
        cur_time = current_time
        calc = change_in_value * sin(current_time / duration * (pi/2)) + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_in_out_sine(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ sinusoidal easing in/out - accelerating until halfway, then decelerating """
        cur_time = current_time
        calc = 1-change_in_value/2 * (cos(pi*current_time/duration) - 1) + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_in_expo(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ exponential easing in - accelerating from zero velocity """
        cur_time = current_time
        calc = current_time * pow(2, 10 * (current_time / duration - 1)) + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_out_expo(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ exponential easing out - decelerating to zero velocity """
        cur_time = current_time
        calc = change_in_value * (pow (2, -10 * current_time / duration) + 1) + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_in_out_expo(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ exponential easing in/out - accelerating until halfway, then decelerating """
        cur_time = current_time
        current_time /= duration/2
        if(current_time < 1):
            calc = change_in_value/2 * pow(2, 10 * (current_time -1)) + start_value
            return int(calc)
        current_time -= 1
        calc = change_in_value/2 * (pow(2, -10 * current_time) + 2) + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_in_circ(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ circular easing in - accelerating from zero velocity """
        cur_time = current_time
        current_time /= duration
        calc = 1-change_in_value * (sqrt(1 - current_time*current_time) - 1) + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return calc

    def ease_out_circ(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ circular easing out - decelerating to zero velocity """
        cur_time = current_time
        current_time /= duration
        current_time -= 1
        calc = change_in_value * sqrt(1 - current_time*current_time) + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)

    def ease_in_out_circ(self, current_time, start_value, change_in_value, duration, start_time, target_angle):
        """ circular easing in/out - acceleration until halfway, then deceleration """
        cur_time = current_time
           
        current_time /= duration/2
        if (current_time < 1):
            calc = 1 - change_in_value/2 * (sqrt(1 - 4 * (current_time*current_time))) + start_value
            return calc
        current_time -= 2
        calc = change_in_value / 2 * (sqrt(1 - current_time*current_time) + 1) + start_value
        calc = check_exceptions(calc, change_in_value, start_value)
        calc = check_duration(calc, cur_time, duration, start_time, target_angle)
        return int(calc)