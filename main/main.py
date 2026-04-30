import pygame

print('Hopa')

pygame.init()

width = 1200
height = 700

ventana = pygame.display.set_mode((width, height))
pygame.display.set_caption("LA BERINTONELA")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()