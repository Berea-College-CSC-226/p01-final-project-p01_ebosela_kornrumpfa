from turtle import Turtle
import os
"""
Question 1:
True or False: A class is interchangeable with a function?
    False - A class and a function are two distinction data-types, as proved by the code-block below.
    Typically, functions are nested within classes.

Class - [attributes, methods, overrides, constructors]
Functions - [...]
Methods - [...]

"""

class foo0():
     def foo2(self):
        pass

def foo1():
    pass

a=type(foo0)
print(a)

b=type(foo1)
print(b)

class myClass: #It may be that classes are no loaded the same way as functions?
    def __init__(self,value): #loading an __init__ method with two parameters.
        self.value = value
    def display_value(self):
        print(f"The value is: {self.value}") # Use of f-strings.

### Once a class is created, instance of that class can be created.
objectInstance0 = myClass(10) #The class blueprint is loaded with an input parameter of 10.
objectInstance0.display_value()

#--------------------------------------------------------------------------

""" 
Question 2
Which one of the sentences correctly describes a (child class) that is a type of (parent class)? 
a. LabeledPoint is a type of Point. [X] <LabeledPoint> is a type of <Point>
b. Dog is a type of Cat. # <Dog> is a type of <Cat>.
c. 2 is a type of alphabet. # <2> is a type of <alphabet>.
d. Fish is a type of mammal. # <Fish> is a type of <mammal>.

This question is a reference to guiding ones understanding of the parent-child relationships.
By filling is the sentence: this <child-class> is a type of that <parent-class>.

In the code block below, I want to illustrate a parent class and a child class interacting

"""



class Point:
    def __init__(self,x=0,y=0):
        self.x = x #  # I attempted to use self.x = x in the child class, but it was not needed.
        self.y = y # Same with self.y = y. Not needed.
    def move(self,dx,dy):
        self.x += dx
        self.y += dy
    def __str__(self): #What is the function of __str__?
        return f"Point({self.x}, {self.y})" #f-string.

objectInstance1 = Point(10,20) #Overwrite the init values of x and y from 0 and 0 to 10 and 20.
print(objectInstance1)

class LabelPoint(Point):
    def __init__(self,x,y,label): #call to __init__ of the super class is missing. Super class == Parent class?
        super().__init__(x,y) # This is how the class to the __init__ of the super class is made.
        self.label = label #The child class is extending an attribute of the Point class.
    def __str__(self):  #This method is used in coordination with __init__ to perform the extension.
        return f"LabelPoint({self.label}, {self.x}, {self.y})" # # The __str__ is also performing an override.
    def rename(self,new_label): #Additional method added with an additional attribute.
        self.label = new_label

# Object creation called labelPoint using LabelPoint class.
labelPoint = LabelPoint(10,20,"STARTING_LABEL")
print(labelPoint)

labelPoint.move(10,20) #The method .move() can be used on the object created by the LabelPoint child class because of inheritance.
print(labelPoint)

labelPoint.rename("ENDING_LABEL") #The class labelPoint was expanded with the method .rename()
print(labelPoint)

# --------------------------------------------------------------------------------------------
"""
Question 3:
Inheritance vs. Composition

Composition, occurs when an object stores a reference to one or more objects 
in one of its instance variables.  Therefore it should be used, if an object needs to store a reference
to one or more objects in one of its instance variables. 

Inheritance, 

In other words, inheritance should be used if the child class is a specialization of its parent class.
Composition, should be used if the statement fails the heuristic linguistic test used for testing inheritance:
" <rectangle> is a type of <point> " and instead passes the test "<shape> has an <rectangle>". 

"""

# Parent-child relationship using inheritance. "Circle is a type of Shape; Shape is a type of Circle"
class Shape:
    def __init__(self,color="black"):
        self.color = color
    def draw(self):
        print(f"Drawing shape using the color defined by in the __init__ method of: {self.color}")
class Circle(Shape): #The circle class is calling methods from the Shape class.
    def __init__(self,radius,color="black"): #We have to restate the arguments...why?
        super().__init__(color) # This line of code allows the child class to inherit from the parent class.
        self.radius = radius
    def draw(self):
        print("In seeking to understand inheritance, this code block creates")
        print(f"A circle with the radius of {self.radius} and color: {self.color}")

circle = Circle(radius=10,color="red")
circle.draw()

### Parent-child relationship using composition. "Rectangle has a Point; Point has a Rectangle"

# Helper class for composition.
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

# Observation: This child class does not inherit from the Point class.
class Rectangle:
    def __init__(self,width,height,position: Point): ## This class seems to be using composition as indicated its call to the point class "position: Point".
        self.width = width
        self.height = height
        self.position = position
    def area(self):
        return self.width * self.height
    def describe(self):
        print("In seeking to understand the difference between inheritance and composition, this code block creates")
        print(f"A rectangle at point: ({self.position.x}, {self.position.y}) has an area of {self.area()}")

# How to use this composition
position = Point(10,20)
rectangle = Rectangle(4,5,position)
rectangle.describe()

