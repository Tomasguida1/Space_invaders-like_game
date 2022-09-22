import pygame
import random
import math

#inicializa pygame
pygame.init()

#crea la pantalla
pantalla = pygame.display.set_mode((800,600))

#titulo e icono
pygame.display.set_caption("invasores del espacio")
icono = pygame.image.load("alien.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.jpg")

#crear jugador
img_player = pygame.image.load("spaceship.png")
player_x = 368
player_y = 500
player_x_cambio = 0

#crear enemigo
img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_cambio =  []
enemy_y_cambio = []
quantity = 10

for e in range(quantity):
    img_enemy.append(pygame.image.load("enemy.png"))
    enemy_x.append(random.randint(0,734))
    enemy_y.append(random.randint(50, 200))
    enemy_x_cambio.append(0.5)
    enemy_y_cambio.append(50)

#crear bala
img_bullet = pygame.image.load("missile.png")
bullet_x = 0
bullet_y = 500
bullet_x_cambio = 0
bullet_y_cambio = 1
visible_bullet = False

#score
score = 0
fuente = pygame.font.Font("freesansbold.ttf",32)
text_x =10
text_y= 10

#show score
def show_score(x,y):

    text = fuente.render(f"SCORE: {score}", True, (255,255,255))
    pantalla.blit(text, (x,y))
#funcion del jugador
def player(x, y):
    pantalla.blit(img_player,(x, y))
    
#funcion del enemigo
def enemy(x, y, ene):
    pantalla.blit(img_enemy[ene],(x, y))
    
#funcion disparo
def bullet (x, y):
    global visible_bullet
    visible_bullet = True
    pantalla.blit(img_bullet,(x + 16, y+10))

#colisiones
def colisiones(x_1, y_1, x_2, y_2):
    distance = math.sqrt(math.pow(x_1-x_2, 2) + math.pow(y_2-y_1, 2))
    if distance < 27:
        return True
    else:
        return False
    
#mantiene abierto el juego hasta que se cierre
se_ejecuta = True
#iteracion de eventos
while se_ejecuta:
    #imagen
    pantalla.blit(fondo, (0, 0))
    
    #cerrar el juego
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
       
        #chequea si se presiona una tecla 
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                player_x_cambio -= 0.5
            if evento.key == pygame.K_RIGHT:
                player_x_cambio = 0.5
            if evento.key == pygame.K_SPACE:
                if not visible_bullet:
                    bullet_x = player_x
                    bullet(bullet_x, bullet_y)
        
        #chequea si suelta las flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_LEFT:
                player_x_cambio = 0
    #movimiento del jugador
    player_x += player_x_cambio
    #mantener entre los bordes al jugador
    if player_x <= 0:
        player_x = 0
    elif player_x >= 734:
        player_x = 734
    
    #movimiento del enemigo
    for e in range(quantity):
        enemy_x[e] += enemy_x_cambio[e]
    #mantener entre los bordes al enemigo
        if enemy_x[e] <= 0:
            enemy_x_cambio[e] = 0.5
            enemy_y[e] += enemy_y_cambio[e]
        elif enemy_x[e] >= 734:
            enemy_x_cambio[e] = -0.5
            enemy_y[e] += enemy_y_cambio[e]
            #colision
        colision = colisiones(enemy_x[e], enemy_y[e], bullet_x, bullet_y)
        if colision:
            bullet_y = 500
            visible_bullet = False
            score += 1
            enemy_x[e] = random.randint(0,734)
            enemy_y[e]= random.randint(50, 200)
        enemy(enemy_x[e],enemy_y[e], e)  
    
    #movimiento bala
    if bullet_y <= -64:
        bullet_y = 500
        visible_bullet = False
    if visible_bullet:
        bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_cambio
    

    
     
    player(player_x,player_y)
    show_score(text_x, text_y)
    #actualiza
    pygame.display.update()