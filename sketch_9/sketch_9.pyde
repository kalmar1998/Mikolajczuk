

class Kaczka():
    
    def obrazek(self, img):
        self.img = img
        image(loadImage(self.img), 60, 60, 480, 480)
        

              
    def ramka(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        rect(self.v1, self.v2, self.v3, self.v3)
    
        
    def kwadrat(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        rect(self.a1, self.a2, self.a3, self.a3)
        
    def ramka_fill(self, c1, c2, c3):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        fill(c1, c2, c3)
        
def setup():
    background(255, 255, 255)
    textSize(15)
    size(600, 600)
    global kaczka, x
    x = "kaczka_pixel.png"
    kaczka = Kaczka()
   
        
    try: 
        kaczka.obrazek(x)
        kaczka.ramka_fill(15, 41, 255)
        text("obrazek wyswietlil sie prawidlowo", width - 450, height -10)
    
    except:
        
        kaczka.ramka_fill(255, 0, 4)
        text("nazwa obrazka jest nieprawidlowa \n lub obrazka nie ma w folderze", width - 430, height -27)
        kaczka.ramka(45, 45, 510)
        kaczka.ramka_fill(255, 255, 255)
        kaczka.kwadrat(65, 65, 470)
        
    else:
        
        kaczka.ramka(45, 45, 510)
        kaczka.obrazek(x)
        text("obrazek wyswietlil sie prawidlowo", width - 450, height -10)
        
    

    
        
        
        
    
