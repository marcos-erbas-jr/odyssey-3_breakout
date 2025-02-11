import pygame

pygame.init()
screen = pygame.display.set_mode((535,330))
"""icon = pygame.image.load('breakout.png')
pygame.display.set_icon(icon)"""
clock=pygame.time.Clock()
running = True

x = 25
ys = 30

linhas = []

def background():
    screen.fill((0, 0, 0))
    pygame.draw.lines(screen, (255, 255, 255), True,
                      [(10, 10), (525, 10), (10, 10), (10, 320), (525, 320),
                       (525, 10)], 5)
xs = x
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    background()

    if len(linhas) == 0:
        for b in range(0,10):
            for c in range(0,14):
                linhas.append((xs, ys))
                xs += 35
            xs = x
            ys += 15

    for blocks3 in linhas:
        pygame.draw.rect(screen, (255, 255, 255), (blocks3[0], blocks3[1],30,10))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()