def setup():
    size(500, 300)
    noStroke()
    fill(255, 255, 0)
# setup() will only be called once

def draw():
    background(0, 255, 255)
    ellipse(mouseX, mouseY, 50, 50)
    # draw() will repeatedly run very fast
    # mouseX / Y are special built-in variables
    
  
    
