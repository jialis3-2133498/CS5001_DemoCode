v = "This variable is defined globally"


def main():
    """
    """
    f1("x value", "y value")
    print("Main:", v)
    f2("Hello", "World", 3)
    f3()
    print(v)
    f4()


def f4():
    v41 = "value 41"
    v42 = "value 42"

    def f5():
        nonlocal v41
        v41 = "Changed 41"
        v42 = "Changed 42"
        print(f"f5: {v41}")
        print(f"f5: {v42}")

    f5()
    print(f"f4: {v41}")
    print(f"f4: {v42}")


def f3():
    global v
    v = "f3 re-assian global v"  # This v shasows the global v, and f3() no
    # longer can access the global v
    print(f"f3: {v}")


def f2(x, y, z="Default value"):  # z is the Optional input
    print(f"f2: {x}")
    print(f"f2: {y}")
    print(f"f2: {z}")


def f1(x, y):
    print(f"f1: {x}")
    print(f"f1: {y}")
    print(f"f1: {v}")


main()
