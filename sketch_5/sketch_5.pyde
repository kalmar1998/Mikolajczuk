class Kwadrat():
    
    def __init__(self, n):
        self.name = n
    def rysuj_kwadrat(self):
        rect(100, 100, 100, 100)
    def nazwa_figury(self):
        textSize(50)
        text(self.name, 200, 200)

class Kolo():
    def __init__(self, n1, o):
        self.name1 = n1
        self.obiekt = o # trochę na siłę ten atrybut...
    
    def rysuj_kolo(self):
        circle(100, 100, 100)
        
    
def setup():
    size(500, 500)
    global kwadrat, kolo
    kwadrat = Kwadrat("kwadrat")
    kolo = Kolo("koło", kwadrat)
    
def draw():
    kolo.obiekt.rysuj_kwadrat() # niezłe zagnieżdżenie, kwadratura koła x) więcej zamieszania niż praktyczności
    kolo.rysuj_kolo()
    kolo.obiekt.nazwa_figury()
  
def mousePressed():
    exit()

# 1,75p
