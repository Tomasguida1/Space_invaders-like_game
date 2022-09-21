import pygame
import random

#inicializa pygame
pygame.init()

#crea la pantalla
pantalla = pygame.display.set_mode((800,600))

#titulo e icono
pygame.display.set_caption("invasores del espacio")
icono = pygame.image.load("alien.png")
pygame.display.set_icon(icono)

#crear jugador
img_player = pygame.image.load("spaceship.png")
player_x = 368
player_y = 530
player_x_cambio = 0

#crear enemigo
img_enemy = pygame.image.load("enemy.png")
enemy_x = random.randint(0,734)
enemy_y = random.randint(50, 200)
enemy_x_cambio = 0

#funcion del jugador
def player(x, y):
    pantalla.blit(img_player,(x, y))
    
#funcion del enemigo
def enemy(x, y):
    pantalla.blit(img_enemy,(x, y))
    
#mantiene abierto el juego hasta que se cierre
se_ejecuta = True
#iteracion de eventos
while se_ejecuta:
    pantalla.fill((77,0,255))
    
    #cerrar el juego
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
       
        #chequea si se presiona una flecha 
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                player_x_cambio -= 0.3
            if evento.key == pygame.K_RIGHT:
                player_x_cambio = 0.3
        
        #chequea si suelta las flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_LEFT:
                player_x_cambio = 0
    #movimiento del jugador
    player_x += player_x_cambio
    #mantener entre los bordes
    if player_x <= 0:
        player_x = 0
    elif player_x >= 734:
        player_x = 734
    
    enemy(enemy_x,enemy_y)   
    player(player_x,player_y)
    #actualiza
    pygame.display.update()