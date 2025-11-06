# flake8: noqa


def setup():
    size(500, 300) # noqa : F821
    noStroke() # noqa : F821
    fill(255, 255, 0) # noqa : F821
# setup() will only be called once


def draw():
    background(0, 255, 255) # noqa : F821
    ellipse(mouseX, mouseY, 50, 50) # noqa : F821
    # draw() will repeatedly run very fast
    # mouseX / Y are special built-in variables
