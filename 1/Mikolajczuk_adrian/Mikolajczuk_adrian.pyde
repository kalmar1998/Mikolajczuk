def setup():
    rectMode(CORNER)
    size(500,500)
    c = color(120,300,24) # wartoby kolor usawić raz na starcie, skoro nie zmieniasz go w trakcie działania programu, a nie ustawiać co klatkę
    fill(c)
def draw():
    if mousePressed:
        circle(mouseX, mouseY, width/10) # tam gdzie się da warto używać zmiennych zależnych

# brakuje else, miało się też coś zadziać, gdy mysz nie będzie kliknięta
#1,5 pkt ale plus do aktywności za zagłębienie się w ustawianie koloru
    
    
