x = 200
c = 200
v = 200
b = 200
def setup():
    size(400,400)
def draw():
   global x,c,v,b
   background(100)
   ellipse(c,v,20,20)
   ellipse(x,b,20,20)
   ellipse(c,b,20,20)
   ellipse(x,v,20,20)
   x -= 1
   c += 1
   v -= 1
   b += 1
   
