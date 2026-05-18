import pygame as pg
import random

# Función que recoge el las dimensiones de la ventana y el tamaño de cada celda
# para saber cuantas celdas caben en el rango dado de la ventana y poder añadir ese numero de celdas 
# a las filas y columnas de una lista
def listaLaberinto():
  
  global ventanaH, ventanaW, tamañoCelda, numColumnas, numFilas
  
  cuadricula = []

  # Iteración que crea las filas de la lista 'cuadricula':
  for c in range(numFilas):
    
    fila = []

    # Iteración que crea las filas de la columnas 'cuadricula':
    for d in range(numColumnas):

      celda = {
        'visitada': False,
        'paredes': {'n': True, 's': True, 'e': True, 'w': True}
      }
      fila.append(celda)
  
    cuadricula.append(fila)

  return cuadricula

def dibujarLaberinto(cuadricula):

  global tamañoCelda

  for f in range(len(cuadricula)):
    
    for c in range(len(cuadricula[f])):

      # Se calcula la posición de cada celda en px.
      x = 100 + (c * tamañoCelda)
      y = 100 + (f * tamañoCelda)

      paredes = cuadricula[f][c]['paredes']

      # A partir de aquí, se mira en cada celda el subdiccionario de paredes (norte, sur, este y oeste) para dibujarlas mediante
      # evaluaciones booleanas independientes para cada eje
      if ( paredes['n'] ):
        
        pg.draw.line(
          ventanaJuego,
          (255, 255, 255),
          (x, y),
          (x + tamañoCelda, y),
          2
        )

      if ( paredes['s'] ):
        
        pg.draw.line(
          ventanaJuego,
          (255, 255, 255),
          (x, y + tamañoCelda),
          (x + tamañoCelda, y + tamañoCelda),
          2
        )

      if ( paredes['e'] ):
        
        pg.draw.line(
          ventanaJuego,
          (255, 255, 255),
          (x + tamañoCelda, y),
          (x + tamañoCelda, y + tamañoCelda),
          2
        )

      if ( paredes['w'] ):
        
        pg.draw.line(
          ventanaJuego,
          (255, 255, 255),
          (x, y),
          (x, y + tamañoCelda),
          2
        )

def generarLaberinto(cuadricula):

  global numColumnas, numFilas

  # Se eligen una fila y columnas al azar desde la primera hasta la última:
  filaInicio = random.randint(0, numFilas - 1)
  colInicio = random.randint(0, numColumnas - 1)

  # Se define la celda actual:
  actual = [filaInicio, colInicio]

  # Se marca la celda como visitada en la matriz:
  cuadricula[filaInicio][colInicio]['visitada'] = True

  pila = [actual]

def buscarVecinos(f, c, cuadricula):

  vecinos = []

  if f > 0:
    if not cuadricula[f - 1][c]['visitada']:
       
       vecinos.append(('n', f - 1, c))

    if not cuadricula[f + 1][c]['visitada']:
       
       vecinos.append(('s', f + 1, c))

  if c > 0:
    if not cuadricula[f][c - 1]['visitada']:
       
       vecinos.append(('w', f, c - 1))

    if not cuadricula[f][c + 1]['visitada']:
        
        vecinos.append(('e', f, c + 1))
    

pg.init()

global ventanaH, ventanaW, tamañoCelda, numColumnas, numFilas

ventanaW = 800
ventanaH = 800
tamañoCelda = 40

# Variables para que calcule cuántas celdas caben en el rango dado (Dimension de la ventana menos 200px)
# Nota: se declara su resultado como 'int' porque, de lo contrario, el resultado da '15.0', lo que Python reconoce como un 'float'
numColumnas = int((ventanaW-200)/tamañoCelda)
numFilas = int((ventanaH-200)/tamañoCelda)

print(listaLaberinto())

ventanaJuego = pg.display.set_mode((ventanaW, ventanaH))

labCuadricula = listaLaberinto()

activo = True

# Bucle de ventana:
# Asegurararse de llevar una jerarquía en el bucle. EJ: No se puede cargar primero el jugador que el fondo.
while activo:

  ventanaJuego.fill((0, 0, 0))

  dibujarLaberinto(labCuadricula)

  for event in pg.event.get():
    
    if ( event.type == pg.QUIT ):

      activo = False

  pg.display.update()