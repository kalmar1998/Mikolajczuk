add_library('pdf')

def wasy():
    noFill()
    stroke(0)
    strokeWeight(5)
    beginShape()
    curveVertex(10, 10)
    curveVertex(60, 430)
    curveVertex(246, 430)
    curveVertex(100, 100)
    endShape()
    
    beginShape()
    curveVertex(492, 0)
    curveVertex(432, 430)
    curveVertex(246, 430)
    curveVertex(200, 0)
    endShape()

def okulary():
    fill(0)
    noStroke()
    beginShape()
    curveVertex(316, 0)
    curveVertex(100, 314)
    curveVertex(246, 314)
    curveVertex(0, 0)
    endShape()
    
    fill(0)
    beginShape()
    curveVertex(316, 0)
    curveVertex(392, 314)
    curveVertex(246, 314)
    curveVertex(316, 0)
    endShape()

def setup():
    global img
    size(492, 633)
    img = loadImage("zdjecie.jpg")
    image(img, 0,0,width, height) # dzięki temu obraz załąduje też na wejściu w program i widzimy na czym działamy

def draw():
    global img
    
    if keyPressed:
        beginRecord(PDF, "out.pdf") # tak będzie zgrabniej :)
        image(img, 0,0,width, height)
        if key=='1':
            wasy()
        elif key=='2':
            wasy()
            okulary()
        endRecord()

                
def mousePressed():
    exit()
    
# 2pkt
