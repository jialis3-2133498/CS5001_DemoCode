# A program implementing the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula

from math import sqrt


def main():
    PRECISION = 3
    a = float(input("Enter the coefficient of x squared: "))
    b = float(input("Enter the coefficient of x: "))
    c = float(input("Enter the constant: "))

    # Use the quadratic formula to compute the roots.
    # Assumes a positive discriminant.
    TWO = 2
    FOUR = 4

    discriminant = b**TWO - (FOUR * a * c)
    root1 = ((-b) + sqrt(discriminant)) / (TWO * a)
    root2 = ((-b) - sqrt(discriminant)) / (TWO * a)

    print("Root #1:", round(root1, PRECISION))
    print("Root #2:", round(root2, PRECISION))


main()

# Test with
# 1, 3, -4
# 2, -4, -5
# 1, -1, -3
