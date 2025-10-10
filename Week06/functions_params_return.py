import math


def main():
    """
    Runs demo functions
    None -> None
    """
    hello_function("World")
    hello_function("Sonething else!")
    my_double_num = double_num(4)
    add_nums(my_double_num, double_num(3))
    no_argv_no_return()
    v1, v2, v3 = multi_value_return()
    print(is_prime(9))

    print(v1)
    print(v2)
    print(v3)


def hello_function(my_argument):
    """
    Prints hello message with argument
    String -> None
    """
    print("Hello, ", my_argument)
    # Every function that has no Return will return none


def double_num(number):
    """
    Double a number
    Return -> Number
    """
    return 2 * number


def add_nums(num1, num2):
    """
    Add two numbers
    Number: Number -> Number
    """
    return num1 + num2


def no_argv_no_return():
    """
    Print a string
    None -> None
    """
    print("There is an IO action with no return value")
    return  # Return will be the end of the function
    print("Hello from beyond excution")  # This will never happen


def multi_value_return():
    """
    Return three values
    Naone -> Chracter Character Number
    """
    return 'a', 'b', 10.5


def is_prime(num):
    """
    Evaluate whether a number is prime
    Integer -> Boolean
    """
    for d in range(2, int(math.sqrt(num+1))):
        if not num % d:
            return False
    return True


if __name__ == "__main__":  # __name__ is the file that is calling
    # "__main__" means this file's name
    main()
