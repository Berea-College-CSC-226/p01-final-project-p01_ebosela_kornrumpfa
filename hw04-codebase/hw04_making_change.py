######################################################################
# Author: Dr. Scott Heggen              TODO: Change this to your names
# Username: heggens                     TODO: Change this to your usernames
#
# Assignment: HW04: A Bug's Life
#
# Purpose: Demonstrates the use of division and modulus operations,
#
# This program INCORRECTLY calculates the largest number of
# quarters, dimes, nickels and pennies needed to make that change in coins.
# It is designed to show a subtle error and the value of unit tests.
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

from inspect import getframeinfo, stack


def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def pennies_test_suite():
    """
    The test_suite function utilizes the testit() function,
    and is designed to test the is_i_steal_pennies() function,
    returning True only when the input is even.

    :return: None
    """

    print("\nRunning pennies_test_suite()).")

    # Remember that I_steal_pennies() returns a list in the form [num_quarters, num_dimes, num_nickels, num_pennies]
    unittest(i_steal_pennies(0.88) == [3, 1, 0, 3]) # because 0.88 = 3*0.25 + 1*0.10 + 0*0.05 + 3*0.01
    unittest(i_steal_pennies(0.89) == [3, 1, 0, 4]) # because 0.89 = 3*0.25 + 1*0.10 + 0*0.05 + 4*0.01

    # TODO ADD MORE UNIT TESTS HERE!

    print("Run of pennies_test_suite() complete.")


def i_steal_pennies(to_change):
    """
    This function looks like it should take a floating point number to_change
    and return a list of how much change to give as:

    [num_quarters, num_dimes, num_nickels, num_pennies]

    However, it compounds small truncation errors of the floating point arithmetic.
    Such errors are subtle and can be quite hard to debug, so unit tests are useful!
    A better algorithm would be to use integers instead of floats,
    but the point of this code is to demonstrate the invisible error.
    It is also to help you learn the value of unit tests.

    :param to_change: a float representing an amount of money
    :return: A list of the number of quarters, dimes, nickels,
             and pennies representing the amount of money above
    """
    # TODO DO NOT CHANGE THIS FUNCTION!

    # Initialize values
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0

    # Compute numbers of each coin type
    if to_change >= 0.25:
        num_quarters = int(to_change / 0.25)
        to_change = float(to_change % 0.25)

    if to_change >= 0.1:
        num_dimes = int(to_change / 0.1)
        to_change = float(to_change % 0.1)

    if to_change >= 0.05:
        num_nickels = int(to_change / 0.05)
        to_change = float(to_change % 0.05)

    if to_change >= 0.01:
        num_pennies = int(to_change / 0.01)

    return [num_quarters, num_dimes, num_nickels, num_pennies] # this order will be retained


def print_change(coinlist):
    """
    This program expects an input coin list of [num_quarters, num_dimes, num_nickels, num_pennies]
    It will print the values out for the user.

    :param coinlist: A list of the number of quarters, dimes, nickels,
                     and pennies representing the amount of money above
    :return: None
    """

    print("Can you tell if I am an honest machine? ")
    print("Give out the following change: ")
    value_list = ["Quarter(s): ", "Dime(s): ", "Nickel(s): ", "Penny(s): "]
    for item in range(4):
        print(value_list[item] + str(coinlist[item]))


def user_input_of_coins():
    """
    This function is created just for interactive fun.
    This would be the normal mode of operation (not testing)

    :return: None
    """

    the_total = float(input("Input total amount of dollars and cents (e.g., 2.45): "))
    print("You have asked how to make " + str(the_total)+ " in change.")
    list_of_change = i_steal_pennies(the_total)
    print_change(list_of_change)


def main():
    """
    This main function is intended to test the correctness of the i_steal_pennies() function

    :return:
    """

    pennies_test_suite()


if __name__ == "__main__":
    # If you run this code directly (i.e., hit the green run button on this file),
    # it runs the test suite. If you call this code from another file
    # (e.g., t04_making_change_interactive.py), it will NOT run the test suite
    main()
