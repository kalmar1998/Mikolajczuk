global side
r = 50    

global x
xpos = 0 

global y
y = 0 

global x1
x1 = 1

global y1
y1 = 1

def setup():
    global x, y
    size(640, 360)
    frameRate(120)
    x = width/2
    y = height/2

def draw():
    
    background(100)
    paleta_kolorow = {"zielony":(0,255,0), "niebieski":(0,0,255), "szary":(120)}
  
    global x, y, x1, y1, r
    x = x + x1 
    y = y + y1
    
    if (x > width-(r/2) or x < r/2):
        x1 *= -1
        fill(*paleta_kolorow["zielony"])
            
    if (y > height-(r/2) or y < r/2):
        y1 *= -1
        fill(*paleta_kolorow["niebieski"])
        
    circle(x, y, r)

def mousePressed():
    exit()
