import pygame
import json

ANCHO=200
ALTO= 200

def Sparar(l,ancho):
    con=0
    matriz=[]
    linea=[]
    for i in l:
        linea.append(i)
        con += 1
        if con == ancho:
            matriz.append(linea)
            linea=[]
            con = 0
    return matriz

def Cargar_fondo(archivo,ancho_c,alto_c):
    imagen = pygame.image.load(archivo).convert_alpha()
    img_ancho ,img_alto = imagen.get_size()
    linea_fondo=[]
    for f_y in range(0,img_alto/alto_c):
        for f_x in range(0, img_alto/alto_c):
            cuadro = (f_x*ancho_c,f_y*alto_c,ancho_c,alto_c)
            linea_fondo.append(imagen.subsurface(cuadro))
    return linea_fondo


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    with open ('mapa.json') as js_ar:
        base= json.load(js_ar)

    al=base['height']
    an=base['width']
    print 'dimensiones: ' ,al, 'x', an

    for v in base['tilesets']:
        archivo=v['image']
        c_al=v['tileheight']
        c_an=v['tilewidth']
'''
    lt = Cargar_fondo(archivo,c_an,c_al)
    var_x=0
    for ef in lt:
        pantalla.blit(ef,[var_x,0])
        var_x+=c_an
    pygame.display.flip()'''

    #colicion lista de listatodos
    var_y=0
    for f in colision:
        var_x=0
        for c in f:
            indice =c-1
            if indice > 0:
                cuadro=lt[indice]
                if var_x <= ANCHO:
                    pantalla.blit(cuadro,[var_x,var_y])
            var_y += c_al
        var_x += c_an


    # lsm=[]
    #
    # for v in base['layers']:
    #     if v['name']== 'muros':
    #         lsm = v['data']
    #
    # m= Separar(lsm,an)

    fin = False




    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

    main()
