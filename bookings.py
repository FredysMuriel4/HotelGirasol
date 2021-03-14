import tkinter as tk
from tkinter import StringVar

def index():
	root.destroy()
	import index.py

def show():
	if userId.get() == "1001947524":
		condition.set("Activo")
		name.set("Fredys")
		last_name.set("Muriel")
		age.set("19 años")
		tel.set("3016335538")
		r_day.set("14/03/2021")
		c_day.set("5")
		t_room.set("Empresarial")
		night_p.set("250000")
		calc_total = int(night_p.get()) * int(c_day.get())
		total.set(str(calc_total))
		userId.set("")

title = ("Arial", 20)
font_base = ("Arial", 18)
font_answers = ("Arial", 15)

root = tk.Tk()
root.title("Reservas")
root.config(bg="#dfe4ea")
root.geometry("800x500+300+100")
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file = "img/revision.png"))
tk.Label(root, text='Administración "Hotel Girasol"', bg="#eccc68", font=title).place(x=0, y=0, width=800, height=70)

tk.Button(root, text="Inicio", font=font_base, bg="#eccc68", command=index).place(x=700, y=90)
tk.Label(root, text="Identificacion ", bg="#dfe4ea", font=font_answers).place(x=20, y=150)

userId = StringVar()
tk.Entry(root, textvariable = userId, bg="#ced6e0", font=font_answers).place(x=150, y=150, width=300)
tk.Button(root, text="Consultar",  font=font_answers, bg="#eccc68", command=show).place(x=320, y=190)

condition = StringVar()
c = tk.Entry(root, textvariable = condition, bg="#ced6e0", font=font_answers)
c.insert(0,"Estado")
c.configure(state='disabled')
c.place(x=30, y=190, width=100)

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

age = StringVar()
a = tk.Entry(root, textvariable = age, bg="#ced6e0", font=font_answers)
a.insert(0,"Edad")
a.configure(state='disabled')
a.place(x=510, y=260, width=200)

tel = StringVar()
t = tk.Entry(root, textvariable = tel, bg="#ced6e0", font=font_answers)
t.insert(0,"Teléfono")
t.configure(state='disabled')
t.place(x=30, y=320, width=200)

r_day = StringVar()
rd = tk.Entry(root, textvariable = r_day, bg="#ced6e0", font=font_answers)
rd.insert(0,"Día de reserva")
rd.configure(state='disabled')
rd.place(x=270, y=320, width=200)

c_day = StringVar()
cd = tk.Entry(root, textvariable = c_day, bg="#ced6e0", font=font_answers)
cd.insert(0,"Cantidad de días")
cd.configure(state='disabled')
cd.place(x=510, y=320, width=200)

t_room = StringVar()
tr = tk.Entry(root, textvariable = t_room, bg="#ced6e0", font=font_answers)
tr.insert(0,"Tipo de habitación")
tr.configure(state='disabled')
tr.place(x=30, y=380, width=200)

night_p = StringVar()
np = tk.Entry(root, textvariable = night_p, bg="#ced6e0", font=font_answers)
np.insert(0,"Precio por noche")
np.configure(state='disabled')
np.place(x=270, y=380, width=200)

total = StringVar()
to = tk.Entry(root, textvariable = total, bg="#ced6e0", font=font_answers)
to.insert(0,"Total a pagar")
to.configure(state='disabled')
to.place(x=510, y=380, width=200)

tk.Button(root, text="Efectuar Pago", font=font_answers, bg="#eccc68").place(x=300, y=430)

root.mainloop()