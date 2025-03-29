######################################################################
# Authors: Arbjosa Halilaj
# Usernames: halilaja
#
# Assignment: HW05: Funky Functions, Fun Exams
# Purpose:  Test the function by function designer.
#######################################################################
# Acknowledgements: hw_05_funky_functions_suite
########################################################################
from inspect import getframeinfo, stack

from chapter_6_function import *


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

def chapter_6_suite():
    """
    The test_suite function utilizes the testit() function,
    and is designed to test the chapter_6_function function.

    :return: None
    """
    print("\nRunning the chapter_6_function_test_suite().")
    ##########################################
    #valid input test
    unittest(multiple_Choice_Question() == "A") #expected

    #unexpected input tests
    unittest(multiple_Choice_Question() == "Wrong") # Runs the multiple choice function in chapter 6 function.py, and If a non existent choice is passed, an error will be generated.
    unittest(multiple_Choice_Question() == "Wrong") #another invalid choice

    #incorrect type tests
    # unittest(multiple_Choice_Question(3.14) == "Wrong") #float instead of string
    # unittest(multiple_Choice_Question(["A"]) == "Wrong") #list instead of string

    ##########################################
    print("\nEnding the chapter_6_function_test_suite()).")


def main():
    """
    A program that checks the function.

    :return: None
    """
    chapter_6_suite()


if __name__ == "__main__":
    main()
