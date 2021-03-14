import tkinter as tk
from tkinter import StringVar

def index():
	root.destroy()
	import index.py

title = ("Arial", 20)
font_base = ("Arial", 18)
font_answers = ("Arial", 15)

root = tk.Tk()
root.title("Reservas")
root.config(bg="#dfe4ea")
root.geometry("800x500+300+100")
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file = "img/revision.png"))
tk.Label(root, text='Administración "Hotel Girasol"', bg="#eccc68", font=title).place(x=0, y=0, width=800, height=70)


root.mainloop()