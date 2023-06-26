import pygame as pg ; import math ;
from pygame.locals import RLEACCEL 

width = 1100 ; height = 500 ; running = True 
g = 9.81 ; x = 50 ; y = 500 ; time = 0

v0 = float(input("ingrese una velocidad: ")) ## v en m/s
ang = int(input("ingrese el angulo: ")) ## angulo en grados

#color pelota
red = (255, 0, 0)
screen = pg.display.set_caption('Tiro parabolico')

#cargado de imagenes
def Load_Image(sFile,transp = False):
    try: image = pg.image.load(sFile)
    except pg.error as message:
           raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color, RLEACCEL)
    return image

#iniciacion de pygame
pg.init()
screen = pg.display.set_mode((width, height)) #asignacion a screen
pg.display.set_caption('Simulacion de Tiro parabolico') #titulo de ventana
pg.display.set_mode((width, height)) #tamaño ventana

clock = pg.time.Clock()

#fondo
aImg = []
aImg.append(Load_Image('fondo.jpg',False ))

def Fondo():
    screen.blit(aImg[0],(0,0))
    return

#ecuacioones
def calculate_position(time):
    radian_angle = math.radians(ang)
    x = v0 * math.cos(radian_angle) * time   #x = v0 * cos(angulo) * tiempo
    y = (v0 * math.sin(radian_angle) * time) - (0.5 * g * time ** 2) #y = (v0 * seno (angulo) * tiempo)- (1/2*g*tiempo^2)
    return x, y

#bucle principal
while running:
 cKey = pg.key.get_pressed()
 if cKey[pg.K_ESCAPE] : running = False

 ev = pg.event.get()
 for e in ev:
  if e.type == quit               : running = False
  
 time += 0.1
 position = calculate_position(time) 
 Fondo()
 pg.draw.circle(screen, (red), (int(position[0]), int(height - position[1])),20, 5) #dibujo de palota y su posicion en x e y
 print(position[1]) #mostrar posicion en el eje Y
 pg.display.flip() #mostrar la pantalla
 clock.tick(60) #iteraciones por segundo
pg.quit
