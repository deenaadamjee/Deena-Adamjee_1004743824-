# provide access to the Turtle module
import turtle

# bring the turtle to life and call it alex
alex = turtle.Turtle()

#tell alex where to go 
alex.setheading(-90)      # make alex face south
alex.down()               # make alex put pen down
alex.circle(100, 90)      # make alex go in circle of radius of 150 for 360 degrees
alex.forward(100)         # make alex go 200 forward
alex.left(135)            # make alex turn to the left for 135 degree
alex.forward(283)         # make alex go 400 forward
alex.right(135)           # make alex turn to the right for -135 degree
alex.forward(100)         # make alex go 150 forward
alex.circle(-100, 180)    # make alex go in circle of radius of 150 for 90 degrees
alex.circle(-50, 180)     # make alex go in circle of radius of 150 for 90 degrees
alex.circle(50, 180)      # make alex go in circle of radius of 150 for 90 degrees
alex.circle(100, 90)      # make alex go in circle of radius of 150 for 360 degrees
