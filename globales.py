import pygame

class Globales():
    def __init__(self):

        #PANTALLA
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.DISPLAYSURF = pygame.display.set_mode((self.WIDTH, self.HEIGHT))


        #COLORES
        self.NEGRO = (0,0,0)
        self.BLANCO = (255,255,255)
        self.ROJO = (255,0,0)
        self.AZUL = (0,0,255)
        self.verde = (81,255,64)
        self.gris = (177,177,177)
        self.celeste = (53,197,255)
        self.grisclaro = (217,217,217)
        self.rojo_oscuro = (189,17,17)
        self.verde_oscuro = (20,137,8)
        self.amarillo = (239,231,27)
        self.celeste = (56,212,240)
        self.morado = (202,47,243)
        self.naranjo = (233,132,24)
        self.gris_oscuro = (84,84,84)
        self.negro_azulado = (31,34,44)
        self.suelo = (244, 229, 136)

        #FPS
        self.FPS = 60
        self.RELOJ = pygame.time.Clock()
