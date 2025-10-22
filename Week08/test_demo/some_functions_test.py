import some_functions as sf


def test_multiply_numbers():
    """
    Test the multiply_numbers function
    """
    assert sf.multiply_numbers(5, 10) == 50
    assert sf.multiply_numbers(5, -10) == -50
    assert sf.multiply_numbers(2.5, 2) == 5.0
    assert sf.multiply_numbers(2.5, 0) == 0
    # In command line, type "pytest <file.py>"
    # Or type "pytest" to test all functions in the dict


def test_flatten_list_of_strings():
    """
    Test the flatten_list_of_strings function
    """
    s1 = "hello "
    s2 = "world."
    s3 = "1234"
    list_argument = [s1, s2, s3]
    conc = "hello world.1234"
    assert sf.flatten_list_of_strings(list_argument) == conc
    assert sf.flatten_list_of_strings([]) == ""