import math


def damped_oscillator_position(gamma, t, omega_0):
    """ (num, num, num) -> (num)
    This function takes in the damping coefficient (gamma), time (t) and the
    angular frenquency (omega), it produces the position of the oscillator
    at the given time.
    

    >>> position = damped_oscillator_position(gamma, t, omega)
    >>> position = 
    -0.7798529395484154
    """
    position = math.exp(-gamma*t)*math.cos(math.sqrt(omega**2 - gamma**2)*t)
    return position


#""" HERE TO TEST YOUR CODE, REMOVE BEFORE HANDING IN """
#gamma = 0.1
#t = 2
#omega = 30

#position = damped_oscillator_position(gamma, t, omega)
#print("\nThe range is: " + str(position))
