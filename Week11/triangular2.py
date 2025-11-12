import sys


def main(number):
    """
    Print out the triangular number of
    number (sum of natural nums from 0 to number)
    using tail recursion
    Number -> None)
    """
    print(tri_num(number, 0, 0))


def tri_num(number, counter, total):
    if (counter == number):
        return total
    else:
        counter += 1
        total = total + counter
        return tri_num(number, counter, total)


main(int(sys.argv[1]))
# This recursion works not like stack because each
# call of the function will be excuted with
# arithmetic and no need to wait for the last
# call function. This will not take the space in
# the CPU.
# Tail recursion: No need to do anything about the
# last call of the function with previous recursions.

# Tail call optimization
