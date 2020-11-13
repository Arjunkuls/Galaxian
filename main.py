import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

score_val = 0
font = pygame.font.Font("freesansbold.ttf", 32)
tx = 10
ty = 10
def sscore(x, y):
    score = font.render("Score : " + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))

over_font = pygame.font.Font("freesansbold.ttf", 64)
def game_over():
    global score_val
    score_val = 0
    over = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over, (200, 250))


background=pygame.image.load('space.png')

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

bimg = pygame.image.load('bullet.png')
bx=0
by=500
by_change = 5
b_state = "ready"


playerimg = pygame.image.load('Player.png')
px=370
py=500

px_change = 0

def player(x, y):
    screen.blit(playerimg, (x, y))



enemyimg = []
ex = []
ey = []
ex_change = []
ey_change = []
enemy_num = 6
def ec():
    for x in range(enemy_num):
        enemyimg.append(pygame.image.load('enemy.png'))
        ex.append(random.randint(0, 730))
        ey.append(random.randint(50, 150))

        ex_change.append(1)
        ey_change.append(70)
ec()
def enemy(x, y, z):
    screen.blit(enemyimg[z], (x, y))

def fb(x, y):
    global b_state
    b_state = "fire"
    screen.blit(bimg, (x+16,y+10))

def iscoll(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1-x2, 2)) + (math.pow(y1-y2, 2)))
    if distance <27:
        return True

    else:
        return False

running=True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                px_change = -3
            if event.key == pygame.K_d:
                px_change = 3
            if event.key == pygame.K_SPACE:
                bx = px
                fb(bx, by)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                px_change=0
    px += px_change
  
    if px <= 0:
        px = 0
    elif px >= 736:
        px=736
    for x in range(enemy_num):
        if ey[x] > 430:
            for j in range(enemy_num):
                ey[j]=2000
            game_over()
            break
            
        ex[x] += ex_change[x]
        if ex[x] <= 0:
            ex_change[x] = 1
            ey[x] += ey_change[x]
        elif ex[x] >= 736:
            ex_change[x]=-1
            ey[x] += ey_change[x]
        coll = iscoll(ex[x], bx, ey[x], by)
        if coll:
            by = 500
            b_state = "ready"
            score_val += 1
            ex[x]=random.randint(0, 730)
            ey[x]=random.randint(50, 150)
            enemy_num+=1
            ec()
        enemy(ex[x], ey[x], x)

    if by<=0:
        by = 500
        b_state = "ready"

    if b_state == "fire":
        fb(bx, by)
        by -= by_change






    player(px, py)
    sscore(tx, ty)
    pygame.display.update()