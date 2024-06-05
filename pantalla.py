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
        pygame.draw.rect(self.DISPLAYSURF, self.vMapa.rectangulo5[0], self.vMapa.rectangulo5[1])

    def actualiza_pantalla(self):
        self.DISPLAYSURF.fill(vGlobales.verde)
    
    def actualiza_suelo (self):
        self.DISPLAYSURF.blit(self.vMapa.suelo1Superficie, (0,0))

    def actualiza_malito(self, enemigo):
        pygame.draw.rect(self.DISPLAYSURF, enemigo.color, enemigo.rect)

    def actualiza_base(self, base):
        pygame.draw.rect(self.DISPLAYSURF, base.color, base.rect)

    def actualiza_balas(self, arma, malito):
        tempLista = self.genera_lista_colision([malito])
        for i in range (len(arma.balas)):
            pygame.draw.rect(self.DISPLAYSURF, vGlobales.AZUL, arma.balas[i][0])
            arma.mueve_balas()
            if pygame.Rect.collidelist(arma.balas[i][0], tempLista):
                print('muerte')
                arma.elimina_bala(i)

    def genera_terreno1(self):
        self.vMapa.genera_suelo1()

#Recibe una lista con una lista de atributos que admitan un .rect
#Devuelve una lista con solo atributos rect para la colision con las balas
    def genera_lista_colision (self, lista):
        tempLista = []
        for i in range (len(lista)):
            for j in range (len(lista[i])):
                tempLista = tempLista + [lista[i][j].rect]
        return tempLista
