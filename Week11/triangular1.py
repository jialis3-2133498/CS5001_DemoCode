import sys


def main(number):
    """
    Print out the triangular number of
    number (sum of natural nums from 0 to number
    Number -> None)
    """
    print(tri_num(number))


def tri_num(number):
    if (number == 0):
        return 0
    else:
        return number + tri_num(number-1)


main(int(sys.argv[1]))
# This recursion works like the stack. The last called function
# must be solved first in order to finish all other function
# calls
# That means the first called function will be stored in the
# memory until the last called function is solved. This will
# require lots of memory storage.
