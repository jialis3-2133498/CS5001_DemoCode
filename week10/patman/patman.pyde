WIDTH = 500
HEIGHT = 500
PATMAN_SIZE = 100
PATMAN_COLOR = (1.0, 1.0, 0.0)
SPEED = 3
x = WIDTH/2
y = HEIGHT/2
x_add = 0
y_add = 0

def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)
    fill(*PATMAN_COLOR)
    noStroke()
    
def draw():
    global x, y
    background(0)
    x = x + x_add
    y = y + y_add
    
    # Handle Right Direction edge
    if (x > WIDTH + (PATMAN_SIZE / 2)):
            # Reset x value to the left side
        x = PATMAN_SIZE / 2
    # if patman is overlapping the right edge
    elif (x > WIDTH - (PATMAN_SIZE / 2)):
        patman(x - WIDTH, y)
    
    # Handle Down direction edge
    if (y > HEIGHT + (PATMAN_SIZE / 2)):
        # Reset x value to the left side
        y = PATMAN_SIZE / 2
    # if patman is overlapping the right edge
    elif (y > HEIGHT - (PATMAN_SIZE / 2)):
        patman(x, y - HEIGHT)
    
    # Handle Left direction edge 
    if (x < - (PATMAN_SIZE / 2)):
    # Reset x value to the left side
        x = WIDTH - (PATMAN_SIZE / 2)
    # if patman is overlapping the right edge
    elif (x < (PATMAN_SIZE / 2)):
        patman(x + WIDTH, y)
    
    # Handle Up direction edge
    if (y < - (PATMAN_SIZE / 2)):
    # Reset x value to the left side
        y = HEIGHT - ( PATMAN_SIZE / 2)
    # if patman is overlapping the right edge
    elif (y < (PATMAN_SIZE / 2)):
        patman(x, y + HEIGHT)
    
    patman(x, y)
    
def patman(x, y):
    """Draw patman to the screen"""
    arc(x, y, PATMAN_SIZE, PATMAN_SIZE,
        radians(45),
        radians(315))
def keyPressed():
    global x_add, y_add
    if (key == CODED):
        if (keyCode == DOWN):
            x_add = 0
            y_add = SPEED
        elif (keyCode == UP):
            x_add = 0
            y_add = -(SPEED)
        elif(keyCode == LEFT):
            x_add = -(SPEED)
            y_add = 0
        elif (keyCode == RIGHT):
            x_add = SPEED
            y_add = 0
    
