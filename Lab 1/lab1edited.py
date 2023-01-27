# APS106 Lab 1 - Drawing Shapes with Turtle
# Student Name: Deena
# PRA Section: 0101


################################################
# Part 1 - Finding Errors and Debugging
################################################

# provide access to the Turtle module
import turtle

# bring the turtle to life and call it alex
alex = turtle.Turtle()

# tell alex where to go
alex.setheading(90)     # make alex face north
alex.down()             # make alex put pen down
alex.forward(50)        # make alex go 50 forward
alex.right(90)          # make alex turn right 90 degree
alex.circle(50, 180)    # make alex go in circle of radius of 50 for 180 degree
alex.left(90)           # make alex turn to the left for 90 degree
alex.forward(150)       # make alex go forward 150 steps

alex.setheading(0)      # make alex face east
alex.down()             # make alex put pen down
alex.forward(50)        # make alex go 50 forward
alex.right(90)          # make alex turn right 90 degree
alex.circle(50, 180)     # make alex go in circle of radius of 50 for 180 degree
alex.left(90)           # make alex turn to the left for 90 degree
alex.forward(150)       # make alex go forward 150 steps

alex.setheading(180)    # make alex face west
alex.down()             # make alex put pen down
alex.forward(50)        # make alex go 50 forward
alex.right(90)          # make alex turn right 90 degree
alex.circle(50, 180)    # make alex go in circle of radius of 50 for 180 degree
alex.left(90)           # make alex turn to the left for 90 degree
alex.forward(150)       # make alex go forward 150 steps

alex.setheading(-90)    # make alex face south
alex.down()             # make alex put pen down
alex.forward(50)        # make alex go 50 forward
alex.right(90)          # make alex turn right 90 degree
alex.circle(50, 180)    # make alex go in circle of radius of 50 for 180 degree
alex.left(90)           # make alex turn to the left for 90 degree
alex.forward(150)       # make alex go forward 150 steps
alex.up()

################################################
# Part 2 - Draw The Shape In the Handout
################################################
# modify the above code to tell alex
# alex.setheading(0)      # make alex face east
# alex.circle(100, 180)   # make alex go in a circle with radius of 100 for 180 degrees
# TODO: Enter your code here

#tell alex where to go 
alex.forward(300)
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

turtle.done()