import turtle
""" We are going to continue to use this file for reference, but are no longer
going to use the turtle module."""
window = turtle.Screen() # Fundamentally, this line uses the Screen() method inside of the turtle class to create an object called windows. This line crashes if there is no event handler in line 3.
# a=type(wn)
# print(a)
# b="string"
# b1=type(b)
# print(b1)
# z=[1,2,3]
# type(z)
#print(z)

Ant = turtle.Turtle() # This will create an object in memory that can be acted on.
Aije = turtle.Turtle() # This will create an object in memory that can be acted on.
# y=type(Ant) #type test.
# print(y) # The output is <class 'turtle.Turtle'> This is an object that is part of the turtle class.

Ant.penup()
Ant.color('red') # We defining the attributes of the object ANT.
Ant.setpos(21,0) # Modifying starting position.

Aije.penup()
Aije.color('blue') # Defining the att. of object AIJE.
Aije.setpos(7,0) # Modifying start position.

"""
At this point we need to be able to modify the movement of the created objects.
To accomplish this we are referencing T11_player.py.
Our initial reference and work is located inside of /AI Programs/Example Turtle Method.py
At this stage, we need try and program the now bound keys to specific actions for the turtle objects.
"""

# Define a function to be triggered on key press
"""The following function will behave to bind an event handler to a specific key in order
to support the movement of the object. This required the creation of additional classes to 
support the 4 cardinal movements of each object (UP-DOWN-LEFT-RIGHT). 

"""

def move_ant_up():
    Ant.setheading(90)  # Set heading to 'up' (90 degrees)
    Ant.forward(10)

def move_ant_down():
    Ant.setheading(270)  # Set heading to 'down' (270 degrees)
    Ant.forward(10)

def move_ant_left():
    Ant.setheading(180)  # Set heading to 'left' (180 degrees)
    Ant.forward(10)

def move_ant_right():
    Ant.setheading(0)  # Set heading to 'right' (0 degrees)
    Ant.forward(10)

def move_aije_up():
    Aije.setheading(90)  # Set heading to 'up' (90 degrees)
    Aije.forward(10)

def move_aije_down():
    Aije.setheading(270)  # Set heading to 'down' (270 degrees)
    Aije.forward(10)
    return

def move_aije_left():
    Aije.setheading(180)  # Set heading to 'left' (180 degrees)
    Aije.forward(10)
    return

def move_aije_right():
    Aije.setheading(0)  # Set heading to 'right' (0 degrees)
    Aije.forward(10)
    return

#def on_key_pressed():
    # print("A key was pressed, but not exactly the 'A' key.")

window.onkeypress(move_ant_left, "a") # This
window.onkeypress(move_ant_up, "w")
window.onkeypress(move_ant_right, "d")
window.onkeypress(move_ant_down, "s")

window.onkeypress(move_aije_left, "f") # This
window.onkeypress(move_aije_up, "t")
window.onkeypress(move_aije_right, "h")
window.onkeypress(move_aije_down, "g")

# Listen for key events
window.listen()









window.exitonclick()
