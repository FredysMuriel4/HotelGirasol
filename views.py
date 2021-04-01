import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
from tkinter import ttk

from queries import database

db = database()


class Views:
	def login(self):
		def enter():
			fun_empty = empty(user.get(), password.get())
			if fun_empty != 0:
				if user.get() == "a" and password.get() == "a":
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
			userData = db.obtainUserData(int(userId.get()))
			global globalUserId
			globalUserId = userId.get()
			name.set(userData[1])
			lastName.set(userData[2])
			reserveData = db.obtainReserveData(int(userData[0]))
			if reserveData[8] == 1:
				condition.set("Pendiente")
			elif reserveData[8] == 2:
				condition.set("Activo")
			childsQuant.set(str(reserveData[6]) + " Niños")
			dadsQuant.set(str(reserveData[5]) + " Adultos")
			bedQuant.set(str(reserveData[4]) + " Camas")
			nightQuant.set(str(reserveData[3]) + " Noches")
			inDate.set(reserveData[1])
			outDate.set(reserveData[2])
			idBooking.set("# Reserva: " + str(reserveData[0]))
			userId.set('')

		def activate():
			if condition.get() == "Pendiente":
				condition.set("Activo")
				userIdObtain = db.obtainUserData(globalUserId)
				db.changeStatus(userIdObtain[0])
				messagebox.showinfo(message='Estado cambiado a "ACTIVO".', title="Proceso exitoso")
			elif condition.get() == "Activo":
				messagebox.showerror(message="Error, el usuario ya está activado", title="Error")

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

		lastName = StringVar()
		ln = tk.Entry(root, textvariable = lastName, bg="#ced6e0", font=font_answers)
		ln.insert(0,"Apellido")
		ln.configure(state='disabled')
		ln.place(x=270, y=260, width=200)

		childsQuant = StringVar()
		a = tk.Entry(root, textvariable = childsQuant, bg="#ced6e0", font=font_answers)
		a.insert(0,"Cantidad Niños")
		a.configure(state='disabled')
		a.place(x=510, y=260, width=200)

		dadsQuant = StringVar()
		t = tk.Entry(root, textvariable = dadsQuant, bg="#ced6e0", font=font_answers)
		t.insert(0,"Cantidad Adultos")
		t.configure(state='disabled')
		t.place(x=30, y=320, width=200)

		bedQuant = StringVar()
		rd = tk.Entry(root, textvariable = bedQuant, bg="#ced6e0", font=font_answers)
		rd.insert(0,"Cantidad Camas")
		rd.configure(state='disabled')
		rd.place(x=270, y=320, width=200)

		nightQuant = StringVar()
		cd = tk.Entry(root, textvariable = nightQuant, bg="#ced6e0", font=font_answers)
		cd.insert(0,"Cantidad Noches")
		cd.configure(state='disabled')
		cd.place(x=510, y=320, width=200)

		inDate = StringVar()
		tr = tk.Entry(root, textvariable = inDate, bg="#ced6e0", font=font_answers)
		tr.insert(0,"Fecha Ingreso")
		tr.configure(state='disabled')
		tr.place(x=30, y=380, width=200)

		outDate = StringVar()
		n = tk.Entry(root, textvariable = outDate, bg="#ced6e0", font=font_answers)
		n.insert(0,"Fecha Salida")
		n.configure(state='disabled')
		n.place(x=270, y=380, width=200)

		idBooking = StringVar()
		ln = tk.Entry(root, textvariable = idBooking, bg="#ced6e0", font=font_answers)
		ln.insert(0,"# Reserva")
		ln.configure(state='disabled')
		ln.place(x=510, y=380, width=200)

		tk.Button(root, text="Activar", font=font_answers, bg="#eccc68", command=activate).place(x=330, y=430)

		root.mainloop()

	def delete(self):
		def index():
			root.destroy()
			self.index()

		def show():
			userDataToDelete = db.obtainUserDataToDelete(int(userId.get()))
			global userIdToDelete
			userIdToDelete = userDataToDelete[0]
			name.set(userDataToDelete[1])
			lastName.set(userDataToDelete[2])
			email.set(userDataToDelete[3])
			tel.set(userDataToDelete[4])
			reserveDataToDelete = db.obtainReserveDataToDelete(userDataToDelete[0])
			global reserveIdToDelete
			reserveIdToDelete = reserveDataToDelete[0]
			if reserveDataToDelete[8] == 1:
				condition.set("Pendiente")
			elif reserveDataToDelete[8] == 2:
				condition.set("Activo")
			inDate.set(reserveDataToDelete[1])
			outDate.set(reserveDataToDelete[2])
			roomIdToDelete = db.obtainRoomIdToDelete(reserveDataToDelete[0])
			roomId.set("# Habitación " + str(roomIdToDelete[0]))

		def delete():
				db.deleteReserves(userIdToDelete, reserveIdToDelete)
				messagebox.showinfo(message="Eliminación exitosa")
				self.index()

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

		lastName = StringVar()
		ln = tk.Entry(root, textvariable = lastName, bg="#ced6e0", font=font_answers)
		ln.insert(0,"Apellido")
		ln.configure(state='disabled')
		ln.place(x=270, y=260, width=200)

		email = StringVar()
		a = tk.Entry(root, textvariable = email, bg="#ced6e0", font=font_answers)
		a.insert(0,"Correo")
		a.configure(state='disabled')
		a.place(x=510, y=260, width=200)

		tel = StringVar()
		t = tk.Entry(root, textvariable = tel, bg="#ced6e0", font=font_answers)
		t.insert(0,"Teléfono")
		t.configure(state='disabled')
		t.place(x=30, y=320, width=200)

		inDate = StringVar()
		rd = tk.Entry(root, textvariable = inDate, bg="#ced6e0", font=font_answers)
		rd.insert(0,"Fecha Ingreso")
		rd.configure(state='disabled')
		rd.place(x=270, y=320, width=200)

		outDate = StringVar()
		cd = tk.Entry(root, textvariable = outDate, bg="#ced6e0", font=font_answers)
		cd.insert(0,"Fecha Salida")
		cd.configure(state='disabled')
		cd.place(x=510, y=320, width=200)

		roomId = StringVar()
		tr = tk.Entry(root, textvariable = roomId, bg="#ced6e0", font=font_answers)
		tr.insert(0,"# Habitacion")
		tr.configure(state='disabled')
		tr.place(x=30, y=380, width=200)

		tk.Button(root, text="Eliminar Reserva", font=font_answers, bg="#eccc68", command=delete).place(x=300, y=430)

		root.mainloop()

	def facturation(self):
		def index():
			root.destroy()
			self.index()
		def validate():
			userData = db.obtainUserData(userId.get())

			global userDataToInsertIntoExtendRecord
			userDataToInsertIntoExtendRecord = db.searchUserData(userData[0])
			global reserveDataToInsertIntoExtendRecord
			reserveDataToInsertIntoExtendRecord = db.searchReserveData(userData[0])

			reserveData = db.obtainReserveData(userData[0])
			if reserveData[8] == 2:
				condition.set("Activo")
				n.config(state='normal')
				ln.config(state='normal')
				a.config(state='normal')
				t.config(state='normal')
			else:
				messagebox.showerror(message="Error, no se encontró al usuario", title="Error")

		def saveInvoice():
			if condition.get() == "Activo":
				db.executeInvoice(int(userId.get()), specialRequest.get(), concept.get(), value.get(), total.get())
				db.insertIntoExtendRecord(userDataToInsertIntoExtendRecord[1], userDataToInsertIntoExtendRecord[2], userDataToInsertIntoExtendRecord[6], reserveDataToInsertIntoExtendRecord[1], reserveDataToInsertIntoExtendRecord[2])
				messagebox.showinfo(message="Factura exitosa.", title="Facturación exitosa")
				index()

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
		tk.Button(root, text="Consultar",  font=font_answers, bg="#eccc68", command=validate).place(x=320, y=190)
		
		condition = StringVar()
		c = tk.Entry(root, textvariable = condition, bg="#ced6e0", font=font_answers)
		c.insert(0,"Estado")
		c.configure(state='disabled')
		c.place(x=30, y=190, width=100)

		specialRequest = StringVar()
		n = tk.Entry(root, textvariable = specialRequest, bg="#ced6e0", font=font_answers)
		n.insert(0,"Solicitud Especial ")
		n.config(state='readonly')
		n.place(x=30, y=260, width=200)

		concept = StringVar()
		ln = tk.Entry(root, textvariable = concept, bg="#ced6e0", font=font_answers)
		ln.insert(0,"Concepto")
		ln.config(state='readonly')
		ln.place(x=270, y=260, width=200)

		value = StringVar()
		a = tk.Entry(root, textvariable = value, bg="#ced6e0", font=font_answers)
		a.insert(0,"Valor")
		a.config(state='readonly')
		a.place(x=30, y=320, width=200)

		total = StringVar()
		t = tk.Entry(root, textvariable = total, bg="#ced6e0", font=font_answers)
		t.insert(0,"Total")
		t.config(state='readonly')
		t.place(x=270, y=320, width=200)

		tk.Button(root, text="Efectuar Pago", font=font_answers, bg="#eccc68", command=saveInvoice).place(x=530, y=270)
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
		table = ttk.Treeview(frame, columns=("name","lastName", "document", "inDate","outDate","room"), yscrollcommand = sb.set )

		table.column("#0", width=5, minwidth=5)
		table.column("name", width=80, minwidth=80)
		table.column("lastName", width=80, minwidth=80)
		table.column("document", width=100, minwidth=100)
		table.column("inDate", width=80, minwidth=80)
		table.column("outDate", width=80, minwidth=80)
		table.column("room", width=100, minwidth=100)

		table.heading("#0", text="#", anchor="w")
		table.heading("name",text="Nombre", anchor="w")
		table.heading("lastName",text="Apellido", anchor="w")
		table.heading("document",text="# Documento", anchor="w")
		table.heading("inDate",text="Ingreso", anchor="w")
		table.heading("outDate",text="Salida", anchor="w")
		table.heading("room",text="Habitacion", anchor="w")

		sb.config( command = table.yview )
		table.pack(fill=tk.X, side=tk.LEFT, expand=False)

		frame.place(x=110, y=200)

		root.mainloop()
