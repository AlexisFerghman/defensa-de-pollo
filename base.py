import pygame, globales

vGlobales = globales.Globales()
class Base:
    def __init__(self) -> None:
        
        #Centro
        self.rect = pygame.Rect(vGlobales.WIDTH/2 -75, vGlobales.HEIGHT/2 -75, 150, 150)
        self.color = vGlobales.AZUL