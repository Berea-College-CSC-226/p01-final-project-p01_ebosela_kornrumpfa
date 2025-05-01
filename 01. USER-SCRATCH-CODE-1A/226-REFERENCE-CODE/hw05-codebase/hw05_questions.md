# HW05: Funky Function, Fun Exams

## Instructions

Please replace each `**Replace this text with your response**` with your answer to the question above.

## SECTION 1 

1.a. Brainstorm with your partner three other fruitful 
functions where you could see a return value being useful.

```
1. Square_Root_Return(X)
2. Bowling_Ball_Return(X)
3. Dog_Fetch_Return(X)
```


1.b. Are functions that `print` to the screen considered fruitful functions? 
Why or why not?

```
    What makes a function fruitful? 
    
    15.	Fruitful function, a function in which a return statement 
    is used after the expression is evaluated. 
    It is fruitful because the result is returned to the function that  
    called it, as the “fruit” of calling this function.
    
    Can use print and then call a function with it?
    
    
   Print is a fruitful function if you call another function inside of it.
   EX. print(<function_call>)
```

1.c. Are functions that draw to the turtle screen considered fruitful functions? 
Why or why not?

```
     Does drawing on a screen return a value?
     What function draws the screen?
     We reviewed the code-based in HW02, and noticed that the functions that draw
     to the turtle screen do not use a RETURN. 
     
     Based on the missing RETURN, we do not think it is frutiful.

CODE BASE.     
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

     
```

In your repo, there’s another example of code with a fruitful function: 
**hw05_funky_functions.py**.
Run the code a few times, then pop over to the test suite,


**hw05_funky_functions_suite.py**. 
Answer the following questions:

1.d Run the **hw05_funky_functions_suite.py** test suite. Do all the uncommented tests pass?

```
TRUE: 

Running the funky_functions_test_suite()).
Test at line 46 ok.
Test at line 47 ok.
Test at line 48 ok.
Test at line 49 ok.
Test at line 50 ok.
Test at line 51 ok.
Test at line 52 ok.
```

1.e. Inspect each test, looking at the inputs and outputs. 
Should they all pass? (for some, it’s a judgment call… 
do you think the output of all of those is the intended operations of the programmer?)

```
    Looking at line 46-52.
    They do all pass, but should they?
    We ran each of the name inside of funky_function.py, and the inputs did produce 
    the intended outputs, because each of the first two characters were in the 
    list. 
    
    The output must be the intended operations of the program because
    the inputs were pre-defined? 
    
    In other words, the programmer had pre-defined all the possible scenarios.
    
```

1.f. Uncomment you the two commented out tests (one at a time, in line 53 and 54) 
What happens with each, and why?

```
In line 53, there is an error. This is because in this test, they did not expect 
an integer input. The program can only handle strings. 

In line 54, there is an error. This is because in this test, they also did not
expect the list input. The program can only handle strings. 
```

1.g. Brainstorm ideas of how you would fix the `willoughby_wallaby()` 
     function to handle those weird cases. 
     You don’t have to implement the fix; 
     rather, describe your solution to this problem in plain English.

```   
    Can you convert the inputs back into a string?
    
    OR
    
    Can you add another if condition, that would accept inputs of integers; 
    and an else condition that would accept lists.
    
    OR 
    In the input question, be more specific. Ask for a real name.
    
    
```

_Return to the Google Doc to continue the assignment._

## SECTION 2

2.a. After you've assigned yourself an issue and have a partner, complete the information below:

```
    Function Designer:ANTONIO K.
    Issue Title: Chapter 6.1 --> 6.5: Functions Part I
    Issue URL: https://github.com/Berea-College-CSC-226/hw05-main/issues/27
    
    Unit Tester:  ARBJOSA HALILAJA :) 
    Issue Title: Chapter 6.1 --> 6.5: Functions Part I
    Issue URL: https://github.com/Berea-College-CSC-226/hw05-main/issues/27
```

Communicate with your partner and 
develop a communication plan that works well for both of you. Describe the plan here. 
Be specific (some sections may not be needed):

2.b. When and how will the two of you be communicating?

```
    Date(s): 2/18 & 2/19
    Time(s): 8:00 - 9:00 PM 
    Location(s): CMIT
    Using Slack/Teams/E-mail/other?: IN PERSON.
```

_Return to the Google Doc to continue the assignment._

## SECTION 3 

3.a. What challenges did you experience trying to write both the code 
and the test suite at the same time? 
Put another way, what questions were you asking each other 
as you developed your code? 
How well did you communicate?**

```   
    Working on person on Day #1 made this much easier. Most of the
    questions we had were documented as comments within the code.
    Likely each of each as unique challenges when doing the function design
    vs the unit test, but since that was done (largely)
    individually, there was not a lot of communication. 
    Overall, meeting it person made getting started easy, and then
    afterward tools like Slack, PyCharm, Git, made it possible
    to work remotely. 
    
    10/10 - KOSOVO #1. 
      
```

3.b. List one or two advantages to writing the fruitful function 
_before_ writing the tests.

```
    1. The first advantage was that I'd already started to comment out 
    type of errors I was running into.
    2. The second advantage of writing the function was that 
    the test would actually know what to test. In other words,
    without a function to run, there is no function to test.
    
```

3.c. List one or two advantages to writing the test suite 
_before_ writing the fruitful function.

```
     1. The function could be designed with a specific set of inputs 
     in mind. 
     2. The functions design would take into consideration the inputs 
     of the user.
     
```

3.d. Would you prefer writing the test suite first, OR 
the fruitful function first? Why? 
```
     Both of us think that writing the function first would be better.
     If you write the test suite first, the function designer would
     still not know what function was being designed. 
     However, creating the test suit does seem more challenging.
     
```

---