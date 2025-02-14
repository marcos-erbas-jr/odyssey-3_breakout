import time

import pygame

pygame.init()
screen = pygame.display.set_mode((535,330))
pygame.display.set_caption('Breakout')
icon = pygame.image.load('breakouticon.png')
pygame.display.set_icon(icon)
clock=pygame.time.Clock()
running = True

#Text Score
myfont = pygame.font.SysFont("monospace", 15, bold=pygame.font.Font.bold)
score = 0

x = 25
xs = x
ys = 35

colors = [(230, 220, 70), (0,200,50), (0,30,250)]
playerx = (535/2) - 20
playery = 270

ballx = (535/2) + 1
bally = 259
velocid = 1.5
incrementox = 2
incrementoy = 5

#blocos
linhas = []

start = playerx

def background():
    screen.fill((0, 0, 0))
    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(10, 10), (525, 10), (10, 10), (10, 320), (525, 320),
                       (525, 10)], 5)
if len(linhas) == 0:
    for b in range(0,3):
        for c in range(0,14):
            bxmax = xs + 30 #ponto do eixo x máximo do bloco
            bymax = ys +10 #ponto do eixo y máximo do bloco
            linhas.append([xs, ys, bxmax, bymax])
            xs += 35
        xs = x
        ys += 15

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    background()
    scoretext1 = myfont.render("Score: {0}".format(score), 0, (255, 255, 255))
    screen.blit(scoretext1, (25, 15))


    for blocks3 in linhas:
        pygame.draw.rect(screen, (255, 255, 255), (blocks3[0], blocks3[1],30,10))

    #player
    pygame.draw.rect(screen, (150,200,50), (playerx, playery, 50,10))

    #ball
    pygame.draw.rect(screen, (255,0,0),(ballx, bally, 10, 10))

    #captura de teclas
    keys = pygame.key.get_pressed()
    if 13 <= playerx <= 473:
        if keys[pygame.K_RIGHT]:
            playerx +=3
            if playerx > 473:
                playerx = 473
        if keys[pygame.K_LEFT]:
            playerx -=3
            if playerx < 13:
                playerx =13

    #Ball move
    if start != playerx:
        bally -= incrementoy / velocid
        ballx += incrementox / velocid
    x_comparat = ballx + 5
    y_comparat = bally

    if bally < 15:
        incrementoy *= -1
    if ballx < 13 or ballx > 513:
        incrementox *= -1

    for blocksComparat in linhas:
        if (blocksComparat[0] < x_comparat+10 and x_comparat < blocksComparat[2] and
                blocksComparat[1] < y_comparat+10
                and y_comparat < blocksComparat[3]):
            linhas.remove(blocksComparat)
            incrementoy *= -1
            incrementox *= -1
            score += 1

    if (playerx < x_comparat + 10 and x_comparat < playerx + 50 and playery <
    y_comparat + 10):
        incrementoy *= -1
        #incrementox *= -1

    if bally > 310 or keys[pygame.K_SPACE] :
        playerx = (535 / 2) - 20
        playery = 270
        ballx = (535 / 2) + 1
        bally = 260
        time.sleep(4)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()