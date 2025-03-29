############ ANTONIO KORNRUMPF ###############################
############ HW04 - A BUGS LIFE ##############################


"""



1. Ask the user to enter their birth year.
[?] Can I implement this as code? | YES // NO.
    YES.

1a. CONVERT the year to 4 (individual digits) and SUM those and | RETURN an output [A]
to be used elsewhere.
[?] Can I implement this as code? | YES // NO.
    YES.

2. Ask the user to enter their birth month.
[?] Can I implement this as code? | YES // NO.
    YES.

2a. CONVERT the birth month from month to (individual) digits and SUM the digits.
[EXCEPT IF] the month == 11, then don't SUM. | RETURN an output [B]
[?] Can I implement this as code? | YES // NO.
    YES.

3. Ask the user to enter their birthday day.
[?] Can I implement this as code? | YES // NO.
    YES.

3a. COVERT, the day to individual digits and SUM them.
[EXCEPT IF] the day == 11, 22 | RETURN an output [C]
[?] Can I implement this as code? | YES // NO.
    YES.

4. SUM [A] + [B] + [C] = [D]
[?] Can I implement this as code? | YES // NO.
    YES.


4a. Break this output [D] into individual digits and sum them.
[EXCEPT IF] the output [D] is 11, 22, 33.
[?] Can I implement this as code? | YES // NO.
    YES.

"""


"""
SECTION #1
1. Ask the user to enter their birth year. 
[?] Can I implement this as code? | [YES] // NO.
[?] HOW. 
Started by creating a variable to store an input request as an integer. 
Some automation within Pycharm completed out the code, likely referencing my PLAN.
Ran the code, but observed some errors in regard to inputs:
1. Input length limitation. Should I set a restriction to a max of 4 numbers?
2. What if the user attempts to enter their birth month as a string "January"?
2a. Does the assigment require that this be taken as a string and then converted?

"""


""" 
/ = Nested code inside the main function.
/ = Defining another function that will be called back into main, tested and it runs.
? = How do I take the input integer and then parse the numbers from 1991 to 1-9-9-1?
    A few methods I've been given to do this are to "convert the integer into a string, and
    add dashes between each digit." This does not allow me to add the numbers together.
    A second option relies on storing each digit as a unique variable and then summing those values.
    To do this, I must convert the integer back into a string and then map numbers to
    a character. I can then sum each of these characters.
    I am doing some data conversion, but now I am stuck with a list that of elements, but I don't 
    know how to act on them. My first thought is to use a for loop.
    I've done that in (2) ways.
    Module 1 is partial complete. I should be able to re-use this. 
    [?] How do I use returns correctly? 
    EXAMPLE: the If the input is not a master number, convert the input to digits and return the sum of the digits.

-----------------SECTION #1 SUMMARY
    Got some additional practice defining functions, using built-in functions within Python to
    convert data types. Worked with control block if-then-else; and for loops.
    Still need some clarification on how to properly use returns. 
   
"""
def main():
    A=module1()
    B=module2()
    C=module3()
    totals=A+B+C
    updatedTotals = module4(totals) # Passes the updated totals into module5.
    module5(updatedTotals)


def module1():
    birth_year = int(input('Enter your birth year: '))  # This function does take an integer as an input parameter.
    str_birth_year = str(birth_year) # converts the birth year int into a string.
    #list = map(int, str_birth_year)
    character_list=list(map(int, str_birth_year)) #Successfully converted an INT input into a string. Converted that string back to an INT. Used the map function to transform the INT elements into individual digits. Then pass this output into a list.
    #print(list) # Generated output "<map object at 0x000001A5F2F308B0>" when list = map(int, str_birth_year) was used.
    #print(birth_year)
    #print(type(str_birth_year)) #Type checker.
    #print(type(character_list)) #Outputs a list.

   # for digit in character_list: #### Loop attempt 1, but printed 4 outputs for each position in the list.
    #    print(sum(character_list))
    #for digit in range(1): #Simpler only runs once.
     #   print(sum(character_list))
    for digits in range(1):
        storage = sum(character_list)
        if storage % 11 == 0:
            print('Your birth year is a master number.')
            return storage
        elif storage % 22 == 0:
            print('Your birth year is a master number.')
            return storage
        elif storage % 33 == 0:
            print('Your birth year is a master number.')
            return storage
        else:
            storage = (int(sum(character_list)))
            #print('Your birth year' + storage + 'is a working number.')
            print('Your birth year is a working number.')
            #print(type(storage)) #Type checker.
            #sum(storage)
            #print(storage) To verify sum function.
            return storage

