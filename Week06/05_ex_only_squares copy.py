import sys
import math

# Write a program that takes a series of numbers as
# command line arguments and prints out a list of only
# those numbers that are perfect squares (i.e.
# the product of an integer with itself).

# Use "filter". You may define any helper functions
# you need separately or use a lambda expression. If
# you succeed using one approach, see if you can
# solve it using the other approach also.

# Example usage:
# $ python 05_ex_only_squares.py 10 5 16 36 8 4 9
# $ [16, 36, 4, 9]


def main(numbers):
    """
    Prints out perfect squares
    [Number] -> None
    """
    def is_perfect_sqrt(numbers):
        for each_num in numbers:
            each_num = int(each_num)
            if math.sqrt(each_num.is_integer()):
                return True
            return False
    new_nums = filter(
        is_perfect_sqrt,
        numbers
    )
    return print(list(new_nums))


main(sys.argv[1:])
