import pygame
import random
import math
from pygame import mixer
pygame.init()

screen = pygame.display.set_mode((1280, 720))

# title and icon
pygame.display.set_caption("Corona Invaders")
icon = pygame.image.load('v.png')

pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('coronavirus.png')
playerX = 640
X_change = 0
playerY = 600
Y_change = 0

# Indian
indianImg = []
indX = []
indY = []
indX_change = []
indY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    indianImg.append(pygame.image.load('india.png'))
    indX.append(random.randint(0, 1216))
    indY.append(random.randint(0, 500))
    indX_change.append(0.8)
    indY_change.append(20)

bullet = pygame.image.load('v.png')
bulX = 0
bulY = 600
bulX_change = 0
bulY_change = 2
bul_state = "ready"
#bg
Img = pygame.image.load('mapb.png').convert()
mixer.music.load('background.wav')
mixer.music.play(-1)
#score
score_val = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX =10
textY =10
def show_score(x,y):
    score = font.render("Deaths :" + str(score_val),True,(0,0,0))
    screen.blit(score,(x,y))

# over

o_font = pygame.font.Font('freesansbold.ttf', 80)


def gameover():
        over = font.render("GAME OVER", True, (0, 0, 0))
        screen.blit(over, (640, 360))











def player(x, y):
    screen.blit(playerImg, (x, y))


def indian(x, y, i):
    screen.blit(indianImg[i], (x, y))


def fbullet(x, y):
    global bul_state
    bul_state = "fire"
    screen.blit(bullet, (x + 16, y + 10))


def isCollision(indX, indY, bulX, bulY):
    distance = math.sqrt((math.pow(indX - bulX, 2)) + (math.pow(indY - bulY, 2)))
    if distance < 27:
        return True
    else:
        return False


# GAme Loop
running = True
while running:

    screen.fill((255, 255, 255))
    # bg img
    screen.blit(Img, (0, 0))

    # pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                X_change = -0.7
            if event.key == pygame.K_RIGHT:
                X_change = 0.7
            if event.key == pygame.K_SPACE:
                if bul_state is "ready":
                    bullet_sound =mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulX = playerX
                    fbullet(bulX, bulY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                X_change = 0
            if event.key == pygame.K_RIGHT:
                X_change = 0
        if event.type == pygame.K_SPACE:
            fbullet(playerX, playerY)

    playerX += X_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1216:
        playerX = 1216
    for i in range(num_of_enemies):
        #gameover
        if indY[i] > 542:
            for j in range(num_of_enemies):
                indY[j] = 2000
            gameover()
            break

        indX[i] += indX_change[i]
        if indX[i] <= 0:
            indX[i] = 0
            indX_change[i] = 0.5
            indY[i] += indY_change[i]
        elif indX[i] >= 1216:
            indX[i] = 1216
            indX_change[i] = -0.5
            indY[i] += indY_change[i]
            # collision
        collision = isCollision(indX[i], indY[i], bulX, bulY)
        if collision:
            exp_sound =mixer.Sound('explosion.wav')
            exp_sound.play()
            bulY = 600
            bul_state = "ready"
            score_val += 1
            #print(score)
            indX[i] = random.randint(0, 1216)
            indY[i] = random.randint(0, 500)

        indian(indX[i], indY[i] ,i)

        # bullet movement
    if bulY <= 0:
        bulY = 600
        bul_state = "ready"
    if bul_state is "fire":
        fbullet(bulX, bulY)
        bulY -= bulY_change




    player(playerX, playerY)
    show_score(textX,textY)

    pygame.display.update()
