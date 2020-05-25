class Kwadrat(object):
    def __init__(self, bok): 
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
class KolorowyKwadrat(Kwadrat):
    def __init__(self,bok): 
        super(KolorowyKwadrat,self).__init__(bok) # celowo nie wprowadzałam, żeby nie robić większego zamieszania, ale miło, że się dokształciłeś :)
        
    def sketchKolorowy(self, x, y):
        
        super(KolorowyKwadrat,self).sketch(x, y)
        
    def koloruj(self,v1,v2,v3):
        fill(v1, v2, v3)
    
    def koloruj_krawedz(self, v1, v2, v3):
        stroke(v1/3, v2/2, v3)   
        
def setup():
    size(500, 500)
    
    kolorowy_kwadrat = KolorowyKwadrat(100)
    kolorowy_kwadrat.koloruj(0,227,255)
    kolorowy_kwadrat.sketchKolorowy(100, 100)
    
    kolorowy_kwadrat_z_kolorowa_krawedzia = KolorowyKwadrat(100)
    kolorowy_kwadrat_z_kolorowa_krawedzia.koloruj(60,210,35)
    kolorowy_kwadrat_z_kolorowa_krawedzia.koloruj_krawedz(0,227,255)
    kolorowy_kwadrat_z_kolorowa_krawedzia.sketchKolorowy(200, 200)
    
# 2pkt
