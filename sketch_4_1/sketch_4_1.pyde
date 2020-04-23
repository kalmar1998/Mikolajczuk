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

def draw():
    global img
    
    if keyPressed:
        if key=='1':
            beginRecord(PDF, "out.pdf")
            image(img, 0,0,width, height)
            wasy()
            endRecord()
        elif key=='2':
            beginRecord(PDF, "out.pdf")
            image(img, 0,0,width, height)
            wasy()
            okulary()
            endRecord()

                
def mousePressed():
    exit()
