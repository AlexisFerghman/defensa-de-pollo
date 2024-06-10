import pygame, sys, pantalla, globales, enemigo, base, arma, random, balas

#DATOS
vGlobales = globales.Globales()
vPantalla = pantalla.Pantalla()

#Inicializacion de el terreno
vPantalla.dibuja_mapa1()
vPantalla.vMapa.genera_suelo1()
pygame.init()

malo1= enemigo.Enemigo()

base1 = base.Base()
a = arma.Arma(pygame.Rect(30,380,5,5), vGlobales.naranjo ,2)
a.agregar_nueva_bala(malo1)
armas = [a]

m= pygame.Rect(1,1,1,1)

while True:
    #EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                temp_arma = arma.Arma(pygame.Rect((event.pos), (10,10)), vGlobales.naranjo ,random.randint(3,8))
                temp_arma.dispara_bala(malo1)
                armas.append(temp_arma)
    
    vPantalla.actualiza_pantalla()
    vPantalla.actualiza_suelo()
    vPantalla.actualiza_malito(malo1)
    vPantalla.actualiza_base(base1)
    vPantalla.actualiza_arma(armas)

    #movimiento malitos
    malo1.movimiento()

    #movimientos balas
    vPantalla.actualiza_balas(armas, [malo1])

    pygame.display.flip()
    vGlobales.RELOJ.tick(vGlobales.FPS)


