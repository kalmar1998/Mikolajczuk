def setup():
    rectMode(CORNER)
    size(500,500)
def draw():
    if mousePressed:
        circle(mouseX, mouseY, 50)
        c = color(120,300,24)
        fill(c)
    
    
    
