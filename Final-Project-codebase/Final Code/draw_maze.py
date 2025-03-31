import turtle
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
y=type(Ant)
print(y) # The output is <class 'turtle.Turtle'> This is an object that is part of the turtle class.

Ant.color('red') # We defining the attributes of the object ANT.
Ant.setpos(21,0) # Modifying starting position.
Aije.color('blue') # Defining the att. of object AIJE.
Aije.setpos(7,0) # Modifying start position.


"""
At this point we need to be able to modify the movement of the created objects.
To accomplish this we are referencing T11_player.py.
Our initial reference and work is located inside of /AI Programs/Example Turtle Method.py
At this stage, we need try and program the now bound keys to specific actions for the turtle objects.
"""

# Define a function to be triggered on key press
def on_key_pressed():
    print("A key was pressed, but not exactly the 'A' key.")

window.onkeypress(on_key_pressed, "a")
window.onkeypress(on_key_pressed, "w")
window.onkeypress(on_key_pressed, "d")
window.onkeypress(on_key_pressed, "s")



# Listen for key events
window.listen()









window.exitonclick()
