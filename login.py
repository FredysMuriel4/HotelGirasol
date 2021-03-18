import tkinter as tk
from tkinter import StringVar

def index():
	root.destroy()
	import index.py

title = ("Arial", 20)
font_base = ("Arial", 18)
font_answers = ("Arial", 15)

root = tk.Tk()
root.title("Login")
root.config(bg="#dfe4ea")
root.geometry("800x500+300+100")
root,resizable(0,0)
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file = "img/revision.png"))
tk.Label(root, text='Administración "Hotel Girasol"', bg="#eccc68", font=title).place(x=0, y=0, width=800, height=70)

userImg = tk.PhotoImage(file="img/usuario.png")
tk.Label(root, image=userImg, bg="#dfe4ea").place(x=100, y=140)
user = StringVar()
tk.Label(root, text="Usuario:", font=font_base, bg="#dfe4ea").place(x=410, y=150)
tk.Entry(root, textvariable = user, bg="#ced6e0", font=font_answers).place(x=410, y=190, width=250, height=35)
password = StringVar()
tk.Label(root, text="Contraseña:", font=font_base, bg="#dfe4ea").place(x=410, y=250)
tk.Entry(root, textvariable = password, bg="#ced6e0", show="•", font=font_answers).place(x=410, y=290, width=250, height=35)
tk.Button(root, text="Ingresar", font=font_base, bg="#eccc68", command=index).place(x=470, y=350)
root.mainloop()