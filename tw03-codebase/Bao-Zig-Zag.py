import turtle
def main():
    wn = turtle.Screen()
    wn.bgcolor("green")
    antonio = turtle.Turtle()
    faryal = turtle.Turtle()
    antonio.pensize(15)
    faryal.pensize(30)
    faryal.pencolor("yellow")
    faryal.penup()
    faryal.goto(-40,-40)
    faryal.pendown()
    antonio.penup()
    antonio.goto(-50,-50)
    antonio.pendown()
    drawSquare(antonio)
    zigZagPattern(faryal)
    wn.exitonclick()

def drawSquare(t):
    for i in range(4):
        t.forward(300)
        t.left(90)

def zigZagPattern(t):
    for i in range(6):
        t.forward(270)
        t.left(180)
        t.goto(t.xcor(), t.ycor()+25)
        t.forward(270)
        t.right(180)
        if i==5:
            t.penup()
        t.goto(t.xcor(), t.ycor() + 25)


main()