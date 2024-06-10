import pygame, globales, math

#Variables
vGlobales = globales.Globales()

class Enemigo():
    def __init__(self):
        #Datos del bicho
        self.rect = pygame.Rect(0,330,10,10)
        self.posicion = [self.rect.centerx, self.rect.centery]
        self.color = vGlobales.rojo_oscuro
        self.velocidad = 1.5 #Velociad de movimiento del bicho

        self.direccionPasada = 'void'
        self.vector = [0,0] #define el vector de movimiento del enemigo
        self.radar = [0,0] #apunta hacia la direccion que esta mirando 


    def movimiento (self):
        #movimiento inicial
        if self.direccionPasada == 'void':
            self.contador = 0
            self.vector = self.cambio_dirceccion()

        if (self.contador < 15
            or (vGlobales.DISPLAYSURF.get_at((int(self.rect.centerx +self.radar[0] *15 +self.vector[0]), int(self.rect.centery +self.vector[1] + self.radar[1] *15)))== vGlobales.suelo)):
            self.avanzar()
            self.contador+=self.velocidad
        else:
            self.vector = self.cambio_dirceccion()

    def avanzar (self):
        self.posicion[0] += self.vector[0]
        self.posicion[1] += self.vector[1]
        self.rect.center = self.posicion

    #Busca una direccion diferente para avanzar, distinta a la opuesta de la actual. En ese caso retorna [0,0]
    def cambio_dirceccion (self):
        #MOVIMINETO HACIA LA IZQUIERDDA
        if (self.rect.centerx +15 +self.velocidad <= vGlobales.WIDTH
                and self.direccionPasada != 'derecha'
                and vGlobales.DISPLAYSURF.get_at((int(self.rect.centerx +15 +self.velocidad), int(self.rect.centery)))== vGlobales.suelo):
            
            self.direccionPasada = 'izquierda'
            self.radar = [1,0]
            return [self.velocidad,0]

        #MOVIMIENTO HACIA ABAJO
        elif (self.rect.centery+15+self.velocidad <= vGlobales.HEIGHT
                and self.direccionPasada != 'arriba'
                and vGlobales.DISPLAYSURF.get_at((int(self.rect.centerx), int(self.rect.centery +15 +self.velocidad)))== vGlobales.suelo):
            
            self.direccionPasada = 'abajo'
            self.radar = [0,1]
            return [0,self.velocidad]

        #MOVIMIENTO HACIA LA DERECHA
        elif (self.rect.centerx-15+self.velocidad >=0
                and  self.direccionPasada != 'izquierda'
                and vGlobales.DISPLAYSURF.get_at((int(self.rect.centerx -15 +self.velocidad), int(self.rect.centery)))== vGlobales.suelo):
            
            self.direccionPasada = 'derecha'
            self.radar = [-1,0]
            return [-self.velocidad,0]

        #MOVIMIENTO HACIO ARRIBA
        elif (self.rect.centery-15+self.velocidad >=0
                and self.direccionPasada != 'abajo'
                and vGlobales.DISPLAYSURF.get_at((int(self.rect.centerx), int(self.rect.centery -15 +self.velocidad)))== vGlobales.suelo):
            self.direccionPasada = 'arriba'
            self.radar = [0,-1]
            return[0,-self.velocidad]
        self.radar = [0,0]
        return [0,0]

