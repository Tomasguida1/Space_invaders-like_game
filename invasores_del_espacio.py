import pygame

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

#funcion del jugador
def player(x, y):
    pantalla.blit(img_player,(x, y))
    
#mantiene abierto el juego hasta que se cierre
se_ejecuta = True

while se_ejecuta:
    pantalla.fill((77,0,255))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                player_x_cambio -= 0.3
            if evento.key == pygame.K_RIGHT:
                player_x_cambio = 0.3
        
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_LEFT:
                player_x_cambio = 0
    
    player_x += player_x_cambio
    player(player_x,player_y)
    pygame.display.update()