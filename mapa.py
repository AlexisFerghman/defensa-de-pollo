import pygame, globales

#Variables
vGlobales = globales.Globales()

class Mapa:
    def __init__(self) -> None:
        #terreno 1
        self.rectangulo1 = [vGlobales.suelo, pygame.Rect(0, 320, 50, 30)]
        self.rectangulo2 = [vGlobales.suelo, pygame.Rect(50, 50, 30, 300)]
        self.rectangulo3 = [vGlobales.suelo, pygame.Rect(80, 50, 600,30)]
        self.rectangulo4 = [vGlobales.suelo, pygame.Rect(680, 50, 30, 100)]
        self.rectangulo5 = [vGlobales.suelo, pygame.Rect(680, 150, 175, 30)]
        
        #medio

    def copia_pixel(self, pantalla, matriz, color): #Retorna un color para el pixel_array
        i = 0
        while (i < vGlobales.WIDTH):
            j = 0
            while (j < vGlobales.HEIGHT):
                if (pantalla.get_at((i,j)) ==  color):
                    matriz[i][j] = (color)
                else:
                    matriz[i][j] = (0,0,0,0)
                j+=1
            i+=1
        return matriz
    
    #MAPA 1
    def genera_suelo1(self):

        superficieTemporal = pygame.Surface((vGlobales.WIDTH, vGlobales.HEIGHT), pygame.SRCALPHA)
        pixelArray = pygame.PixelArray(superficieTemporal)
        pixelArray = self.copia_pixel(vGlobales.DISPLAYSURF, pixelArray, vGlobales.suelo)
        self.suelo1Superficie = pixelArray.make_surface()
