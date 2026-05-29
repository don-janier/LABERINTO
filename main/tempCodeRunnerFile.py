#importamos las librerias necesarias para el programa
import tkinter as tk
import pygame as pg
import time
from PIL import Image, ImageTk
import random

VENTANA_W = 800
VENTANA_H = 800
SEPARACION_X = 100
SEPARACION_Y = 100
TAMAÑO_CELDA = 40
TAMAÑO_PERSONAJE = TAMAÑO_CELDA - 10


# Variables para que calcule cuántas celdas caben en el rango dado (Dimension de la ventana menos 200px)
# Nota: se declara su resultado como 'int' porque, de lo contrario, el resultado da '15.0', lo que Python reconoce como un 'float'
numColumnas = int((VENTANA_W - 2 * SEPARACION_X) / TAMAÑO_CELDA)
numFilas = int((VENTANA_H - 2 * SEPARACION_Y) / TAMAÑO_CELDA)

entrada = (numFilas // 2, 0) # Fila y columnda para la entrada del laberinto.
salida = (numFilas // 2, numColumnas - 1) # Fila y columnda para la salida del laberinto.


# Función que recoge el las dimensiones de la ventana y el tamaño de cada celda
# para saber cuantas celdas caben en el rango dado de la ventana y poder añadir ese numero de celdas 
# a las filas y columnas de una lista
def lista_laberinto():
  
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

# Función que rastrea las celdas vecinas disponibles:
def buscar_vecinos(f, c, cuadricula):

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

# Función que destruye las paredes de la cuadricula para generar los caminos del laberinto caminos:
def crear_caminos(cuadricula):

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
    vecinosDisponibles = buscar_vecinos(f, c, cuadricula)

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

# Función que genera los caminos del laberinto.
def generar_caminos():

  laberinto = lista_laberinto()
  crear_caminos(laberinto)

  return laberinto

# Función encargada de dibujar el laberinto en la ventana:
def dibujar_laberinto(lienzo, cuadricula):

  for f in range(len(cuadricula)):
    
    for c in range(len(cuadricula[f])):

      # Se calcula la posición de cada celda en px.
      x = 100 + (c * TAMAÑO_CELDA)
      y = 100 + (f * TAMAÑO_CELDA)

      paredes = cuadricula[f][c]['paredes']

      # A partir de aquí, se mira en cada celda el subdiccionario de paredes (norte, sur, este y oeste) para dibujarlas mediante
      # evaluaciones booleanas independientes para cada eje.
      if ( paredes['n'] ):
        
        lienzo.create_line(
          (x, y),
          (x + TAMAÑO_CELDA, y),
          fill = 'white',
          w = 2
        )

      if ( paredes['s'] ):
        
        lienzo.create_line(
          (x, y + TAMAÑO_CELDA),
          (x + TAMAÑO_CELDA, y + TAMAÑO_CELDA),
          fill = 'white',
          w = 2
        )

      if ( paredes['e'] ):

        lienzo.create_line(
          (x + TAMAÑO_CELDA, y),
          (x + TAMAÑO_CELDA, y + TAMAÑO_CELDA),
          fill = 'white',
          w = 2
        )

      if ( paredes['w'] ):
        
        lienzo.create_line(
          (x, y),
          (x, y + TAMAÑO_CELDA),
          fill = 'white',
          w = 2
        )

# Función para establecer el tiempo límite de cada ronda del laberinto:
def temporizador(tiempo):

  global tiempoRestante

  if tiempoRestante >= 0:

    # Se calculan los minutos y segundos:
    formato = f'{tiempoRestante:02d}'
    tiempo.config(text = formato)

    # Se resta un segundo:
    tiempoRestante -= 1

    # Se llama a esta función después de 1 segundo (en milisegundos):
    tiempo.after(1000, temporizador, tiempo)

  else:

    ventana.unbind('<KeyPress>') # Swe bloquea el movimiento.

def personaje(lienzo, x1, y1, x2, y2):

  return lienzo.create_oval(
      (x1, y1),
      (x2, y2),
      fill = 'red',
      w = 0
    )

# Función para traducir la fila y la columna en coordenadas de pantalla (px):
def calcular_coords(f, c):

  x1 = SEPARACION_X + c * TAMAÑO_CELDA + (TAMAÑO_CELDA - TAMAÑO_PERSONAJE) // 2
  y1 = SEPARACION_Y + f * TAMAÑO_CELDA + (TAMAÑO_CELDA - TAMAÑO_PERSONAJE) // 2

  x2 = x1 + TAMAÑO_PERSONAJE
  y2 = y1 + TAMAÑO_PERSONAJE

  return x1, y1, x2, y2

#creamos una funcion para empezar el juego, esta funcion se va a ejecutar cuando el usuario haga click en el boton de play, 
#esta funcion va a eliminar todos los elementos de la ventana y va a cambiar el color de fondo de la ventana.
def empezar_juego():

  global tiempoRestante
  tiempoRestante = 10

  puntaje = 0

  for elemento in ventana.winfo_children():
      
      elemento.destroy()
  
  ventana.configure(bg = "#100221")

  # Se crea un frame en la parte superior de la ventana para visualizar el tiempo:
  frameTiempo = tk.Frame(
    ventana,
    bg = "#100221"
  )

  frameTiempo.pack(
    side = 'top',
    fill = 'x'
  )
  tiempo = tk.Label(
    frameTiempo, 
    font = ("Fixedsys", 50), 
    fg = "#6CEBEB", 
    bg = "#100221", 
    height = -2, 
    width = 20
  )

  tiempo.pack()
  
  frameJuego = tk.Frame(
    ventana,
    bg = "#100221"
  )

  frameJuego.pack(
    side = 'bottom',
    fill = 'both',
    expand = True
  )

  #creamos un lienzo para dibujar el juego, le damos un tamaño y un color de fondo, y lo colocamos en la ventana.
  lienzo = tk.Canvas(
    frameJuego,
    w = VENTANA_W,
    height = VENTANA_H,
    bg = "#100221",
    highlightthickness = 0
  )
  lienzo.pack()

  laberinto = generar_caminos()
  
  # Se abren las paredes exteriores de la celda de entradan y salida:
  laberinto[entrada[0]][entrada[1]]['paredes']['w'] = False
  laberinto[salida[0]][salida[1]]['paredes']['e'] = False

  dibujar_laberinto(lienzo, laberinto)

  # Se guarda la posición del jugador en un diccionario:
  posicion = {
    'f': entrada[0],
    'c': entrada[1]
  }

  # Se dibuja al personaje y se guarda su ID:
  x1, y1, x2, y2 = calcular_coords(posicion['f'], posicion['c'])
  jugadorID = personaje(lienzo, x1, y1, x2, y2)

  def mover_jugador(evento):

    tecla = evento.char.lower()
    f = posicion['f']
    c = posicion['c']
    
    # Se evalúa W/A/S/D.
    # Si la tecla es corecta y la pared en esa dirección está con 'False', el personaje se moverá.
    if ( tecla == 'w' and not laberinto[f][c]['paredes']['n'] ):

      posicion['f'] -= 1

    if ( tecla == 's' and not laberinto[f][c]['paredes']['s'] ):

      posicion['f'] += 1

    # NOTA: Se añade una validación para que el jugador no se salga de los límites por la puerta de inicio ni por la salida.
    if ( tecla == 'a' and not laberinto[f][c]['paredes']['w'] and c > 0):

      posicion['c'] -= 1

    if ( tecla == 'd' and not laberinto[f][c]['paredes']['e'] and c < numColumnas - 1):

      posicion['c'] += 1

    # Se calculan las nuevas coordenadas y se le pide al lienzo que mueva el dibujo:
    nx1, ny1, nx2, ny2 = calcular_coords(posicion['f'], posicion['c'])
    lienzo.coords(jugadorID, nx1, ny1, nx2, ny2)


  ventana.bind('<KeyPress>', mover_jugador)

  temporizador(tiempo)
    

#creamos una funcion para cerrar el programa, esta funcion se va a ejecutar cuando el usuario haga click en el boton de exit,
def cerrar_programa():
    ventana.destroy()

#inicializamos pygame solo para usar sus funciones, porque el juego se va a desarrollar con tkinter, 
#pero se usaran algunas funciones de pygame para el desarrollo del juego.
pg.init()

#creamos la ventana del juego con tkinter, le damos un titulo, un tamaño, un color de fondo y hacemos que no se pueda redimensionar.
ventana = tk.Tk()
ventana.title("La Berintonela")
ventana.geometry(f"{VENTANA_W}x{VENTANA_H}")
ventana.configure(bg="#100221")
ventana.resizable(False, False)

imagen_personaje_global = None

#creamos los elementos de la ventana, como etiquetas y botones, les damos un estilo y los colocamos en la ventana.
etiqueta1 = tk.Label(ventana, text="LA BERINTONELA", font=("Fixedsys", 50, "bold"), fg="#6CEBEB", bg="#100221", height=-2, width=20   )
etiqueta1.pack(pady=40)

boton_play = tk.Button(ventana, text="PLAY", font=("Fixedsys", 20, "bold"), command=empezar_juego, fg="#000000", width=10, height=2)
boton_play.pack(pady=100)

boton_exit = tk.Button(ventana, text="EXIT", font=("Fixedsys", 20, "bold"), command=cerrar_programa, fg="#000000", width=10, height=2)
boton_exit.pack(pady=10)

#iniciamos el bucle principal de la ventana, servira para mantener la ventana abierta.
ventana.mainloop()