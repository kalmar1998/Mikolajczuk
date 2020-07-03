posX = 0
posY = 0
punkty = 0
bool=False
czas = 100
szansa = random(0, 100)


class Obiekt(object):
    def __init__(self):
        self.posX=0
        self.posY=0
        
    def obrazek(self):

        self.posX = random(70, width-100)
        self.posY = random(70, height-200)
        global szansa
        szansa = random(0, 100)
        clear()
        
class Kaczka(Obiekt):
    def obrazek(self):
        super(Kaczka,self).obrazek()
        image(loadImage("kaczka2.png"), self.posX, self.posY, 70, 70)
        
class Ryba(Obiekt):
    def obrazek(self):
        super(Ryba,self).obrazek()
        image(loadImage("ryba.png"), self.posX, self.posY, 70, 70)
        
        
        
def setup():
    size(500, 500)
    textSize(20)
    global kaczka, ryba, posX, posY, punkty, szansa
    
    szansa = 100
    punkty = 0
    bool=False
    czas = 100
    kaczka = Kaczka()
    ryba = Ryba()
    
    if szansa >= 0 and szansa <= 65:
        kaczka.obrazek()
    else:
        ryba.obrazek()
        
    
    
def draw():
    global bool, czas, kaczka, ryba, szansa
    
    text("POLOWANIE NA KACZKI!!!  (/^o^)/", width-420, height-450)
    text("[Uzyskaj 20 pkt!]", width - 500, height - 20)
    text("[0 - exit]", width - 86, height - 20)
    text(punkty, width/2, height - 50)
    
    if bool == True:
        
        if szansa >= 0 and szansa <= 65:
            kaczka.obrazek()
        else:
            ryba.obrazek()
            
        text(punkty, width/2, height - 50)
        fill(random(255), random(255), random(255))
        czas = 100
        bool=False   
        
    else:
        czas = czas - 3.75
        
    if czas<=0:
        bool=True
        
def mousePressed():
    global posX, posY, punkty, bool, kaczka, ryba, szansa
    
    if mouseX>=kaczka.posX and mouseX<=kaczka.posX+70 and mouseY>=kaczka.posY and mouseY<=kaczka.posY+70:
        background(random(255), random(255), random(255))
        bool = True
        print("------")
        print("KWAK!")
        print("------")
        global punkty   
        punkty+=1
        
    else:
        print("------")
        print(":(")
        print("------")
        punkty-=1
        if punkty<0:
            punkty=0 
            
    if mouseX>=ryba.posX and mouseX<=ryba.posX+70 and mouseY>=ryba.posY and mouseY<=ryba.posY+70:
        background(random(255), random(255), random(255))
        bool = True
        print("------")
        print("...!")
        print("------")
        global punkty   
        punkty-=1
        if punkty<0:
            punkty=0
            
    if punkty == 20:
        exit()
        
def keyPressed():
    if key == '0':
        exit()
        
 #stworzyłem taki mały projekt, gdyby Pani oceniła, byłoby mi miło
