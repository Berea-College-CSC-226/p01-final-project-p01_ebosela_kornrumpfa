######################################################################
# Authors: Dr. Scott Heggen        TODO: Change this to your names
# Username: heggens                TODO: Change this to your usernames
#
# Assignment: HW05: Funky Functions, Fun Exams Test Suite
# Purpose:  Test suite to test the willoughby_wallaby function in hw05_funky_functions.py
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import sys
from inspect import getframeinfo, stack

from hw05_funky_functions import *


def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0]) #This is new!
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def funky_functions_suite():
    """
    The test_suite function utilizes the testit() function,
    and is designed to test the willaby_wallaby() function.

    Using this function to test the willaby_wallaby() function.

    :return: None
    """
    print("\nRunning the funky_functions_test_suite()).")
    ##########################################
    unittest(willoughby_wallaby("Scott") != "Wott")      # Tests consonant blend
    unittest(willoughby_wallaby("Felix") == "Welix")     # Tests non-consonant blend
    unittest(willoughby_wallaby("Oscar") == "Woscar")    # Tests a case that worked, but is this correct?
    unittest(willoughby_wallaby("Isaac") == "Wisaac")    # How about this one?
    unittest(willoughby_wallaby("Norah") == "Worah")     # I have to test all my children, right?
    unittest(willoughby_wallaby("Jo") == "Wo")           # Tests two letters only
    unittest(willoughby_wallaby("") == False)            # Tests weird cases, such as no input. Is this what we really wanted?
    # unittest(willoughby_wallaby(555) == "W")           # Tests an input with a type we didn't expect. Bad results?
    # unittest(willoughby_wallaby([1,2,3]) == "W")       # Another bad type test... how should we handle cases like this?

    ##########################################
    print("\nEnding the funky_functions_test_suite()).")


def main():
    """
    A fun little program that sings the Willabee Wallabee song.

    :return: None
    """
    funky_functions_suite()


if __name__ == "__main__":
    main()
