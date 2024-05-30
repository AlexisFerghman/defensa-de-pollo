import pygame, globales

#Variables
vGlobales = globales.Globales()

class Enemigo():
    def __init__(self):
        #Datos del bicho
        self.rect = pygame.Rect(0,330,10,10)
        self.color = vGlobales.rojo_oscuro
        self.velocidad = 1 #Velociad de movimiento del bicho

        self.direccionPasada = 'void'
        self.vector = [0,0]

    def movimiento (self):
        if self.direccionPasada == 'void':
            self.contador=0
            self.vector = self.cambio_dirceccion()
        
        if (self.contador <15
            or (vGlobales.DISPLAYSURF.get_at((self.rect.centerx +self.vector[0]*15 +self.vector[0], self.rect.centery +self.vector[1] +self.vector[1]*15))== vGlobales.suelo)):
            
            self.avanzar()
            self.contador+=self.velocidad
        else:
            self.vector = self.cambio_dirceccion()

    def avanzar (self):
        self.rect.centerx += self.vector[0]
        self.rect.centery += self.vector[self.velocidad]

    #Busca una direccion diferente para avanzar, distinta a la opuesta de la actual. En ese caso retorna [0,0]
    def cambio_dirceccion (self):
        #MOVIMINETO HACIA LA IZQUIERDDA
        if (self.rect.centerx+15+self.velocidad <= vGlobales.WIDTH and self.direccionPasada != 'derecha' and vGlobales.DISPLAYSURF.get_at((self.rect.centerx+15+self.velocidad,self.rect.centery))== vGlobales.suelo):
            self.direccionPasada = 'izquierda'
            return [self.velocidad,0]

        #MOVIMIENTO HACIA ABAJO
        elif (self.rect.centery+15+self.velocidad <= vGlobales.HEIGHT and self.direccionPasada != 'arriba' and vGlobales.DISPLAYSURF.get_at((self.rect.centerx,self.rect.centery+15+self.velocidad))== vGlobales.suelo):
            self.direccionPasada = 'abajo'
            return [0,self.velocidad]

        #MOVIMIENTO HACIA LA DERECHA
        elif (self.rect.centerx-15+self.velocidad >=0 and  self.direccionPasada != 'izquierda' and vGlobales.DISPLAYSURF.get_at((self.rect.centerx-15+self.velocidad,self.rect.centery))== vGlobales.suelo):
            self.direccionPasada = 'derecha'
            return [-self.velocidad,0]

        #MOVIMIENTO HACIO ARRIBA
        elif (self.rect.centery-15+self.velocidad >=0 and self.direccionPasada != 'abajo' and vGlobales.DISPLAYSURF.get_at((self.rect.centerx,self.rect.centery-15+self.velocidad))== vGlobales.suelo):
            self.direccionPasada = 'arriba'
            return[0,-self.velocidad]
        return [0,0]

