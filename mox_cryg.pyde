x = 0
y = 0
def setup():
    size(400,400)
def draw():
    global x,y
    background(100)
    ellipse(x,y,20,20)
    x += 1
    y += 1
    
    
