######################################################################
# Author: Dr. Scott Heggen               TODO: Change this to your names
# Username: heggens                      TODO: Change this to your usernames
#
# Assignment: HW04: A Bug's Life
#
# Purpose: This program is designed to demonstrate testing of the of Boolean functions
# and the modulus (%) operator which gives the remainder following a division
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


def is_even_test_suite():
    """
    The test_suite function utilizes the testit() function,
    and is designed to test the is_even() function, returning True
    only when the input is even.

    :return: None
    """
    print("\nRunning is_even_test_suite().")

    # testing of positive integers
    unittest(is_even(1) == False)
    unittest(is_even(2) == True)
    unittest(is_even(10) == True)
    unittest(is_even(99999) == False)
    
    # Another way to implement the four tests above is the following:
    # unittest(not is_even(1))
    # unittest(is_even(2))
    # unittest(is_even(10))
    # unittest(not is_even(99999))

    # testing of 0 and negative integers
    unittest(is_even(0) == True)
    unittest(is_even(-1) == False)
    unittest(is_even(-2) == True)
    unittest(is_even(-11111) == False)

    # What should the is_even function do to handle this case?
    unittest(is_even(1.1) == False)

    # And these cases? (Uncomment them to see what happens)
    # unittest(is_even("hi") == False)
    # unittest(is_even(True) == False)

    print("Run of is_even_test_suite() complete.")


def is_even(num):
    """
    Function intended to take an integer as input. Returns True if even and False if odd

    :param num: the integer to be tested
    :return: Boolean value representing if the number is even or not
    """
    if int(num) % 2 == 0:
        return True
    else:
        return False


def main():
    """
    This main function is intended to test the correctness of the is_even function
    :return: None
    """

    is_even_test_suite()


if __name__ == "__main__":
    main()
