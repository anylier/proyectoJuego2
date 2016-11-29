import pygame
from finallib import *

ANCHO = 600
ALTO = 500

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
    fondo = pygame.image.load("imagenes/f.jpg")#Cargar la imagen de fondo
    j = CargarFondo("imagenes/pj1.png",48,48)


    mov_x = 1
    pos_x = 0
    pos_y = 0

    marco = fondo.subsurface(pos_x,pos_y,ANCHO,ALTO)

    todos = pygame.sprite.Group()


    reloj = pygame.time.Clock()
    cont = 0
    fin = False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pj = Jugador(0,400,j[3][6])
                    pj.var_x += 5
                    todos.add(pj)







        #pos_x += mov_x

        #print pos_x

        marco = fondo.subsurface(pos_x,pos_y,ANCHO,ALTO)
        pantalla.blit(marco,[0,0])
        todos.draw(pantalla)
        todos.update(pantalla)
        pygame.display.flip()
        reloj.tick(160)
