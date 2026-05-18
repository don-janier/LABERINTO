import pygame as pg
# Asegurarse de cambiar \ por / a la hora de escribir URL.

pg.init()

# Tamaño de la ventana:
width = 1200
height = 800

ventana = pg.display.set_mode((width, height))

# Para insertar un título a la ventana del juego:
pg.display.set_caption('LABERINTO')

# Para insertar una imágen como ícono:
icon = pg.image.load('GUÍAS/maze.png')
pg.display.set_icon(icon)

# Jugador:
jugadorImg = pg.image.load('0x72_DungeonTilesetII_v1.7/0x72_DungeonTilesetII_v1.7/frames/angel_idle_anim_f0.png')

jugadorW = jugadorImg.get_width()
jugadorH = jugadorImg.get_height()

jugadorX = width*0.5
jugadorY = height*0.5

jugadorX_C = 0
jugadorY_C = 0

def jugador(x, y):

  ventana.blit(jugadorImg, (x, y)) # El método .blit permite dibujar lo que se haya cargado en el programa.

activo = True

# Bucle de ventana:
# Asegurararse de llevar una jerarquía en el bucle. EJ: No se puede cargar primero el jugador que el fondo.
while activo:

  ventana.fill((155,155,155))

  for event in pg.event.get():

    # Para que cuando el usuario presione el botón de X en la ventana, este se salga:
    if ( event.type == pg.QUIT ):

      activo = False

  keys = pg.key.get_pressed()

  jugadorX_C = 0
  jugadorY_C = 0

  if keys[pg.K_a]:

    jugadorX_C = -0.2

  elif keys[pg.K_d]:

    jugadorX_C = 0.2

  if keys[pg.K_w]:

    jugadorY_C = -0.2

  elif keys[pg.K_s]:

    jugadorY_C = 0.2

  # Calcular nueva posición
  nuevaX = jugadorX + jugadorX_C
  nuevaY = jugadorY + jugadorY_C

  # Verificar límites
  if nuevaX >= 0 and nuevaX <= width - jugadorW:
    jugadorX = nuevaX
  if nuevaY >= 0 and nuevaY <= height - jugadorH:
    jugadorY = nuevaY

  jugador(jugadorX, jugadorY)
  pg.display.update() # Mantiene las variables del juego actualizadas.

