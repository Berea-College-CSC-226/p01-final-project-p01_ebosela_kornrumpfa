import turtle

# Define a function to be triggered on key press
def on_key_pressed():
    print("A key was pressed, but not exactly the 'A' key.")

# Set up the screen
screen = turtle.Screen()

# Bind the on_key_pressed function to the "a" key
''' We want to utilize the .onkeypress method in combination with the screen object created in line 8 
in order to bind the function on_key_pressed to the up-arrow.
At first we tried to use up-arrow, down-arrow, left-arrow, and right-arrow, but this 
threw an error (likely due to some incorrect use of the string name and 
codex association). 
So, Instead we are going to try to use "a", "w", "d", "s". [PASS]

'''
screen.onkeypress(on_key_pressed, "a")
screen.onkeypress(on_key_pressed, "w")
screen.onkeypress(on_key_pressed, "d")
screen.onkeypress(on_key_pressed, "s")

# screen.onkeypress(on_key_pressed, "up_arrow, left_arrow, right_arrow,down_arrow")
# Error: _tkinter.TclError: bad event type or keysym "up_arrow,"


# Listen for key events
screen.listen()

# Keep the window open
turtle.mainloop()

turtle.exitonclick()