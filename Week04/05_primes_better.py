import sys
import math


def main(max_val):
    """
    Print out prime number from
    2 to max_val
    """
    START_VAL = 2
    START_DIVISOR = 3

    print(START_VAL)

    for candidate in range(START_VAL+1, max_val, 2):
        is_prime = True
        square_root = math.sqrt(candidate)
        div = START_DIVISOR
        while (div < square_root and is_prime):
            if (not (candidate % div)):
                is_prime = False
            div += 2
        if (is_prime):
            print(candidate)


main(int(sys.argv[1]))
