import mysql.connector

class database:
	def __init__(self):
		super(database, self).__init__()
		
	global hotelGirasolDB	

	hotelGirasolDB = mysql.connector.connect(
		host='127.0.0.1',
		user='root',
		password='',
		database='bdhotelgirasol'
	)

######################################## RESERVAS #########################################################################################################################
	
	def obtainUserData(self, idNumber):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Nombre, Apellido, Telefono FROM usuario WHERE Num_Documento = %s"
		adr = (idNumber, )

		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		for x in myresult:
			dataFound = x
		return dataFound

	def obtainReserveId(self, idNumber):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Id_Reserva FROM usuario WHERE Num_Documento = %s"
		adr = (idNumber, )

		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		reserves = []

		for x in myresult:
			dataFound = x
			reserves.append(dataFound)
		return reserves

	def obtainReserveData(self, reserveId):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Cant_Ninos, Cant_Adulto, Cant_Camas, Cant_Noches, Fecha_Ingreso, Fecha_Salida, Estado  FROM reserva WHERE Id_Reserva = %s"
		adr = (reserveId, )

		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		reserves = []

		for x in myresult:
			dataFound = x
			reserves.append(dataFound)
		return reserves

	def activateReserve(self, reserveId):
		mycursor = hotelGirasolDB.cursor()
		sql = "UPDATE reserva SET Estado = %s WHERE Id_Reserva = %s"
		adr = (2, reserveId)

		mycursor.execute(sql, adr)

		hotelGirasolDB.commit()


######################################## RESERVAS #########################################################################################################################

######################################## ELIMINAR RESERVAS #########################################################################################################################

	def obtainUserDataToDelete(self, idNumber):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Id_Usuario, Nombre, Apellido, Correo, Telefono, Id_Reserva FROM usuario WHERE Num_Documento = %s"
		adr = (idNumber, )

		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		for x in myresult:
			dataFound = x
		return dataFound

	def obtainReserveDataToDelete(self, idUser):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT * FROM reserva WHERE Id_Reserva = %s"
		adr = (idUser, )

		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		for x in myresult:
			dataFound = x
		return dataFound

	def obtainRoomData(self, idReserve):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Id_Habitacion FROM reserva WHERE Id_Reserva = %s"
		adr = (idReserve, )

		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		for x in myresult:
			dataFound = x
		return dataFound[0]

	def deleteReserves(self, userId, reserveId):
		mycursor = hotelGirasolDB.cursor()

		deleteUserInfo = "DELETE FROM usuario WHERE Id_Usuario = %s"
		userInfo = (userId, )
		deleteReserveInfo = "DELETE FROM reserva WHERE Id_Reserva = %s"
		reserveInfo = (reserveId, )


		mycursor.execute(deleteUserInfo, userInfo)
		mycursor.execute(deleteReserveInfo, reserveInfo)

		hotelGirasolDB.commit()


######################################## ELIMINAR RESERVAS #########################################################################################################################

######################################## REGISTRO EXTENDIDO #########################################################################################################################
	
	def obtainUserInformation(self, reserveId):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Nombre, Apellido, Num_Documento FROM usuario WHERE Id_Reserva = %s"
		adr = (reserveId, )

		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		for x in myresult:
			dataFound = x
		return dataFound

	def obtainReserveInformation(self, reserveId):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Fecha_Ingreso, Fecha_Salida, Id_Habitacion FROM reserva WHERE Id_Reserva = %s"
		adr = (reserveId, )

		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		for x in myresult:
			dataFound = x
		return dataFound
 
	def insertIntoExtendRecord(self, name, lastName, idNumber, inDate, outDate, roomId):
		mycursor = hotelGirasolDB.cursor()

		sql = "INSERT INTO registroextendido (Nombre, Apellido, Num_Documento, Fecha_Ingreso, Fecha_Salida, Habitacion) VALUES (%s, %s, %s, %s, %s, %s)"
		val = (name, lastName, idNumber, inDate, outDate, roomId)
		mycursor.execute(sql, val)

		hotelGirasolDB.commit()	

	def showUsers(self):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT * FROM registroextendido"
		mycursor.execute(sql)

		myresult = mycursor.fetchall()

		recordsList = []

		for x in myresult:
			data = x
			recordsList.append(data)

		if recordsList == []:
			return False
		else:
			return recordsList
			

