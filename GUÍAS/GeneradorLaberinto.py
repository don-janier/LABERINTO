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

# Función encargada de dibujar el laberinto en la ventana:
def dibujarLaberinto(cuadricula):

  global tamañoCelda

  for f in range(len(cuadricula)):
    
    for c in range(len(cuadricula[f])):

      # Se calcula la posición de cada celda en px.
      x = 100 + (c * tamañoCelda)
      y = 100 + (f * tamañoCelda)

      paredes = cuadricula[f][c]['paredes']

      # A partir de aquí, se mira en cada celda el subdiccionario de paredes (norte, sur, este y oeste) para dibujarlas mediante
      # evaluaciones booleanas independientes para cada eje.
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

# Función que destruye las paredes de la cuadricula para generar los caminos del laberinto caminos:
def generarLaberinto(cuadricula):

  global numColumnas, numFilas

  # Se eligen una fila y columnas al azar desde la primera hasta la última:
  filaInicio = random.randint(0, numFilas - 1)
  colInicio = random.randint(0, numColumnas - 1)

  # Se define la celda actual y se inicializa la pila:
  actual = [filaInicio, colInicio]
  pila = [actual]

  # Bucle para conocer si el laberinto está terminado o no y que destruye las paredes de la cuadrícula:
  while pila:

    #  Se marca la celda inicial como visitada en la matriz:
    cuadricula[filaInicio][colInicio]['visitada'] = True

    actual = pila[-1]

    # Se extraen 'f' y 'c' de la celda actual para que existan en el código:
    f = actual[0]
    c = actual[1]

    # 'f' y 'c' se extraen de la celda actual: << f, c = actual[0], actual [1] >>:
    vecinosDisponibles = buscarVecinos(f, c, cuadricula)

    if vecinosDisponibles:

      # Se elige un vecino al azar y se desempaquetan sus tres datos:
      direccion, fVecino, cVecino = random.choice(vecinosDisponibles)

      # Se rompen las paredes ( asignando False a la actual y a la opuesta del vecino )
      if direccion == 'n':

        cuadricula[f][c]['paredes']['n'] = False
        cuadricula[fVecino][cVecino]['paredes']['s'] = False

      elif direccion == 's':

        cuadricula[f][c]['paredes']['s'] = False
        cuadricula[fVecino][cVecino]['paredes']['n'] = False

      elif direccion == 'w':

        cuadricula[f][c]['paredes']['w'] = False
        cuadricula[fVecino][cVecino]['paredes']['e'] = False

      elif direccion == 'e':

        cuadricula[f][c]['paredes']['e'] = False
        cuadricula[fVecino][cVecino]['paredes']['w'] = False

      # Se marca la celda como visitada:
      cuadricula[fVecino][cVecino]['visitada'] = True

      # Se guarda la nueva celda en la pila:
      actual = [fVecino, cVecino]
      pila.append(actual)

    else:

      pila.pop()

# Función que rastrea las celdas vecinas disponibles:
def buscarVecinos(f, c, cuadricula):

  global numFilas, numColumnas

  vecinos = []

  if ( f > 0 and not cuadricula[f - 1][c]['visitada'] ):
       
    vecinos.append(('n', f - 1, c))

  if ( f < numFilas - 1 and not cuadricula[f + 1][c]['visitada'] ):
       
       vecinos.append(('s', f + 1, c))

  if ( c > 0 and not cuadricula[f][c - 1]['visitada'] ):
       
       vecinos.append(('w', f, c - 1))

  if ( c < numColumnas - 1 and not cuadricula[f][c + 1]['visitada'] ):
        
    vecinos.append(('e', f, c + 1))

  return vecinos
    

pg.init()

global ventanaH, ventanaW, tamañoCelda, numColumnas, numFilas

ventanaW = 800
ventanaH = 800
tamañoCelda = 40

# Variables para que calcule cuántas celdas caben en el rango dado (Dimension de la ventana menos 200px)
# Nota: se declara su resultado como 'int' porque, de lo contrario, el resultado da '15.0', lo que Python reconoce como un 'float'
numColumnas = int((ventanaW-200)/tamañoCelda)
numFilas = int((ventanaH-200)/tamañoCelda)

ventanaJuego = pg.display.set_mode((ventanaW, ventanaH))

laberinto = listaLaberinto()

generarLaberinto(laberinto)

activo = True

reloj = pg.time.Clock()

# Bucle de ventana:
# Asegurararse de llevar una jerarquía en el bucle. EJ: No se puede cargar primero el jugador que el fondo.
while activo:

  ventanaJuego.fill((0, 0, 0))

  dibujarLaberinto(laberinto)

  for event in pg.event.get():
    
    if ( event.type == pg.QUIT ):

      activo = False
      pg.quit()

  pg.display.update()
  reloj.tick(60)

# ¡POR FIN! AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA