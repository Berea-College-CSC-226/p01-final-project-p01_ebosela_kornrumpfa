import turtle

def main(): #The main function creates the screen, modifies that screen, as well as creating the turtle objects
    # these turtle objects are modified, and then moved using two functions.
    wn = turtle.Screen()
    wn.bgcolor("green")
    wn.textinput("Hello", "What is your name?")
    Tony = turtle.Turtle() #Used to draw
    Tiger = turtle.Turtle()
    # Failed attempt to create the turtle object DrawTurtle(Tiger)
    Tony.pencolor("Yellow")
    Tiger.pencolor("Pink")
    Tony.pensize(50)
    Tiger.pensize(50)
    moveTurtle(Tony)
    invertMoveTurtle(Tiger)
    wn.exitonclick()


def moveTurtle(t): #Funtion to control movement, using a loop.
    for i in range(4):
        t.forward(300)
        t.left(90)
def invertMoveTurtle(t): #Funtion to control movement, using a loop.
    for i in range(4):
        t.forward(-300)
        t.right(-90)

main()

# Your program uses the Turtle library to draw on the screen. | COMPLETE
#Your program uses at least two turtle objects to draw. | COMPLETE
#What you draw is something that brings a smile to your face.| I like it. COMPLETE.
#The program uses at least one loop. | Using a for loop. COMPLETE
#The program makes use of multiple attributes and methods of either the turtle class,
# the screen class, or both. #COMPLETE.
# You can explore the full lists of methods in Section 24.1.2 and Section 24.1.2.2 of the documentation for Turtle graphics.
#Your program has the standard header block used in all our programs.
#Add comments to clarify your intent on any lines that are doing something that is not immediately clear. # COMPLETE
