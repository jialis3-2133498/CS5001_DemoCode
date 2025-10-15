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
    print(
        list(
            filter(
                lambda x: math.sqrt(x).is_integer(),
                # lambda x: math.sqrt(x) == math.floor(math.sqrt(x)),
                [int(n) for n in numbers]
            )
        )
    )


# def is_square(num):
#     """
#     Determine whether a number is a perfect square
#     """
#     # for d in range(1, int(math.sqrt(num)+1)):
#     #     if num == d**2:
#     #         return True
#     # return False
#     return math.sqrt(num).is_integer()


main(sys.argv[1:])
