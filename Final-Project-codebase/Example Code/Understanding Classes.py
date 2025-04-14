class Simple:  # creates an empty class
    pass

a = Simple()   # creates a Simple object and assigns it to variable a
b = Simple()   # creates a Simple object and assigns it to variable b

a.x = 5        # sets x attribute of whatever object is assigned to a to 5
b.x = 5        # sets x attribute of whatever object is assigned to b to 5

print(a.x)     # prints x attribute of watever object is assigned to a
print(b.x)     # prints x attribute of watever object is assigned to b


#===============
""" CAUTION: Creating a class with just a pass statement is misleading when
learning how to use classes, and instance variables. 
Below is an example of a class with a single instance variable.
In it each object is created from this class gets its own version of any
instance variables that are used in the class"""

class Simple:
    # Pass in some starting value
    def __init__(self, starting_value): ## __init__ is simply a method that gets called when the object is created  it's also where the construction parameters are received
        # store that value in an instance variable
        self.x = starting_value

    def square(self):
        # use the saved instance variable to compute a square
        squared_value = self.x * self.x
        return squared_value

object_a = Simple(5)
object_b = Simple(10)

print(object_a.x)
print(object_b.x)

print(object_a.square())
print(object_b.square())

####################

class Simple:  # creates a class named Simple
    def __init__(self):  # defines our constructor
        """
        this is our constructor,

        python passes the respective instance to us here and
        we receive it using self which is our method/function argument
        """
        self.x = 5  # sets instance's x attribute to 5


a = Simple()  # creates a Simple object and assigns it to variable a
b = Simple()  # creates a Simple object and assigns it to variable b

print(a.x)  # prints x attribute of whatever object is assigned to a
print(b.x)  # prints x attribute of whatever object is assigned to b