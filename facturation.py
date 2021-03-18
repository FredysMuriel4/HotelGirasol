import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox

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
root,resizable(0,0)
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file = "img/revision.png"))
tk.Label(root, text='Administración "Hotel Girasol"', bg="#eccc68", font=title).place(x=0, y=0, width=800, height=70)

tk.Button(root, text="Inicio", font=font_base, bg="#eccc68", command=index).place(x=700, y=90)
tk.Label(root, text="Identificacion ", bg="#dfe4ea", font=font_answers).place(x=20, y=150)

userId = StringVar()
tk.Entry(root, textvariable = userId, bg="#ced6e0", font=font_answers).place(x=150, y=150, width=300)
tk.Button(root, text="Consultar",  font=font_answers, bg="#eccc68").place(x=320, y=190)

name = StringVar()
n = tk.Entry(root, textvariable = name, bg="#ced6e0", font=font_answers)
n.insert(0,"Nombre")
n.configure(state='disabled')
n.place(x=30, y=260, width=200)

last_name = StringVar()
ln = tk.Entry(root, textvariable = last_name, bg="#ced6e0", font=font_answers)
ln.insert(0,"Apellido")
ln.configure(state='disabled')
ln.place(x=270, y=260, width=200)

peoples = StringVar()
cp = tk.Entry(root, textvariable = peoples, bg="#ced6e0", font=font_answers)
cp.insert(0,"Cantidad de personas")
cp.configure(state='disabled')
cp.place(x=30, y=320, width=200)

t_room = StringVar()
tr = tk.Entry(root, textvariable = t_room, bg="#ced6e0", font=font_answers)
tr.insert(0,"Tipo de habitación")
tr.configure(state='disabled')
tr.place(x=270, y=320, width=200)

tk.Label(root, text="Total ", bg="#dfe4ea", font=font_answers).place(x=510, y=280)

total = StringVar()
np = tk.Entry(root, textvariable = total, bg="#ced6e0", font=font_answers)
np.insert(0,"$0")
np.configure(state='disabled')
np.place(x=510, y=320, width=200)

p_day = StringVar()
pd = tk.Entry(root, textvariable = p_day, bg="#ced6e0", font=font_answers)
pd.insert(0,"Precio por día")
pd.configure(state='disabled')
pd.place(x=30, y=380, width=200)

c_days = StringVar()
cd = tk.Entry(root, textvariable = c_days, bg="#ced6e0", font=font_answers)
cd.insert(0,"Cantidad de días")
cd.configure(state='disabled')
cd.place(x=270, y=380, width=200)

tk.Button(root, text="Efectuar Pago", font=font_answers, bg="#eccc68").place(x=150, y=430)

root.mainloop()