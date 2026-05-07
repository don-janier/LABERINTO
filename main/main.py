import pygame 

print('Hozorra')

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

# Cuando vaya a guardar cambios, tiene que ponerles título.
# Si quiere que yo revise los cambios, presiona la opción que diga 'Commit & Push'
# Si quiere que los cambios se guarden y se sincronicen de una, presiona 'Commit & Sync'
# Tengo que crear el ambiente virtual D:
# Recuerde crear un entorno virtual cuando clone la carpeta del repositorio.
# Y después instala Pygame.