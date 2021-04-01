import mysql.connector

class database:
	def __init__(self):
		super(database, self).__init__()
		
	global hotelGirasolDB	

	hotelGirasolDB = mysql.connector.connect(
		host='127.0.0.1',
		user='root',
		password='',
		database='hotel_girasol'
	)

######################################## RESERVAS #########################################################################################################################
	def obtainUserData(self, idNumber):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Id_Usuario, Nombre, Apellido FROM usuario WHERE Num_Documento = %s"
		adr = (idNumber, )

		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		for x in myresult:
			dataFound = x
		return dataFound

	def obtainReserveData(self, idUser):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT * FROM reserva WHERE Id_Usuario = %s"
		adr = (idUser, )

		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		for x in myresult:
			dataFound = x
		return dataFound

	def changeStatus(self, idUser):
		mycursor = hotelGirasolDB.cursor()
		sql = "UPDATE reserva SET Estado = %s WHERE Id_Usuario = %s"
		val = (2, idUser)

		mycursor.execute(sql, val)

		hotelGirasolDB.commit()
######################################## RESERVAS #########################################################################################################################

######################################## ELIMINAR RESERVAS #########################################################################################################################

	def obtainUserDataToDelete(self, idNumber):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Id_Usuario, Nombre, Apellido, Correo, Telefono FROM usuario WHERE Num_Documento = %s"
		adr = (idNumber, )

		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		for x in myresult:
			dataFound = x
		return dataFound

	def obtainReserveDataToDelete(self, idUser):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT * FROM reserva WHERE Id_Usuario = %s"
		adr = (idUser, )

		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		for x in myresult:
			dataFound = x
		return dataFound

	def obtainRoomIdToDelete(self, reserveId):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Id_Habitacion FROM habitacion WHERE Id_Reserva = %s"
		adr = (reserveId, )

		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		for x in myresult:
			dataFound = x
		return dataFound

	def deleteReserves(self, userId, reserveId):
		mycursor = hotelGirasolDB.cursor()

		deleteUserInfo = "DELETE FROM usuario WHERE Id_Usuario = %s"
		userInfo = (userId, )
		deleteReserveInfo = "DELETE FROM reserva WHERE Id_Usuario = %s"
		deleteRoomInfo = "DELETE FROM reserva WHERE Id_Usuario = %s"
		roomInfo = (reserveId, )


		mycursor.execute(deleteUserInfo, userInfo)
		mycursor.execute(deleteReserveInfo, userInfo)
		mycursor.execute(deleteRoomInfo, roomInfo)

		hotelGirasolDB.commit()


######################################## ELIMINAR RESERVAS #########################################################################################################################

######################################## REGISTRO EXTENDIDO #########################################################################################################################

	def showUsers(self):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT * FROM registroextendido"
		mycursor.execute(sql)

		myresult = mycursor.fetchall()

		for x in myresult:
			data = x
			

######################################## REGISTRO EXTENDIDO #########################################################################################################################

######################################## FACTURACION #########################################################################################################################
	def executeInvoice(self, idNumber, specialRequest, concept, value, total):
		
		obtainId = self.searchUserId(idNumber)
		obtainReserveId = self.searchReserveId(obtainId)
		obtainRoomId = self.searchRoomId(obtainReserveId)

		mycursor = hotelGirasolDB.cursor()

		sql = "INSERT INTO factura (Solicitud_Especial, Concepto, Valor, Total, Id_Reserva, Id_Habitacion) VALUES (%s, %s, %s, %s, %s, %s)"
		val = (specialRequest, concept, int(value), int(total), int(obtainReserveId), int(obtainRoomId))
		mycursor.execute(sql, val)

		hotelGirasolDB.commit()

	def searchUserId(self, idNumber):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Id_Usuario FROM usuario WHERE Num_Documento = %s"
		adr = (idNumber, )
		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		for x in myresult:
			idFound = x
		return idFound[0]

	def searchReserveId(self, userId):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Id_Reserva FROM reserva WHERE Id_Usuario = %s"
		adr = (userId, )
		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		for x in myresult:
			idFound = x

		return idFound[0]

	def searchRoomId(self, reserveId):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT Id_Habitacion FROM habitacion WHERE Id_Reserva = %s"
		adr = (reserveId, )
		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		for x in myresult:
			idFound = x
		return idFound[0]

	def searchUserData(self, userId):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT * FROM usuario WHERE Id_Usuario = %s"
		adr = (userId, )
		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		for x in myresult:
			dataFound = x
		return dataFound

	def searchReserveData(self, userId):
		mycursor = hotelGirasolDB.cursor()
		sql = "SELECT * FROM reserva WHERE Id_Usuario = %s"
		adr = (userId, )
		mycursor.execute(sql, adr)

		myresult = mycursor.fetchall()

		for x in myresult:
			dataFound = x

		return dataFound


	def insertIntoExtendRecord(self, name, lastName, numberId, inDate, outDate):
		mycursor = hotelGirasolDB.cursor()

		sql = "INSERT INTO registroextendido (Nombre, Apellido, Num_Documento, Fecha_Ingreso, Fecha_Salida) VALUES (%s, %s, %s, %s, %s)"

		val = (name, lastName, numberId, inDate, outDate)

		mycursor.execute(sql, val)

		hotelGirasolDB.commit()


######################################## FACTURACION #########################################################################################################################