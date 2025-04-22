import turtle

# Function to move the turtle up
def move_alex_up():
    alex.setheading(90)  # Set heading to 'up' (90 degrees)
    alex.forward(10)

# Function to move the turtle down
def move_alex_down():
    alex.setheading(270)  # Set heading to 'down' (270 degrees)
    alex.forward(10)

# Function to move the turtle left
def move_alex_left():
    alex.setheading(180)  # Set heading to 'left' (180 degrees)
    alex.forward(10)

# Function to move the turtle right
def move_alex_right():
    alex.setheading(0)  # Set heading to 'right' (0 degrees)
    alex.forward(10)

# Set up the window and the turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.penup()

# Bind keys to movement functions
window.onkeypress(move_alex_left, "Left")
window.onkeypress(move_alex_up, "Up")
window.onkeypress(move_alex_right, "Right")
window.onkeypress(move_alex_down, "Down")

# Listen for keypress events
window.listen()

# Keep the window open
window.exitonclick()
