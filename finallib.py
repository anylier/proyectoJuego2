import pygame

ANCHO = 600
ALTO = 500

BLANCO=[255,255,255]
NEGRO=[0,0,0]
ROJO=[255,0,0]
VERDE=[0,255,0]
AZUL=[0,0,255]

class Jugador(pygame.sprite.Sprite):
    id=0
    def __init__(self,px,py,archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = archivo
        self.rect=self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
        self.click = False
        self.ind=0
        #self.con=0
        self.dire=1
        self.var_x=0
        self.var_y=0
        self.vida= 300
        self.dano= 1500
        self.sonido=pygame.mixer.Sound("sonidos/famaleReady.fac")
        self.sonido.play()

    def update(self,surface):

        self.rect.x += self.var_x
        self.rect.y += self.var_y
        
