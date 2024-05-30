import pygame, sys, globales, mapa, enemigo, base

#Variables
vGlobales = globales.Globales()

#Clase
class Pantalla():
    def __init__(self):

        self.vMapa = mapa.Mapa()

        #PANTALLA
        self.DISPLAYSURF = pygame.display.set_mode((vGlobales.WIDTH, globales.Globales().HEIGHT))
        self.DISPLAYSURF.fill(globales.Globales().verde)
    
    #Dibujo mapa 1        
    def dibuja_mapa1 (self):
        pygame.draw.rect(self.DISPLAYSURF, self.vMapa.rectangulo1[0], self.vMapa.rectangulo1[1])
        pygame.draw.rect(self.DISPLAYSURF, self.vMapa.rectangulo2[0], self.vMapa.rectangulo2[1])
        pygame.draw.rect(self.DISPLAYSURF, self.vMapa.rectangulo3[0], self.vMapa.rectangulo3[1])
        pygame.draw.rect(self.DISPLAYSURF, self.vMapa.rectangulo4[0], self.vMapa.rectangulo4[1])

    def actualiza_pantalla(self):
        self.DISPLAYSURF.fill(vGlobales.verde)
    
    def actualiza_suelo (self):
        self.DISPLAYSURF.blit(self.vMapa.suelo1Superficie, (0,0))

    def actualiza_malito(self, enemigo):
        pygame.draw.rect(self.DISPLAYSURF, enemigo.color, enemigo.rect)

    def actualiza_base(self, base):
        pygame.draw.rect(self.DISPLAYSURF, base.color, base.rect)

    def genera_terreno1(self):
        self.vMapa.genera_suelo1()
