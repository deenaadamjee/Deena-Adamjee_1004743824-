import math

gamma = input ('what is your value for gamma?')
t = input ('what is your value for time?')
omega = input ('what is your value for omega?')

def damped_oscillator_position(gamma, t, omega_0):
    ''' (num, num, num) -> (num)
    This function takes in the damping coefficient (gamma), time (t) and the
    angular frenquency (omega), it produces the position of the oscillator
    at the given time.
    '''
    position = damped_oscillator_position(gamma, t, omega)
    damped_oscillator_position = math.exp(-gamma*t)*math.cos(math.sqrt(omega**2 - gamma**2)*t)
    return damped_oscillator_position

#""" HERE TO TEST YOUR CODE, REMOVE BEFORE HANDING IN """
#gamma = 0.1
#t = 2
#omega = 30

print("\nThe position is: " + str(position))