"""
SECTION 2
2. Ask the user to enter their birth month.
[?] Can I implement this as code? | YES // NO.
    YES.
    
2a. CONVERT the birth month from month to (individual) digits and SUM the digits.
[EXCEPT IF] the month == 11, then don't SUM. | RETURN an output [B]
[?] Can I implement this as code? | YES // NO.
    YES.
"""
def module2():
    birth_month = int(input('Enter the number of your birth month: '))
    if birth_month % 11 == 0: #Uses modulus (%) to determine if the input is a multiple of 11 (i.e. 11 or 22 or 33). If it is and is 33 or less, the input is a master number, so simply return the master number.
        print('Your birth month is a master number.')
        return birth_month
    else:
        print('Your birth month is a working number.')
        str_birth_month = str(birth_month) # Convert int to a string.
        storage1 = list(map(int, str_birth_month))  #Coverts the string into a list of numbers.
        numberSum = sum(storage1) #If the input is not a master number, convert the input to digits and return the sum of the digits.
        #print(numberSum)  Testing the output to see if a sum is returned.
        return numberSum



"""
SECTION 3
3. Ask the user to enter their birthday day.
[?] Can I implement this as code? | YES // NO.
    YES.

3a. COVERT, the day to individual digits and SUM them.
[EXCEPT IF] the day == 11, 22 | RETURN an output [C]
[?] Can I implement this as code? | YES // NO.
    YES.

"""

def module3():
    birth_day = int(input('Enter the two digit number of your birth day: '))

    if birth_day == 11:
        print('Your birth day is a master number.')
        return birth_day
    elif birth_day == 22:
        print('Your birth day is a master number.')
        return birth_day
    else:
        print('Your birth day is also a working number.')
        str_birth_day = str(birth_day)  # Convert int to a string.
        storage2 = list(map(int, str_birth_day))  # Coverts the string into a list of numbers.
        numberSum1 = sum(storage2)
       #print(numberSum1)  #Testing the output to see if a sum is returned.
        return numberSum1

"""SECTION 4
4. SUM [A] + [B] + [C] = [D]
[?] Can I implement this as code? | YES // NO.
    YES.


4a. Break this output [D] into individual digits and sum them.
[EXCEPT IF] the output [D] is 11, 22, 33.
[?] Can I implement this as code? | YES // NO.
    YES.

"""
# This code did not work correctly for all use cases, though I don't understand why???

def module4(totals):
    print("Your life numbers sum to", totals)
    if totals == 11 or totals == 22 or totals == 33:
        print('Your life numbers achieve the mark')
        return totals
    else:
        while totals not in [11,22,33]: #Tried to use a != but this checks against the whole list. Used 'not in' instead.
            str_totals = str(totals)  # Convert int to a string.
            storage2 = list(map(int, str_totals))  # Coverts the string into a list of numbers.
            numberSum = sum(storage2)
            print('Your new life number is', numberSum)
            numberSum += 1
            print("Increased your number to", numberSum)
            totals = numberSum
    return totals

def module5(totals):
    if totals in [11,22,33]:
        print("After some changes, you have a master number.")



# This code ALSO did not work correctly, though I don't understand why.
# def module4(totals):
#     print("Your life numbers sum to", totals)
#
#     # Check if totals is already a master number
#     if totals == 11 or totals == 22 or totals == 33:
#         print('Your life numbers achieve the mark')
#         return totals  # End the function as it's already a master number
#
#     # Loop until we get a master number
#     while totals not in [11, 22, 33]:
#         str_totals = str(totals)  # Convert totals to a string
#         storage2 = list(map(int, str_totals))  # Convert the string into a list of individual digits
#         numberSum = sum(storage2)  # Sum the digits
#         print('Your new life number is', numberSum)
#
#         # If the sum of digits is a single digit (<= 9), increment it
#         if numberSum < 10:
#             numberSum += 1
#             print(f"Single digit detected. Adding 1 to make it {numberSum}.")
#
#         # Update totals with the new sum and repeat the loop
#         totals = numberSum
#
#     # Once the loop finishes, we've reached a master number
#     print(f"Your life number has achieved the master number: {totals}")
#     return totals

### INFINITE LOOP ####
# def module4(totals):
#     print("Your life numbers sum to", totals)
#
#     # Check if totals is already a master number
#     if totals == 11 or totals == 22 or totals == 33:
#         print('Your life numbers achieve the mark!')
#         return totals  # End the function as it's already a master number
#
#     # Loop until we get a master number
#     while totals not in [11, 22, 33]:
#         str_totals = str(totals)  # Convert totals to a string
#         storage2 = list(map(int, str_totals))  # Convert the string into a list of individual digits
#         numberSum = sum(storage2)  # Sum the digits
#         print('Your new life number is', numberSum)
#
#         if numberSum < 10:
#             numberSum += 1  # Increment to avoid getting stuck in single digits
#             print("Non-master detected. Adding 1 to make it",numberSum)
#
#         totals = numberSum #Updates the totals value.
#
#         if totals in [11, 22, 33]:
#             print('Balanced at', totals)
#             #return totals
#         #else:
#             #print('Balanced at', totals)




    # Once the loop finishes, we've reached a master number


main()