############################## BREAK ######
""" 
Question 4
What distinguishes the following:
Classes -   There aren't a many class uses of returns. 
            The first line definition doesn't include parameters; but its methods (like __init__) do.
            Contains both methods and attributes.
            There is a  difference between Object Oriented Design && Functional Programming  when it comes  to how data is stored and operated. 
            
Methods     -   Are defined within classes.
                The first parameter is usually self.
                MUST be called on an object.
                
    
Attribute.  -   Is a variable that belongs to an object or a class.    
                The data stores in an object.
                The data stored in an object is usually defined by __init__ or other override methods.
                
Functions   -   Standalone blocks of code that are not inside of a class.
                Don't use the self, unless the function is inside of a class.
                There is a  difference between Functional Programming && Object Oriented Design and when it comes  to how data is stored and operated.   
                Data hiding is not possible.
"""

class ClassDistinction:
    def __init__(self, x=0, y=0): #Attribute data for the object.
        self.x = x
        self.y = y

def FunctionDistinction(): #Outside any class, no ref. to self.
    results=1+1
    return results

def main():
    function = FunctionDistinction()
    print(function," - Is what was returned from the function.")

main()

class ClassConstructor:
    def __init__(self): #?
        pass
    def constructor(self): # create an object.
        pass
    def pensize(self): ## modify the pensize
        pass

tess = ClassConstructor() #Use the classConstructor to make the object tess.
tess.pensize() # Call the pensize method on the object tess.


tessy = Turtle() #Using an actual classConstructor from the turtle module.
tessy.pensize(10) #Calling the real pensize method on the object tess.

########## BREAK

"""
Question 5
What is the function of the readline() method? | 
The .readline() method acts on "file-like" objects. 
However, in order to access the readline() a file object must be acted on. 

It reads each line from the file, line-by-line and stops at the new-line character '\n' 

Example via System32 and Python Interpreter.
>>> open("DumpStack.log")
<_io.TextIOWrapper name='DumpStack.log' mode='r' encoding='cp1252'>

"""

#open("DumpStack.log") #Missing PATH.
#open('/C:/DumpStack.log','r') #Error 22 - This is not the correct way to write a Windows File Path in Python.
#open(r"C:\DumpStack.log", "r") #Error 13 - Permission denied: 'C:\\DumpStack.log'
with open(r"C:\Scripts\DumpStack.log","r") as f: #Open and name the object.
    print("Results are:",f.readline())

test = open(r"C:\Scripts\DumpStack.log","r")
print("Test results are:",test.readline())


########### BREAK ###########
"""
Question 6
Reading the function definition below, what is the expected output?

a. Python is fun
b. Hello, world!
c. Hello, world!\nPython is fun.\n 
d. sample.txt 
"""
# Primary Code:
#def write_and_read():
    #open("sample.txt", "w") as file: #missing <with> open("sample.txt", "w") as file:
        #file.write("Hello, world!\n") #Indent error.
    #file.write("Python is fun.\n")

    #with open("sample.txt", "r") as file:
       #content = file.read() #Storing mutated file as content variable.
       #return content # function returns the result of the process.

 #print(write_and_read())


def write_and_read():
    with open("sample.txt", "w") as file:
        file.write("Hello, world!\n")
        file.write("Python is fun.\n")

    with open("sample.txt", "r") as file:
        content = file.read()

    return content


print(write_and_read())

"""
Question 7
How is a file found inside of an operating system, (by programs?) |
a. (The file is found by getting its) location on the disk (according to its) path.
b. (The file is found by) looking inside the drive.
c. (The file is found by) searching for it in folders.
d. (The file is found by) clicking and dragging from the folder. 
"""

"""
Question 8
Are Data files (a type of text file) that is filled with characters?
True - Data file can be text files that are filled with human-readable characters [letters, numbers, symbols]
However, not all data files are .txt files, some are [.csv,.json,.xml].
These can be open by programming languages, read from and edited.

False - 
However, not all data files are text files. 
Some are [.exe, .jpg, .mp3]
These data files are filled with non-human-readable characters due to Binary encoding, 
missing byte maps between character:byte, or special header information that tells 
a program how to interpret the file.

EXAMPLE: Opening - C:\~\..\OTele\opushutil.exe 
Returns:
â-                'qû‘~9-{NöÍ‰Ócv$2ó¸.2·â-                'qû‘~9-{NöÍ‰Ócv$2ó¸.2·          ÿÿÿÿÿÿÿÿÿÿÿÿ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

"""
######### BREAK
"""
QUESTION 9 - Abs. vs. Relative file Paths.
"""

"""
QUESTION 10.
True or False: Will it still be possible to refer to ‘fileref’ later on in the code? 
True -  If the open function is being called within the same directory.
False - In this context, the open function does not have a path to the .txt file; therefore it will not 
be possible for fileref.close() to run, since the open() function will not work.
"""

# BROKEN
#fileref = open("ccdata.txt", "r")
#fileref.close()

# WORKING
test = open(r"C:\Scripts\ccdata.txt","r")
print("Test results are:",test.readline())
test.close()

############ BREAK ############## RQ13.
