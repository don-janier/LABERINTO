#importamos las librerias necesarias para el programa
import tkinter as tk
import pygame
from PIL import Image, ImageTk

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
    lienzo = tk.Canvas(ventana, width=1000, height=600, bg="#100221", highlightthickness=0)
    lienzo.pack()

    #Dibujar personaje
    lienzo.create_image(400, 300, image=imagen_personaje_global)

#creamos una funcion para cerrar el programa, esta funcion se va a ejecutar cuando el usuario haga click en el boton de exit,
def cerrar_programa():
    ventana.destroy()

#inicializamos pygame solo para usar sus funciones, porque el juego se va a desarrollar con tkinter, 
#pero se usaran algunas funciones de pygame para el desarrollo del juego.
pygame.init()

#creamos la ventana del juego con tkinter, le damos un titulo, un tamaño, un color de fondo y hacemos que no se pueda redimensionar.
ventana = tk.Tk()
ventana.title("La Berintonela")
ventana.geometry("1000x600")
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