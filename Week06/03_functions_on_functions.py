def main():
    function_caller(f1)  # Pass in function f1
    function_caller_arg(f2, "Hi there")
    print("***")
    function_caller(f3)  # Pass in the whole function f3()-not the return value
    print("***")
    function_caller(f3())  # Pass in the return value of f3()


def function_caller(foo):
    print("I call a function")
    foo()


def function_caller_arg(foo, arg):
    print("I call a function with an argument")
    foo(arg)


def f4():
    print("I am function f4")


def f3():
    print("I am function f3")
    return f4  # Return the f4 function, not the result of f4


def f2(some_string):
    print(f"I am f2, and here is my argument {some_string}")


def f1():
    print("I am function f1")


main()
