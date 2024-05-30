import pygame, sys, pantalla, globales, enemigo, base

#DATOS
vGlobales = globales.Globales()
vPantalla = pantalla.Pantalla()

#Inicializacion de el terreno
vPantalla.dibuja_mapa1()
vPantalla.vMapa.genera_suelo1()
pygame.init()

malo1= enemigo.Enemigo()

base1 = base.Base()


while True:
    #EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    vPantalla.actualiza_pantalla()
    vPantalla.actualiza_suelo()
    vPantalla.actualiza_malito(malo1)
    vPantalla.actualiza_base(base1)

    #movimiento malitos
    malo1.movimiento()

    pygame.display.flip()
    vGlobales.RELOJ.tick(vGlobales.FPS)
