#importamos las librerias necesarias para el programa
import tkinter as tk
import pygame
from PIL import Image, ImageTk
import random

ventanaW = 800
ventanaH = 800
tamañoCelda = 40
separacionX = 100
separacionY = 100

# Variables para que calcule cuántas celdas caben en el rango dado (Dimension de la ventana menos 200px)
# Nota: se declara su resultado como 'int' porque, de lo contrario, el resultado da '15.0', lo que Python reconoce como un 'float'
numColumnas = int((ventanaW - 2 * separacionX) / tamañoCelda)
numFilas = int((ventanaH - 2 * separacionY) / tamañoCelda)

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
      x = 100 + (c * tamañoCelda)
      y = 100 + (f * tamañoCelda)

      paredes = cuadricula[f][c]['paredes']

      # A partir de aquí, se mira en cada celda el subdiccionario de paredes (norte, sur, este y oeste) para dibujarlas mediante
      # evaluaciones booleanas independientes para cada eje.
      if ( paredes['n'] ):
        
        lienzo.create_line(
          (x, y),
          (x + tamañoCelda, y),
          fill = 'white',
          w = 2
        )

      if ( paredes['s'] ):
        
        lienzo.create_line(
          (x, y + tamañoCelda),
          (x + tamañoCelda, y + tamañoCelda),
          fill = 'white',
          w = 2
        )

      if ( paredes['e'] ):

        lienzo.create_line(
          (x + tamañoCelda, y),
          (x + tamañoCelda, y + tamañoCelda),
          fill = 'white',
          w = 2
        )

      if ( paredes['w'] ):
        
        lienzo.create_line(
          (x, y),
          (x, y + tamañoCelda),
          fill = 'white',
          w = 2
        )

#creamos una variable global para almacenar la imagen del personaje,
#esta variable se va a usar en otras partes del programa para mostrar la imagen del personaje en la ventana.
def crear_personaje():
    tamaño_personaje = 50
    superficie_personaje = pygame.Surface((tamaño_personaje, tamaño_personaje), pygame.SRCALPHA)

    # Cuerpo del personaje
    pygame.draw.rect(superficie_personaje, (200, 30, 0), (4, 4, 52, 52), border_radius=10)
    pygame.draw.rect(superficie_personaje, (100, 10, 0), (4, 4, 52, 52), width=2, border_radius=10)
    pygame.draw.rect(superficie_personaje, (255, 60, 30), (6, 6, 48, 15), border_radius=8)

    # Ojos del personaje
    pygame.draw.ellipse(superficie_personaje, (255, 255, 255), (12, 18, 14, 20))
    pygame.draw.ellipse(superficie_personaje, (0, 200, 255), (15, 22, 8, 12))
    pygame.draw.ellipse(superficie_personaje, (0, 0, 0), (17, 26, 4, 6))
    pygame.draw.ellipse(superficie_personaje, (255, 255, 255), (34, 18, 14, 20))
    pygame.draw.ellipse(superficie_personaje, (0, 200, 255), (37, 22, 8, 12))
    pygame.draw.ellipse(superficie_personaje, (0, 0, 0), (39, 26, 4, 6))

    # Detalles del personaje
    pygame.draw.polygon(superficie_personaje, (255, 200, 0), [(30, 35), (22, 48), (38, 48)])
    pygame.draw.line(superficie_personaje, (150, 100, 0), (30, 35), (30, 45), 2)

    # Convertir la superficie de Pygame a una imagen de Tkinter
    datos_brutos = pygame.image.tostring(superficie_personaje, "RGBA")
    imagen_pil = Image.frombytes("RGBA", superficie_personaje.get_size(), datos_brutos)
    return ImageTk.PhotoImage(imagen_pil)

#creamos una funcion para empezar el juego, esta funcion se va a ejecutar cuando el usuario haga click en el boton de play, 
#esta funcion va a eliminar todos los elementos de la ventana y va a cambiar el color de fondo de la ventana.
def empezar_juego():
    for elemento in ventana.winfo_children():
        elemento.destroy()
    
    ventana.configure(bg="#100221")

    #esta variable global se va a usar para mostrar la imagen del personaje en la ventana, esta variable se va a actualizar con la imagen del personaje cada vez que se ejecute la funcion de empezar el juego.
    global imagen_personaje_global
    imagen_personaje_global = crear_personaje()

    #creamos un lienzo para dibujar el juego, le damos un tamaño y un color de fondo, y lo colocamos en la ventana.
    lienzo = tk.Canvas(
       ventana,
       w = ventanaW,
       height = ventanaH,
       bg = "#100221",
       highlightthickness = 0
    )
    lienzo.pack()

    laberinto = generar_caminos()
    entrada = (numFilas // 2, 0) # Fila y columnda para la entrada del laberinto.
    salida = (numFilas // 2, numColumnas - 1) # Fila y columnda para la salida del laberinto.

    # Se abren las paredes exteriores de la celda de entradan y salida:
    laberinto[entrada[0]][entrada[1]]['paredes']['w'] = False
    laberinto[salida[0]][salida[1]]['paredes']['e'] = False

    dibujar_laberinto(lienzo, laberinto)

    jugadorX = separacionX + entrada[1] * tamañoCelda + tamañoCelda // 2
    jugadorY = separacionY + entrada[0] * tamañoCelda + tamañoCelda // 2


    #Dibujar personaje
    lienzo.create_image(jugadorX, jugadorY, image=imagen_personaje_global)

#creamos una funcion para cerrar el programa, esta funcion se va a ejecutar cuando el usuario haga click en el boton de exit,
def cerrar_programa():
    ventana.destroy()

#inicializamos pygame solo para usar sus funciones, porque el juego se va a desarrollar con tkinter, 
#pero se usaran algunas funciones de pygame para el desarrollo del juego.
pygame.init()

#creamos la ventana del juego con tkinter, le damos un titulo, un tamaño, un color de fondo y hacemos que no se pueda redimensionar.
ventana = tk.Tk()
ventana.title("La Berintonela")
ventana.geometry(f"{ventanaW}x{ventanaH}")
ventana.configure(bg="#100221")
ventana.resizable(False, False)

imagen_personaje_global = None

#creamos los elementos de la ventana, como etiquetas y botones, les damos un estilo y los colocamos en la ventana.
etiqueta1 = tk.Label(ventana, text="LA BERINTONELA", font=("Fixedsys", 50, "bold"), fg="#6CEBEB", bg="#100221", height=-2, width=20   )
etiqueta1.pack(pady=20)

boton_play = tk.Button(ventana, text="PLAY", font=("Fixedsys", 20, "bold"), command=empezar_juego, fg="#000000", width=10, height=2)
boton_play.pack(pady=100)

boton_exit = tk.Button(ventana, text="EXIT", font=("Fixedsys", 20, "bold"), command=cerrar_programa, fg="#000000", width=10, height=2)
boton_exit.pack(pady=10)

#iniciamos el bucle principal de la ventana, servira para mantener la ventana abierta.
ventana.mainloop()