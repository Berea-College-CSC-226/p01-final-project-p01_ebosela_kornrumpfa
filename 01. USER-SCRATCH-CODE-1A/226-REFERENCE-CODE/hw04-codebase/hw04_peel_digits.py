######################################################################
# Author: Dr. Scott Heggen                TODO: Change this to your names
# Username: heggens                       TODO: Change this to your usernames
#
# Purpose: This program is designed to demonstrate the use of Python's string capabilities
# as a method for peeling digits from an integer
######################################################################
# Acknowledgements:
#   Original Authors: Dr. Mario Nakazawa and Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

from inspect import getframeinfo, stack
import random

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


def peel_digits_test_suite():
    """
    The test_suite function utilizes the testit() function,
    and is designed to test the peel_digits() function,
    returning a list of each digit

    :return: None
    """
    print("\nRunning peel_digits_test_suite()).")

    # Remember that I_steal_pennies() returns a list in the form [num_quarters, num_dimes, num_nickels, num_pennies]
    unittest(peel_digits(1998) == [1, 9, 9, 8])
    unittest(peel_digits(1234567) == [1, 2, 3, 4, 5, 6, 7])

    # TODO ADD MORE UNIT TESTS HERE!

    print("Run of peel_digits_test_suite() complete.")


def peel_digits(num):
    """
    Given a positive integer num, peel_digits returns a list filled with the digits
    eg. given 1984, peel_digits returns the list [1, 9, 8, 4]

    :param num: a positive integer
    :return: a list with each digit as an element in the list
    """
    str_num = str(num)                      # Converts to string to utilize Python's strong string features
    digit_list = []                         # Creates empty list
    for letter in str_num:
        digit_list.append(int(letter))      # Puts each digits into list
    # print(digit_list)                     # Testing
    return digit_list


def print_digits(digit_list):
    """
    Given any list, this function prints each list element

    :param digit_list: a list of digits to print
    :return: None
    """
    for digit in digit_list:
        print(digit)


def random_peeler():
    """
    Function for picking a random year between 1000 and 2018 to peel using the
    peel_digit() function, then printing to the screen.

    :return: None
    """

    year = random.randint(1000, 2018)
    print("\nYear = " + str(year))
    year_list = peel_digits(year)  # Put list returned from function into year_list
    print("\nDigits:")
    print_digits(year_list)


def main():
    """
    This main function is intended to display the capabilities of the peel_digits() and print_digit() functions

    :return: None
    """
    random_peeler()           # Run one or the other by uncommenting/commenting
    # peel_digits_test_suite()    # Run one or the other by uncommenting/commenting


if __name__ == "__main__":
    main()
