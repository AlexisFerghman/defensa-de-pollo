import pygame, globales, math, balas

vGlobales = globales.Globales()

class Arma:
    def __init__(self, _rect, _color, _velocidad) -> None:
        self.rect = _rect
        self.color = _color
        self.balas = []
        self.velocidad = _velocidad

#crea una bala nueva con cada llamada la añade a la lista y actualiza
    def agregar_nueva_bala (self, enemigo):
        bala = balas.Balas(self.rect)
        angulo = math.atan2((enemigo.rect.centery - bala.rect.centery),(enemigo.rect.centerx - bala.rect.centerx))
        bala.set_angulo(angulo)
        self.balas.append(bala)
        print(self.balas[0].posicion[0])

    def mueve_balas (self):
        for i in range (len(self.balas)):
            print(i+1)
            print(self.balas[i].posicion[0]+1)
            self.balas[i].posicion[0] = self.balas[i].posicion[0] + self.velocidad * math.cos(self.balas[i].angulo)
            self.balas[i].posicion[1] = self.balas[i].posicion[1] + self.velocidad * math.sin(self.balas[i].angulo)
            self.balas[i].actualiza_posicion()
            #self.balas[i][1] = self.balas[i][1] -1 posible borrado
            
    def elimina_bala (self, indice):
        del self.balas[indice]


