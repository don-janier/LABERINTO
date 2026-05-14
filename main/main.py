import pygame 
import constantes
from pygame import font

print('Hozorra')

pygame.init()

ventana = pygame.display.set_mode((constantes.width, constantes.height))
pygame.display.set_caption("LA BERINTONELA")

#fuentes
font_inicio = pygame.font.Font("inicio.ttf", 50)
font_titulo = pygame.font.Font("titulo.ttf", 100)

#botones
boton_jugar = pygame.Rect(constantes.width//2 - 100, constantes.height//2 - 50, 200, 100)

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