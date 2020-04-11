def setup():
    size(400, 400)
    frameRate(60)
    textSize(70)
    global colorX, colorM, colorA
    colorX = color(255, 255, 255)
    colorA = color(90, 255, 190)
    colorM = color(200, 50, 50)
def draw():
    clear() 
    text("A", width/2-50, height/2) 
    text("M",(width/2-50)+70, height/2)
    if mouseX>=width/2-50 and (mouseX<=(width/2-50) +70) and mouseY<=height/2 and mouseY<=(height/2)+70:
         clear()
         text("A", width/2-50, height/2)
         fill(colorX) 
         text("M", (width/2-50)+70, height/2)
         fill(colorA)
    elif keyPressed:
        if key=="m" or key=="M":
            clear()
            text("A", width/2-50, height/2)
            fill(colorM)
            text("M", (width/2-50)+70, height/2)
            fill(colorX)
        elif key == CODED:
            if keyCode == LEFT:
                clear()
                text("A", width/2-50, height/2)
                fill(colorX)
                text("M", (width/2-50)+70, height/2)
                fill(colorM)
            elif keyCode == RIGHT:
                clear()
                text("A", width/2-50, height/2)
                fill(colorA)
                text("M", (width/2-50)+70, height/2)
                fill(colorX)
# brakuje kształtu niestandardowego
# podświetlenie przeskakuje również gdy żadna z liter nie jest zaznaczona i to dopiero po mojej poprawce wcięć
# 1,25pkt
