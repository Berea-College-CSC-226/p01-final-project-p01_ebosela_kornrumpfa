######################################################################
# Author: Dr. Scott Heggen          TODO: Change this to your name, if modifying
# Username: heggens                 TODO: Change this to your username, if modifying
#
# Assignment: HW02: Loopy Turtles, Loopy Languages
# Purpose: To very simply demonstrate the turtle library to demo shapes
######################################################################
# Acknowledgements:
#
# originally created by Dr. Jan Pearce and Dr. Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

import turtle               # allows us to use the turtles library

turtle.colormode(255)       # change color modes

wn = turtle.Screen()        # Initializes the Screen object to draw on
wn.bgcolor('#DDDDDD')       # Sets background to gray

# Draws a house on the screen
shape = turtle.Turtle()
shape.hideturtle()

# Make the roof
shape.color('red')
shape.begin_fill()          # Tells Python to fill the shape with a color when done
for side in range(3):
    shape.forward(100)
    shape.left(120)
shape.end_fill()            # Tells Python the shape is complete; now fill it
shape.penup()

# Make the main house rectangle
shape.color('#3333FF')
shape.pendown()
shape.begin_fill()
for side in range(2):
    shape.forward(100)
    shape.right(90)
    shape.forward(140)
    shape.right(90)
shape.end_fill()
shape.penup()


# Write text to the screen
shape.color("#0F00F0")
shape.setpos(40,100)
shape.write("My House",move=False,align='center',font=("Arial",30,("bold","normal")))

wn.exitonclick()
