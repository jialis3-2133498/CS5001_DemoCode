from foo_class import Foo


def test_constructor():
    """
    Test __init__ method
    """
    TEST_ATTRIBUTE = "test attribute"
    my_foo = Foo(TEST_ATTRIBUTE)
    assert my_foo.bar == TEST_ATTRIBUTE


def test_return_a_sum():
    """Test return_a_sum"""
    my_foo = Foo("Test attribute")
    assert my_foo.return_a_sum(1, 2, 3) == 6
    assert my_foo.return_a_sum(-1, 0, 0) == -1
