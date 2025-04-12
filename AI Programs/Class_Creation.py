class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(f"The value is: {self.value}")

# Creating an instance of MyClass
obj = MyClass(10)
obj.display_value()  # Output: The value is: 10



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

###################### MAYBE USEFUL FOR THE OBJECT IN THE MAZE ########


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
