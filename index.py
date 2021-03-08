import tkinter as tk
from tkinter import StringVar

title = ("Arial", 20)
font_base = ("Arial", 18)
font_answers = ("Arial", 15)

root = tk.Tk()
root.title("Inicio")
root.config(bg="#dfe4ea")
root.geometry("800x500+300+100")
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file = "img/revision.png"))

tk.Button(root, text="Salir", font=font_base, bg="#eccc68").place(x=700, y=90)
tk.Label(root, text='Administración "Hotel Girasol"', bg="#eccc68", font=title).place(x=0, y=0, width=800, height=70)
tk.Label(root, text='Bienvenido '+" @Username", bg="#dfe4ea", font=font_answers).place(x=20, y=100)
tk.Label(root, text='Opciones: ', bg="#dfe4ea", font=font_answers).place(x=20, y=100)

root.mainloop()