######################################## REGISTRO EXTENDIDO #########################################################################################################################

######################################## FACTURACION #########################################################################################################################

	def userDataToInvoice(self, idNumber):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Id_Usuario, Nombre, Apellido, Telefono from usuario where Num_Documento = %s"
		user = (idNumber, )

		mycursor.execute(sql, user)

		myresult = mycursor.fetchall()

		for x in myresult:
			userData = x
		return userData

	def reserveIds(self, idNumber):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Id_Reserva from usuario where Num_Documento = %s"
		user = (idNumber, )

		mycursor.execute(sql, user)

		myresult = mycursor.fetchall()

		reserves = []

		for x in myresult:
			data = x
			reserves.append(data)

		return reserves

	def reserveDataToInvoice(self, reserveId):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Cant_Noches, Cant_Camas, Estado from reserva where Id_Reserva = %s"
		user = (reserveId, )

		mycursor.execute(sql, user)

		myresult = mycursor.fetchall()

		reserveData = []

		for x in myresult:
			userData = x
			reserveData.append(userData)
		return reserveData

	def roomIds(self, reserveId):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Id_Habitacion from reserva where Id_Reserva = %s"
		user = (reserveId, )

		mycursor.execute(sql, user)

		myresult = mycursor.fetchall()

		rooms = []

		for x in myresult:
			data = x
			rooms.append(data)

		return rooms

	def roomDataToInvoice(self, roomId):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Descripcion, Valor from habitacion where Id_Habitacion = %s"
		user = (roomId, )

		mycursor.execute(sql, user)

		myresult = mycursor.fetchall()

		roomList = []

		for x in myresult:
			roomData = x
			roomList.append(roomData)
		return roomList

    ##########################################################################################################



	def saveInvoiceDetails(self, name, lastName, cellphone, total, reserveId):
		mycursor = hotelGirasolDB.cursor()

		sql = "INSERT INTO detallefactura (nombreCliente, apellidoCliente, telefonoCliente, totalFactura, idReserva) VALUES (%s, %s, %s, %s, %s)"
		val = (name, lastName, cellphone, total, reserveId)
		mycursor.execute(sql, val)

		hotelGirasolDB.commit()	

	def saveRoomDetails(self, roomId, desciption, beeds, nights, value, subTotal, reserveId):
		mycursor = hotelGirasolDB.cursor()

		sql = "INSERT INTO detalleproducto (idHabitacion, descripcion, camas, noches, valor, subTotal, idReserva) VALUES (%s, %s, %s, %s, %s, %s, %s)"
		val = (roomId, desciption, beeds, nights, value, subTotal, reserveId)
		mycursor.execute(sql, val)

		hotelGirasolDB.commit()	

	def obtainProductIdSaved(self, reserveId):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT idDetalleProducto from detalleproducto where idReserva = %s"
		user = (reserveId, )

		mycursor.execute(sql, user)

		myresult = mycursor.fetchall()

		idList = []

		for x in myresult:
			roomData = x
			idList.append(roomData)
		return idList

	def obtainInvoiceIdSaved(self, reserveId):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT id_DetalleFactura from detallefactura where idReserva = %s"
		user = (reserveId, )

		mycursor.execute(sql, user)

		myresult = mycursor.fetchall()

		idList = []

		for x in myresult:
			roomData = x
			idList.append(roomData)
		return idList

	def saveInvoice(self, productId, invoiceId):
		mycursor = hotelGirasolDB.cursor()

		sql = "INSERT INTO factura (idDetalleProducto, idDetalleFactura) VALUES (%s, %s)"
		val = (productId, invoiceId)
		mycursor.execute(sql, val)

		hotelGirasolDB.commit()	



######################################## FACTURACION #########################################################################################################################