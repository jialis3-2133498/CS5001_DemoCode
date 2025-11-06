class Spot:
    """
    A spot object with an x and y position that draws
    itself on the screen
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        noStroke() # noqa : F821
        fill(255) # noqa : F821
        circle(self.x, self.y, 95) # noqa : F821
        fill(0) # noqa : F821
        circle(self.x, self.y, 80) # noqa : F821
        fill(255) # noqa : F821
        circle(self.x, self.y, 65) # noqa : F821
        fill(255, 0, 0) # noqa : F821
        circle(self.x, self.y, 50) # noqa : F821
        fill(255) # noqa : F821
        circle(self.x, self.y, 25) # noqa : F821
        fill(0) # noqa : F821
        circle(self.x, self.y, 10) # noqa : F821
        fill(0) # noqa : F821
