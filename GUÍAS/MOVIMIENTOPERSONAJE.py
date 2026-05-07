import pygame as pg

pg.init()

# Tamaño de la ventana:
width = 1200
height = 800

ventana = pg.display.set_mode((width, height))

pg.display.set_caption('LABERINTO')

icon = pg.image.load('maze.png')
pg.display.set_icon(icon)

activo = True

# Bucle de ventana:
while activo:

  for event in pg.event.get():

    # Para que cuando el usuario presione el botón de X en la ventana, este se salga:
    if ( event.type == pg.QUIT ):

      activo = False
        