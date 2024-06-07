import pygame, globales

vGloblaes = globales.Globales()

class Balas():
    def __init__(self, _rect):
        self.posicion =[_rect.centerx, _rect.centery]
        self.rect = _rect
        print(self.posicion[0], "aqui", self.posicion[1])
    
    def set_angulo (self, _angulo):
        self.angulo = _angulo

    def actualiza_posicion (self):
        self.rect.center = self.posicion
        print(self.posicion[0], "aqui")