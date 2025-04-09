import turtle

# Set up screen
screen = turtle.Screen()
screen.title("Turtle Player Movement")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Create player turtle
player = turtle.Turtle()
player.shape("square")
player.color("white")
player.penup()

# Movement functions
def move_up():
    y = player.ycor()
    player.sety(y + 20)

def move_down():
    y = player.ycor()
    player.sety(y - 20)

def move_left():
    x = player.xcor()
    player.setx(x - 20)

def move_right():
    x = player.xcor()
    player.setx(x + 20)

# Key bindings
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Keep window open
screen.mainloop()
