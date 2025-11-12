import sys

sys.path.append("..")  # Lets us import from the parent directory
# Either of the following Stack imports will work identically
from stack_python_list import Stack  # noqa: E402
# from stack_linked_list import Stack  # noqa: E402


class AnBn:
    """Class for evaluating strings of N a's followed by N b's"""
    def __init__(self):
        self.stack = Stack()
        self.anbn_dict = dict()

    def accept(self, in_string):
        """Takes a string and returns a boolean
indicating whether the string matches the pattern"""
        # TODO:
        # Use a stack to evaluate the pattern.
        # Return True if in_string matches a^nb^n pattern
        # False otherwise. Must work with either implementation
        # of Stack
        seen_b = False
        if not in_string:
            return True
        for i in in_string:
            if i not in self.anbn_dict:
                self.anbn_dict[i] = 1
            else:
                self.anbn_dict[i] += 1
            if i == "a":
                if seen_b:
                    return False
                self.stack.push("a")
            elif i == "b":
                seen_b = True
                if self.stack.is_empty():
                    return False
                self.stack.pop()
            else:
                return False
        if self.anbn_dict.get("a", 0) != self.anbn_dict.get("b", 0):
            return False
        return self.stack.is_empty()

    def clear(self):
        """Clear the stack at the end of each checker"""
        self.stack = Stack()
