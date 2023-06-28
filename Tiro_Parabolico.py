import pygame as pg ; import math 

width = 1100    # ancho de pantalla
height = 500    # alto de pantalla   
g = 9.81   # fuerza de gravedad
x = 0    # posicion inicial en x
y = 500   # posicion inicial en y
time = 0   #tiempo
verde = (0, 255, 0)   # color de la pelota
negro = (0,0,0)  # color del fondo
altura = []   #lista para almacenar alturas

#ingreso de datos
v0 = float(input("ingrese una velocidad: ")) ## v en m/s
ang = int(input("ingrese el angulo: ")) ## angulo en grados

#iniciacion de pygame
pg.init()
screen = pg.display.set_mode((width, height)) #asignacion a screen
pg.display.set_caption('Simulacion de Tiro parabolico') #titulo de ventana
clock = pg.time.Clock()

#ecuacioones
def calculate_position(time):
    radian_angle = math.radians(ang)   # angulo en radians
    x = v0 * math.cos(radian_angle) * time   #x = v0 * cos(angulo) * tiempo
    y = (v0 * math.sin(radian_angle) * time) - (0.5 * g * time ** 2) #y = (v0 * seno (angulo) * tiempo)- (1/2*g*tiempo^2)
    return x, y   # regresa x e y

#mas ecuaciones
t = (2*v0*math.sin(math.radians(ang)))/g  #Tiempo de vuelo total
yMax = (v0**2*(math.sin(math.radians(ang))**2))/(2*g) # Altura maxima 
running = True 


#bucle principal
while running:
 cKey = pg.key.get_pressed()
 if cKey[pg.K_ESCAPE] : running = False   # cerrar ventana con tecla escape

#eventos de pygame
 ev = pg.event.get()
 for e in ev:
  if e.type == quit   : running = False  # evento de cerrar ventana

 time += 0.01 #entre mas decimales seran mas precisos los datos
 position = calculate_position(time) 
 screen.fill(negro)   # se pinta la ventana
 pg.draw.circle(screen, (verde), (int(position[0]), int(height - position[1])),5, 5) #dibujo de palota y su posicion en x e y

#condiciones
 if position[1] > 0: 
   print("position en el eje Y = " + str((position[1]))) #mostrar posicion en el eje Y

 if position[1] < 0 and position [1] > -0.7:   # si la pelota llega a 0 
    print("alcance horizontal = " + str(position[0]))   # Alcance horizontal
    print("tiempo total de vuelo = " + str(t))     #  escribir tiempo total de vuelo
    print("altura maxima = " + str(yMax)) #   escribir altura maxima

 if position[1] < 0:  # si la pelota toca el suelo
   running = False  # se cierra el programa

 
 pg.display.flip() #mostrar la pantalla
 clock.tick(60) #iteraciones por segundo
pg.quit #cerrar pygame
