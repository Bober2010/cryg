x = 1000
z = 1000
def setup():
    size(600,600)
def draw():
    global x,z
    background(100)
    ellipse(300,300,x,z)
    x -= 5
    z -= 5
