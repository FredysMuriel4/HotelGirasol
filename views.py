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
				if user.get() == "Administrador" and password.get() == "Administrador":
					root.destroy()
					global username
					username = user.get()
					self.index()
				else:
					messagebox.showerror(message="Usuario o conraseña incorrectos, verifique", title="Error")
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
		def search():
			table.delete(*table.get_children())
			global idNumber
			idNumber = userId.get()
			userData = db.obtainUserData(userId.get())
			reservesObtained = db.obtainReserveId(userId.get())
			name.set(userData[0])
			lastName.set(userData[1])
			cellphone.set(userData[2])
			pos = 0
			for reserve in reservesObtained:
				pos += 1
				reserveInfo = db.obtainReserveData(reserve[0])
				for x in reserveInfo:
					if x[6] == 1:
						condition = "Pendiente"
					elif x[6] == 2:
						condition = "Activo"
					table.insert("", tk.END , text="" , values=(pos, x[0], x[1], x[2], x[3], x[4], x[5], condition, reserve[0]))
			userId.set('')

		def activate():
			obtainReserveIdToActivate = db.obtainReserveId(idNumber)
			for reserve in obtainReserveIdToActivate:
				db.activateReserve(reserve[0])
			messagebox.showinfo(message="Reservas activadas correctamente.", title="Activado")
			index()

		title = ("Arial", 20)
		font_base = ("Arial", 18)
		font_answers = ("Arial", 15)

		root = tk.Tk()
		root.title("Reservas")
		root.config(bg="#dfe4ea")
		root.geometry("770x500+300+100")
		root.resizable(0,0)
		root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file = "img/revision.png"))
		tk.Label(root, text='Administración "Hotel Girasol"', bg="#eccc68", font=title).place(x=0, y=0, width=770, height=70)

		tk.Button(root, text="Inicio", font=font_base, bg="#eccc68", command=index).place(x=670, y=10)
		tk.Label(root, text="Identificacion ", bg="#dfe4ea", font=font_answers).place(x=20, y=100)

		userId = StringVar()
		tk.Entry(root, textvariable = userId, bg="#ced6e0", font=font_answers).place(x=150, y=100, width=250,  height=30)
		tk.Button(root, text="Consultar",  font=font_answers, bg="#eccc68", command=search).place(x=450, y=95)

		name = StringVar()
		n = tk.Entry(root, textvariable = name, bg="#ced6e0", font=font_answers)
		n.insert(0,"Nombre")
		n.configure(state='disabled')
		n.place(x=30, y=170, width=128)

		lastName = StringVar()
		ln = tk.Entry(root, textvariable = lastName, bg="#ced6e0", font=font_answers)
		ln.insert(0,"Apellido")
		ln.configure(state='disabled')
		ln.place(x=230, y=170, width=128)

		cellphone = StringVar()
		a = tk.Entry(root, textvariable = cellphone, bg="#ced6e0", font=font_answers)
		a.insert(0,"Teléfono")
		a.configure(state='disabled')
		a.place(x=430, y=170, width=128)

		frame = tk.Frame(root)

		sb = tk.Scrollbar(frame)
		sb.pack(side = tk.RIGHT, fill = tk.Y)

		#table
		table = ttk.Treeview(frame, columns=("#","childs","adults", "beeds", "nights", "inDate", "outDate", "condition", "reserveId"), yscrollcommand = sb.set )

		table.column("#0", width=0, minwidth=0)
		table.column("#", width=25, minwidth=25)
		table.column("childs", width=50, minwidth=50, anchor="c")
		table.column("adults", width=50, minwidth=50, anchor="c")
		table.column("beeds", width=50, minwidth=50, anchor="c")
		table.column("nights", width=50, minwidth=50, anchor="c")
		table.column("inDate", width=100, minwidth=100)
		table.column("outDate", width=100, minwidth=100)
		table.column("condition", width=80, minwidth=80)
		table.column("reserveId", width=80, minwidth=80, anchor="c")


		table.heading("#0", text="", anchor="w")
		table.heading("#", text="#", anchor="w")
		table.heading("childs",text="Niños", anchor="w")
		table.heading("adults",text="Adultos", anchor="w")
		table.heading("beeds",text="Camas", anchor="w")
		table.heading("nights",text="Noches", anchor="w")
		table.heading("inDate",text="Fecha Entrada", anchor="w")
		table.heading("outDate",text="Fecha Salida", anchor="w")
		table.heading("condition", text="Estado", anchor="w")
		table.heading("reserveId",text="# Reserva", anchor="w")

		sb.config( command = table.yview )
		table.pack(fill=tk.X, side=tk.LEFT, expand=False)

		frame.place(x=30, y=230)

		tk.Button(root, text="Activar", font=font_base, bg="#eccc68", command=activate).place(x=650, y=320)

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
			reserveDataToDelete = db.obtainReserveDataToDelete(userDataToDelete[5])
			global reserveIdToDelete
			reserveIdToDelete = reserveDataToDelete[0]
			if reserveDataToDelete[8] == 1:
				condition.set("Pendiente")
			elif reserveDataToDelete[8] == 2:
				condition.set("Activo")
			inDate.set(reserveDataToDelete[1])
			outDate.set(reserveDataToDelete[2])
			roomIdToDelete = db.obtainRoomData(reserveDataToDelete[0])
			roomId.set("# Habitación " + str(roomIdToDelete))

		def delete():
				db.deleteReserves(userIdToDelete, reserveIdToDelete)
				messagebox.showinfo(message="Eliminación exitosa")
				index()

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
		
		def search():
			table.delete(*table.get_children())
			userInfoToInvoice = db.userDataToInvoice(userId.get())
			reserves = db.reserveIds(userId.get())
			global userNumber
			userNumber = userId.get()
			pos = 0
			for x in reserves:
				pos += 1
				reserveInfoToInvoice = db.reserveDataToInvoice(x[0])

				for reserveInfo in reserveInfoToInvoice:
					if reserveInfo[2] == 2:
						condition.set("Activo")
						rooms = db.roomIds(x[0])

						for roomId in rooms:
							roomInfoToInvoice = db.roomDataToInvoice(roomId[0])

							for roomInfo in roomInfoToInvoice:
								table.insert("", tk.END , text="" , values=(pos, roomId[0], roomInfo[0], reserveInfo[1], reserveInfo[0], roomInfo[1], str(int(reserveInfo[0] * roomInfo[1]))))

						name.set(userInfoToInvoice[1])
						lastName.set(userInfoToInvoice[2])
						cellphone.set(userInfoToInvoice[3])

			calcTotal = 0
			for child in table.get_children():
				calcTotal += int(table.item(child)["values"][6])
			total.set(str(calcTotal))
			userId.set('')

		def checkIn():
			userInfoToSaveInvoice = db.userDataToInvoice(userNumber)
			reservesToSave = db.reserveIds(userNumber)
			pos = 0
			for x in reservesToSave:
				db.saveInvoiceDetails(name.get(), lastName.get(), cellphone.get(), total.get(), x[0])

			reserveIdList = []
			pos = 0

			for child in table.get_children():

				for reserveIdObtain in reservesToSave:

					r = reserveIdObtain[0]
					reserveIdList.append(r)

				db.saveRoomDetails(table.item(child)["values"][1], table.item(child)["values"][2], table.item(child)["values"][3], table.item(child)["values"][4], table.item(child)["values"][5], table.item(child)["values"][6], reserveIdList[pos])
				pos +=1
			idProductsList = []
			idInvoiceList = []
			pos = 0
			for idInfo in reservesToSave:
				for x in idInfo:
					pass
					for idProducts in db.obtainProductIdSaved(x):
						idProductsList.append(idProducts[0])	
					for idInvoices in db.obtainInvoiceIdSaved(x):
						idInvoiceList.append(idInvoices[0])
				db.insertIntoExtendRecord(db.obtainUserInformation(idInfo[0])[0], 
					db.obtainUserInformation(idInfo[0])[1],
					db.obtainUserInformation(idInfo[0])[2],
					db.obtainReserveInformation(idInfo[0])[0],
					db.obtainReserveInformation(idInfo[0])[1],
					db.obtainReserveInformation(idInfo[0])[2])
				db.saveInvoice(idProductsList[pos], idInvoiceList[pos])
				pos += 1
			messagebox.showinfo(message="Factura realizada exitosamente.", title="Exito.")
			index()


		title = ("Arial", 20)
		font_base = ("Arial", 18)
		font_answers = ("Arial", 15)

		root = tk.Tk()
		root.title("Facturar")
		root.config(bg="#dfe4ea")
		root.geometry("800x520+300+100")
		root.resizable(0,0)
		root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file = "img/revision.png"))
		tk.Label(root, text='Administración "Hotel Girasol"', bg="#eccc68", font=title).place(x=0, y=0, width=800, height=70)

		tk.Button(root, text="Atrás", font=font_base, bg="#eccc68", command=index).place(x=700, y=10)

		tk.Label(root, text="Identificacion ", bg="#dfe4ea", font=font_answers).place(x=20, y=100)

		userId = StringVar()
		tk.Entry(root, textvariable = userId, bg="#ced6e0", font=font_answers).place(x=150, y=100, width=250, height=30)
		tk.Button(root, text="Consultar",  font=font_answers, bg="#eccc68", command=search).place(x=450, y=95)

		condition = StringVar()
		c = tk.Entry(root, textvariable = condition, bg="#ced6e0", font=font_answers)
		c.insert(0,"Estado")
		c.configure(state='disabled')
		c.place(x=30, y=140, width=100)

		name = StringVar()
		n = tk.Entry(root, textvariable = name, bg="#ced6e0", font=font_answers)
		n.insert(0,"Nombre")
		n.configure(state='disabled')
		n.place(x=30, y=200, width=128)

		lastName = StringVar()
		ln = tk.Entry(root, textvariable = lastName, bg="#ced6e0", font=font_answers)
		ln.insert(0,"Apellido")
		ln.configure(state='disabled')
		ln.place(x=230, y=200, width=128)

		cellphone = StringVar()
		a = tk.Entry(root, textvariable = cellphone, bg="#ced6e0", font=font_answers)
		a.insert(0,"Teléfono")
		a.configure(state='disabled')
		a.place(x=430, y=200, width=128)

		frame = tk.Frame(root)

		sb = tk.Scrollbar(frame)
		sb.pack(side = tk.RIGHT, fill = tk.Y)

		#table
		table = ttk.Treeview(frame, columns=("#","roomId","description", "beeds", "nights","price", "subTotal"), yscrollcommand = sb.set )

		table.column("#0", width=0, minwidth=0)
		table.column("#", width=25, minwidth=25)
		table.column("roomId", width=80, minwidth=80, anchor="c")
		table.column("description", width=180, minwidth=180)
		table.column("beeds", width=50, minwidth=50, anchor="c")
		table.column("nights", width=50, minwidth=50, anchor="c")
		table.column("price", width=70, minwidth=70)
		table.column("subTotal", width=80, minwidth=80)

		table.heading("#0", text="", anchor="w")
		table.heading("#", text="#", anchor="w")
		table.heading("roomId",text="Habitación", anchor="w")
		table.heading("description",text="Descripción", anchor="w")
		table.heading("beeds",text="Camas", anchor="w")
		table.heading("nights",text="Noches", anchor="w")
		table.heading("price",text="Precio", anchor="w")
		table.heading("subTotal",text="SubTotal", anchor="w")

		sb.config( command = table.yview )
		table.pack(fill=tk.X, side=tk.LEFT, expand=False)

		frame.place(x=30, y=260)

		total = StringVar()
		a = tk.Entry(root, textvariable = total, bg="#ced6e0", font=font_answers)
		a.insert(0,"Total")
		a.configure(state='disabled')
		a.place(x=640, y=330, width=100)

		tk.Button(root, text="Facturar", font=font_base, bg="#eccc68", command=checkIn).place(x=635, y=380)

		root.mainloop()

	def extendRecords(self):
		def exit():
		    root.destroy()
		    self.index()
		def showExtendRecord():
			table.delete(*table.get_children())
			dataFromExtendRecords = db.showUsers()
			if dataFromExtendRecords == False:
				messagebox.showerror(message="No se encontraron registros.", title="Error")
			else:
				pos = 0
				for x in dataFromExtendRecords:
					pos += 1
					table.insert("", tk.END , text="" , values=(pos, x[0], x[1], x[2], x[3] ,x[4], x[5]))
					if x == '':
						x = ''
						break

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
		table = ttk.Treeview(frame, columns=("#","name","lastName", "document", "inDate","outDate", "roomId"), yscrollcommand = sb.set )

		table.column("#0", width=5, minwidth=5)
		table.column("#", width=30, minwidth=30, anchor="c")
		table.column("name", width=80, minwidth=80)
		table.column("lastName", width=80, minwidth=80)
		table.column("document", width=100, minwidth=100)
		table.column("inDate", width=80, minwidth=80)
		table.column("outDate", width=80, minwidth=80)
		table.column("roomId", width=80, minwidth=80, anchor="c")

		table.heading("#0", text="", anchor="w")
		table.heading("#", text="#", anchor="c")
		table.heading("name",text="Nombre", anchor="w")
		table.heading("lastName",text="Apellido", anchor="w")
		table.heading("document",text="# Documento", anchor="w")
		table.heading("inDate",text="Ingreso", anchor="w")
		table.heading("outDate",text="Salida", anchor="w")
		table.heading("roomId", text="Habitación", anchor="w")

		sb.config( command = table.yview )
		table.pack(fill=tk.X, side=tk.LEFT, expand=False)

		frame.place(x=110, y=200)

		root.mainloop()
