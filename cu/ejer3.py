import math
class Punto(object):
    x=0
    y=0
    x2=''
    y2=''
    def __init__(self,x,y,x2,y2):
        self.x=x
        self.y=y
        self.x2=x2
        self.y2=y2
    def distancia(self):
        return math.sqrt(self.x2**2+self.y2**2)
    def muestra_punto(self):
        print(self.x2,self.y2)
    def verdistancia(self):
        if dist1<dist2:
            print(punto1)
        else:
            print(punto2)
punto1=Punto(0,0,3,2)
punto2=Punto(0,0,4,5)
punto1.distancia()
dist1=punto1.distancia()
print('distancia punto1',punto1.distancia())
punto2.distancia()
print('distancia punto2',punto2.distancia())
dist2=punto2.distancia()
punto1.muestra_punto()
punto2.muestra_punto()
punto1.verdistancia()
punto2.verdistancia()

