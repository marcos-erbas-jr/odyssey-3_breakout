import pygame

pygame.init()
screen = pygame.display.set_mode((535,330))
"""icon = pygame.image.load('breakout.png')
pygame.display.set_icon(icon)"""
clock=pygame.time.Clock()
running = True

x = 25
xs = x
ys = 30

playerx = 30
playery = 200

linhas = []

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


    for blocks3 in linhas:
        pygame.draw.rect(screen, (255, 255, 255), (blocks3[0], blocks3[1],30,10))

    pygame.draw.rect(screen, (150,200,50), (playerx, playery, 10,10)) #player
    # de teste

    #captura de teclas
    keys = pygame.key.get_pressed()
    if 13 <= playery <= 308:
        if keys[pygame.K_UP]:
            playery -=3
            if playery < 13:
                playery = 13
        if keys[pygame.K_DOWN]:
            playery +=3
            if playery > 308:
                playery = 308

    if 13 <= playerx <= 513:
        if keys[pygame.K_RIGHT]:
            playerx +=3
            if playerx > 513:
                playerx = 513
        if keys[pygame.K_LEFT]:
            playerx -=3
            if playerx < 13:
                playerx =13
    print(playerx, playery)

    x_comparat = playerx + 5
    y_comparat = playery
    for blocksComparat in linhas:

        if (blocksComparat[0] < x_comparat+10 and x_comparat < blocksComparat[2] and
                blocksComparat[1] < y_comparat+10
                and y_comparat < blocksComparat[3]):
            pygame.draw.rect(screen, (255, 0, 0),
                             (blocksComparat[0], blocksComparat[1], 30, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()