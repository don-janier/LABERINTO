import tkinter as tk

ventana = tk.Tk()
ventana.title("La Berintonela")
ventana.geometry("1000x600")
ventana.configure(bg="Purple4")
etiqueta = tk.Label(ventana, text="LA BERINTONELA", font=("Fixedsys", 30, "bold"), fg="white", bg="black", height=-2, width=20   )
etiqueta.pack(pady=20)
ventana.mainloop()