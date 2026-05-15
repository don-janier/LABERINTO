import tkinter as tk

ventana = tk.Tk()
ventana.title("La Berintonela")
ventana.geometry("1000x600")
ventana.configure(bg="#100221")
ventana.resizable(False, False)

def empezar_juego():
    for elemento in ventana.winfo_children():
        elemento.destroy()
    ventana.configure(bg="#100221")

def cerrar_programa():
    ventana.destroy()

etiqueta1 = tk.Label(ventana, text="LA BERINTONELA", font=("Fixedsys", 50, "bold"), fg="#6CEBEB", bg="#100221", height=-2, width=20   )
etiqueta1.pack(pady=20)

boton_play = tk.Button(ventana, text="PLAY", font=("Fixedsys", 20, "bold"), command=empezar_juego, fg="#000000", width=10, height=2)
boton_play.pack(pady=100)

boton_exit = tk.Button(ventana, text="EXIT", font=("Fixedsys", 20, "bold"), command=cerrar_programa, fg="#000000", width=10, height=2)
boton_exit.pack(pady=10)

ventana.mainloop()