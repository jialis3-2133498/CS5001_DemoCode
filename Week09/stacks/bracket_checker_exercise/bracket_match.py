import sys

sys.path.append("..")  # Lets us import from the parent directory
# Either of the following Stack imports will work identically
from stack_python_list import Stack  # noqa: E402
# from stack_linked_list import Stack  # noqa: E402


class BracketMatch:
    """Class for evaluating parenthetical strings"""
    def __init__(self):
        self.stack = Stack()
        # TODO:
        # Any necessary or helpful attributes
        # should be set here.
        pass

    def brackets_match(self, in_string):
        """Takes a string and returns a boolean
indicating whether the strings' brackets match"""
        # TODO:
        # Use a stack to evaluate the string.
        # Return True if in_string's brackets match,
        # False otherwise. Must work with either implementation
        # of Stack
        pass

    def clear(self):
        self.stack = Stack()
