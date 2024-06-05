import pygame, globales, math

vGlobales = globales.Globales()

class Arma:
    def __init__(self, _rect, _color, _velocidad) -> None:
        self.rect = _rect
        self.color = _color
        self.balas = []
        self.velocidad = _velocidad

#crea una bala nueva con cada llamada la añade a la lista y actualiza
    def agregar_nueva_bala (self, enemigo):
        bala = self.rect
        angulo = -math.atan((enemigo.rect.centery - bala.centery)/(enemigo.rect.centerx - bala.centerx))
        self.balas.append([bala, 30, angulo])
        print(angulo*180/math.pi , math.sin(angulo), math.cos(angulo))

    def mueve_balas (self):
        for i in range (len(self.balas)):
            self.balas[i][0].centerx = self.balas[i][0].centerx + self.velocidad * math.cos(self.balas[i][2])
            self.balas[i][0].centery = self.balas[i][0].centery + self.velocidad * math.sin(self.balas[i][2])
            self.balas[i][1] = self.balas[i][1] -1
            
    def elimina_bala (self, indice):
        del self.balas[indice]


