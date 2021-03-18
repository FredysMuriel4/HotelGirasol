import tkinter as tk
from tkinter import StringVar

def exit():
	root.destroy()
	import login.py

def bookings():
	root.destroy()
	import bookings.py

def delete():
	root.destroy()
	import delete.py

title = ("Arial", 20)
font_base = ("Arial", 18)
font_answers = ("Arial", 15)

root = tk.Tk()
root.title("Inicio")
root.config(bg="#dfe4ea")
root.geometry("800x500+300+100")
root.resizable(0,0)
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file = "img/revision.png"))
tk.Label(root, text='Administración "Hotel Girasol"', bg="#eccc68", font=title).place(x=0, y=0, width=800, height=70)

tk.Button(root, text="Salir", font=font_base, bg="#eccc68", command=exit).place(x=700, y=90)
tk.Label(root, text='Bienvenido '+" @Username", bg="#dfe4ea", font=font_answers).place(x=20, y=100)
tk.Label(root, text='Opciones: ', bg="#dfe4ea", font=font_answers).place(x=20, y=150)
rImg = tk.PhotoImage(file="img/stock.png")
tk.Button(root, text="Revisar Reservas", font=font_answers, bg="#eccc68", command=bookings).place(x=20, y=200, width=180)
tk.Label(root, image=rImg, bg="#eccc68").place(x=202, y=202, height=35)
dImg = tk.PhotoImage(file="img/remove.png")
tk.Button(root, text="Eliminar Reservas", font=font_answers, bg="#eccc68", command=delete).place(x=20, y=250, width=180)
tk.Label(root, image=dImg, bg="#eccc68").place(x=204, y=252, height=35)
sImg = tk.PhotoImage(file="img/stock.png")
tk.Button(root, text="Registro Extendido", font=font_answers, bg="#eccc68").place(x=20, y=300, width=180)
tk.Label(root, image=sImg, bg="#eccc68").place(x=204, y=302, height=35)
fImg = tk.PhotoImage(file="img/invoice.png")
tk.Button(root, text="Facturación", font=font_answers, bg="#eccc68").place(x=20, y=350, width=180)
tk.Label(root, image=fImg, bg="#eccc68").place(x=204, y=352, height=35)

root.mainloop()