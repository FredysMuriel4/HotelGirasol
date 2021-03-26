import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
from tkinter import ttk


class Views:
	def login(self):
		def enter():
			fun_empty = empty(user.get(), password.get())
			if fun_empty != 0:
				if user.get() == "Admin" and password.get() == "Administracion":
					root.destroy()
					global username
					username = user.get()
					self.index()
			else:
				messagebox.showerror(message="Usuario o conraseña incorrectos, verifique", title="Error")
		def empty(user, password):
			if user == '' or password == '':
				return 0
		title = ("Arial", 20)
		font_base = ("Arial", 18)
		font_answers = ("Arial", 15)

		root = tk.Tk()
		root.title("Login")
		root.config(bg="#dfe4ea")
		root.geometry("800x500+300+100")
		root.resizable(0,0)
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
		tk.Button(root, text="Ingresar", font=font_base, bg="#eccc68", command=enter).place(x=470, y=350)
		root.mainloop()
	def index(self):
		def exit():
			root.destroy()
			self.login()

		def bookings():
			root.destroy()
			self.bookings()

		def delete():
			root.destroy()
			self.delete()

		def facturation():
			root.destroy()
			self.facturation()

		def extendrecords():
			root.destroy()
			self.extendRecords()

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
		tk.Label(root, text='Bienvenido '+username, bg="#dfe4ea", font=font_answers).place(x=20, y=100)
		tk.Label(root, text='Opciones: ', bg="#dfe4ea", font=font_answers).place(x=20, y=150)
		rImg = tk.PhotoImage(file="img/stock.png")
		tk.Button(root, text="Revisar Reservas", font=font_answers, bg="#eccc68", command=bookings).place(x=20, y=200, width=180)
		tk.Label(root, image=rImg, bg="#eccc68").place(x=202, y=202, height=35)
		dImg = tk.PhotoImage(file="img/remove.png")
		tk.Button(root, text="Eliminar Reservas", font=font_answers, bg="#eccc68", command=delete).place(x=20, y=250, width=180)
		tk.Label(root, image=dImg, bg="#eccc68").place(x=204, y=252, height=35)
		sImg = tk.PhotoImage(file="img/stock.png")
		tk.Button(root, text="Registro Extendido", font=font_answers, bg="#eccc68", command=extendrecords).place(x=20, y=300, width=180)
		tk.Label(root, image=sImg, bg="#eccc68").place(x=204, y=302, height=35)
		fImg = tk.PhotoImage(file="img/invoice.png")
		tk.Button(root, text="Facturación", font=font_answers, bg="#eccc68", command=facturation).place(x=20, y=350, width=180)
		tk.Label(root, image=fImg, bg="#eccc68").place(x=204, y=352, height=35)

		root.mainloop()

	def bookings(self):
		def index():
			root.destroy()
			self.index()

		def show():
			if userId.get() == "1001947524":
				condition.set("Pendiente")
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
			else:
				messagebox.showerror(message="No se ha encontrado el documento.", title="Error")

		def pay():
			if condition.get() == "Pendiente":
				condition.set("Activo")
				messagebox.showinfo(message='Estado cambiado a "ACTIVO".', title="Proceso exitoso")
			else:
				messagebox.showerror(message="Error", title="Error")

		title = ("Arial", 20)
		font_base = ("Arial", 18)
		font_answers = ("Arial", 15)

		root = tk.Tk()
		root.title("Reservas")
		root.config(bg="#dfe4ea")
		root.geometry("800x500+300+100")
		root.resizable(0,0)
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

		tk.Button(root, text="Activar", font=font_answers, bg="#eccc68", command=pay).place(x=330, y=430)

		root.mainloop()

	def delete(self):
		def index():
			root.destroy()
			self.index()

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
				userId.set("")
			else:
				messagebox.showerror(message="No se ha encontrado el documento.", title="Error")

		def delete():
				condition.set("")
				name.set("")
				last_name.set("")
				age.set("")
				tel.set("")
				r_day.set("")
				c_day.set("")
				t_room.set("")
				userId.set("")
				messagebox.showinfo(message="Eliminación exitosa")

		title = ("Arial", 20)
		font_base = ("Arial", 18)
		font_answers = ("Arial", 15)

		root = tk.Tk()
		root.title("Eliminar reserva")
		root.config(bg="#dfe4ea")
		root.geometry("800x500+300+100")
		root.resizable(0,0)
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

		tk.Button(root, text="Eliminar Reserva", font=font_answers, bg="#eccc68", command=delete).place(x=300, y=430)

		root.mainloop()

	def facturation(self):
		def index():
			root.destroy()
			self.index()

		title = ("Arial", 20)
		font_base = ("Arial", 18)
		font_answers = ("Arial", 15)

		root = tk.Tk()
		root.title("Reservas")
		root.config(bg="#dfe4ea")
		root.geometry("800x500+300+100")
		root.resizable(0,0)
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

	def extendRecords(self):
		def exit():
		    root.destroy()
		    self.index()
		def showExtendRecord():
		    table.insert("", tk.END , text="" , values=("Fredys", "Muriel", "1001947524", "19", "21/05/2021","25/05/2021","P1 H3"))
		    table.insert("", tk.END , text="" , values=("Fredys", "Muriel", "1001947524", "19", "21/05/2021","25/05/2021","P1 H3"))
		    table.insert("", tk.END , text="" , values=("Fredys", "Muriel", "1001947524", "19", "21/05/2021","25/05/2021","P1 H3"))


		title = ("Arial", 20)
		font_base = ("Arial", 18)
		font_answers = ("Arial", 15)

		root = tk.Tk()
		root.title("Login")
		root.config(bg="#dfe4ea")
		root.geometry("800x500+300+100")
		root.resizable(0,0)
		root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file = "img/revision.png"))
		tk.Label(root, text='Administración "Hotel Girasol"', bg="#eccc68", font=title).place(x=0, y=0, width=800, height=70)

		tk.Button(root, text="Inicio", font=font_base, bg="#eccc68", command=exit).place(x=700, y=90)

		tk.Button(root, text="Ver Registro Extendido", font=font_base, bg="#eccc68", command=showExtendRecord).place(x=110, y=130)

		frame = tk.Frame(root)

		sb = tk.Scrollbar(frame)
		sb.pack(side = tk.RIGHT, fill = tk.Y)

		#table
		table = ttk.Treeview(frame, columns=("name","lastName", "document", "age","inDate","outDate","room"), yscrollcommand = sb.set )

		table.column("#0", width=5, minwidth=5)
		table.column("name", width=80, minwidth=80)
		table.column("lastName", width=80, minwidth=80)
		table.column("document", width=100, minwidth=100)
		table.column("age", width=50, minwidth=50)
		table.column("inDate", width=80, minwidth=80)
		table.column("outDate", width=80, minwidth=80)
		table.column("room", width=100, minwidth=100)

		table.heading("#0", text="#", anchor="w")
		table.heading("name",text="Nombre", anchor="w")
		table.heading("lastName",text="Apellido", anchor="w")
		table.heading("document",text="# Documento", anchor="w")
		table.heading("age",text="Edad", anchor="w")
		table.heading("inDate",text="Ingreso", anchor="w")
		table.heading("outDate",text="Salida", anchor="w")
		table.heading("room",text="Habitacion", anchor="w")

		sb.config( command = table.yview )
		table.pack(fill=tk.X, side=tk.LEFT, expand=False)

		frame.place(x=110, y=200)

		root.mainloop()
