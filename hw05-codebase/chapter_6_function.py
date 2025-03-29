######################################################################
# Authors: Antonio K.
# Usernames: kornrumpfa
#
# Assignment: HW5_Function_Design_Unit_Test
# Purpose:  Creating a frutiful function.
######################################################################
# Acknowledgements:
#   Original Author: Antonio K.
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################



'''

Function Designer: Create a program that will satisfy the following:
Ask the user a multiple choice question related to your chapter.
     Based on chapter 6.2.... the following question:
        ......... We are still trying to understand what makes
        a function fruitful or not. We are going to used the code block:
        import math
        print(math.pow(2,3))
        We started to look at the help module for math.pow, and
        found the following: 'pow(x, y, /) # Will Return x**y (x to the power of y).

            [A]. If we use the pow function and pass a float, will it work?
            [B]. If we use character in the pow function will it work? What is returned? TypeError: must be real number, not str

Use a combination of print and input statements to format it nicely!
Use a fruitful function to:
Take in the user's response as an input parameter.
Checks their answer and returns appropriately helpful feedback (i.e., if the answer is right, give them more information; if the answer is wrong, give them some help towards the right answer). Return this feedback as a string.
'''


'''
Main explained:
1. The main function first prompt the user to determine what a valid input into the math.pow() function is.
2. The multiple_Choice_Question() function then ask the user to select a value: A,B,C,D - and once it is select that value is returned. (Making it fruitful) The value is stored into a variable inside of main().
3. The value returned from the user selection is then used an an input parameter for the userChoice() function; which evaluates if the input is valid or invalid.
'''
def main():
    print("If you use the pow function, what inputs are valid? A. "
          "Integers | B. Floats | C. Characters | D. Lists  ")
    #multiple_Choice_Question() #TypeError: multiple_Choice_Question() missing 1 required positional argument: 'A'
    user_input = multiple_Choice_Question()  # Get the result from the first function
    userChoice(user_input)  # Get feedback based on the selection

# STEP 1
# 2....3

# def multiple_Choice_Question():
#     #input("If you use the pow function, what inputs are valid?")
#     userInput = input()
#     if userInput == "Integers":
#         print("Integers")
#     elif userInput == "Floats":
#         print("Floats")
#     elif userInput == "Lists":
#         print("Lists")
#     else:
#         print("Wrong")
#     #A == "Integers"....
#     #B == "Floats"....
#     #C == "Characters"...
#     #D == "Lists"....
#     return

'''
How to make this fruitful?
'''
def multiple_Choice_Question():
    # Ask the user for input
    userInput = input("Please choose an option (A, B, C, D): ")
    if userInput == "A":
        #print("Integers")
        return "A"
    elif userInput == "B":
        #print("Floats")
        return "B"
    elif userInput == "C":
        #print("Characters")
        return "C"
    elif userInput == "D":
        #print("Lists")
        return "D"
    else:
        #print("Wrong input")
        return "Wrong"

def userChoice(User_Selection):
    if User_Selection == "A":
        print("Integers can be used")
    elif User_Selection == "B":
        print("Floats can be used")
    elif User_Selection == "C":
        print("Characters cannot be used")
    else:
        print("Lists cannot be used")

if __name__ == "__main__": # The following ensures that the main function is called only when the script is executed directly
    main()