import pygame as PG ; import numpy as NP ;
from pygame.locals import RLEACCEL 

Size = (1100,550) ; lOK = True ; PelotaC = 1 
g = 9.81 ; x = 50 ; y = 500 ;

v0 = float(input("ingrese una velocidad: ")) ## v en m/s
alfa = int(input("ingrese el angulo: ")) ## angulo en grados
# ecuaciones
v0x = v0 * NP.cos(NP.deg2rad(alfa))
v0y = v0 * NP.sin(NP.deg2rad(alfa))
t_total = 2 * v0y / g
x_final = v0x * t_total

def Load_Image(sFile,transp = False):
    try: image = PG.image.load(sFile)
    except PG.error as message:
           raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color, RLEACCEL)
    return image

def Init_PyGame():
    PG.init()
    PG.display.set_caption('Tiro parabolico')
    return PG.display.set_mode(Size)

def Init_Fig():
    aImg = []
    aImg.append(Load_Image('pelota.png',True ))
    aImg.append(Load_Image('fondo.jpg',False ))
    return aImg

def Fondo():
    sWin.blit(aFig[1],(0,0))

    return



sWin = Init_PyGame() ; aFig = Init_Fig()

def pelota():
  sWin.blit(aFig[0],(x,y))

while lOK:
 cKey = PG.key.get_pressed()
 if cKey[PG.K_ESCAPE] : lOK = False
 if cKey[PG.K_d] :
    print("Velocidad en x", v0x)
    print("Velocidad en y", v0y)
    print("Tiempo total", t_total)
    print("Distancia de desplazamiento", x_final)
    

 ev = PG.event.get()
 for e in ev:
  if e.type == quit               : lOK = False


 x= x+v0x
 y = y-v0y

 Fondo()
 pelota()
 PG.display.flip()
PG.quit
