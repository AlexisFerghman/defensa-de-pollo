import pygame, globales

vGloblaes = globales.Globales()

class Balas():
    def __init__(self, _rect, _tamaño):
        self.posicion = [_rect.left, _rect.top]
        self.rect = pygame.Rect(_rect.topleft, (_tamaño, _tamaño))

    def set_angulo (self, _angulo):
        self.angulo = _angulo

    def actualiza_posicion (self):
        self.rect.center = self.posicion
