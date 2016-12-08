import pygame
from finallib import *

ANCHO = 600
ALTO = 448

BLANCO=[255,255,255]
NEGRO=[0,0,0]
ROJO=[255,0,0]
VERDE=[0,255,0]
AZUL=[0,0,255]

def CargarFondo(archivo,ancho_corte,alto_corte):#carga una imagen y la dicide como una matriz
    imagen = pygame.image.load(archivo).convert_alpha()
    img_ancho ,img_alto = imagen.get_size()
    #print img_alto , '' , img_ancho
    matriz_fondo=[]
    for fila in range(0,int(img_ancho/ancho_corte)):
        linea=[]
        for columna in range(0, int(img_alto/alto_corte)):
            cuadro = (fila*ancho_corte,columna*alto_corte,ancho_corte,alto_corte)
            linea.append(imagen.subsurface(cuadro))
        matriz_fondo.append(linea)
    return matriz_fondo


if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO,ALTO))

    pygame.display.set_caption("Juego")#Nombre de la ventana
    fondo = pygame.image.load("imagenes/ff.png")#Cargar la imagen de fondo
    personaje = CargarFondo("imagenes/pj1.png",48,48)


    mov_x = 1
    pos_x = 0
    pos_y = 0
    j = Jugador(10,320,personaje[3][6])
    inicio = Bloque(10,128,0,320)
    final = Bloque(10,128,590,320)
    ########################  BLOQUES MUNDO ######################################
    b1 = Bloque(255,50,0,368)
    b1.rect.x = 0

    ##############################################################################
    marco = fondo.subsurface(pos_x,pos_y,ANCHO,ALTO)

    todos = pygame.sprite.Group()
    bloques = pygame.sprite.Group()
    mundo = pygame.sprite.Group()

    bloques.add(inicio)
    bloques.add(final)
    mundo.add(b1)
    todos.add(j)

    j.lb = bloques

    reloj = pygame.time.Clock()

    fin = False
    con = 0
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    con = 0
                    j.dire = 6
                    j.var_x = 5


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    con = 0
                    j.dire = 5
                    j.var_x = -5


            if event.type == pygame.KEYUP:
                j.var_x = 0
                con = 1





        pos_x += j.mov_x


        #pos_x += mov_x

        for pj in todos:
            if con == 0 and j.rect.x > 10:
                pj.image = personaje[3 + pj.con][pj.dire]

        #print pos_x

        marco = fondo.subsurface(pos_x,pos_y,ANCHO,ALTO)
        pantalla.blit(marco,[0,0])
        #mundo.draw(pantalla)
        todos.draw(pantalla)
        todos.update(pantalla)
        pygame.display.flip()
        reloj.tick(30)
