import sys

sys.path.append("..")  # Lets us import from the parent directory
# Either of the following Stack imports will work identically
from stack_python_list import Stack  # noqa: E402
# from stack_linked_list import Stack  # noqa: E402


class AnBn:
    """Class for evaluating strings of N a's followed by N b's"""
    def __init__(self):
        self.stack = Stack()

    def accept(self, in_string):
        """Takes a string and returns a boolean
indicating whether the string matches the pattern"""
        # TODO:
        # Use a stack to evaluate the pattern.
        # Return True if in_string matches a^nb^n pattern
        # False otherwise. Must work with either implementation
        # of Stack
        return False

    def clear(self):
        """Clear the stack at the end of each checker"""
        self.stack = Stack()
