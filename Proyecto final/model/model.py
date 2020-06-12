from mysql import connector

class Model:
	"""
	*****************************************
	* A data model with MySQL for a amigo DB*
	*****************************************
	"""
	def __init__(self, config_db_file='config.txt'):
		self.config_db_file = config_db_file
		self.config_db = self.read_config_db()
		self.connect_to_db()

	def read_config_db(self):
		d = {}
		with open(self.config_db_file) as f_r:
			for line in f_r:
				(key, val) = line.strip().split(':')
				d[key] = val
		return d 

	def connect_to_db(self):
		self.cnx = connector.connect(**self.config_db)
		self.cursor = self.cnx.cursor()

	def close_db(self):
		self.cnx.close()

	def read_a_pass(self,descripcion, password):
		try:
	 		sql = 'SELECT * FROM FAC_USUARIO WHERE DESCRIPCION=%s and PASSWORD = %s'
	 		vals = (descripcion, password)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
		except connector.Error as err:
	 		return err		
		
	def create_cat(self, descripcion, estatus, fechacreacion):
		try:
			sql = 'INSERT INTO FAC_CATEGORIA (`DESCRIPCION`, `ESTATUSREGISTRO`, `FECHACREACION`) VALUES (%s, %s, %s)'
			vals = (descripcion, estatus, fechacreacion)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err	
	def lectura_descripcion(self):
		try:
			sql = 'SELECT descripcion FROM FAC_CATEGORIA'
			self.cursor.execute(sql)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def lectura_descripcion_alta(self):
		try:
			sql = 'SELECT descripcion FROM FAC_CATEGORIA WHERE ESTATUSREGISTRO=0'
			self.cursor.execute(sql)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def lectura_descripcion_box(self, nombre):
		try:
			sql = 'SELECT IDCATEGORIA FROM FAC_CATEGORIA WHERE DESCRIPCION=%s'
			vals=(nombre,)
			self.cursor.execute(sql,vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def edit_cat(self,descripcion, fechamodificacion, idcat):
		try:
			sql = 'UPDATE FAC_CATEGORIA SET DESCRIPCION = %s, FECHAMODIFICACION = %s WHERE IDCATEGORIA = %s'
			vals = (descripcion, fechamodificacion, idcat)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err	

	def estatus_cat(self,estatus, fechamodificacion, idcat):
		try:
			sql = 'UPDATE FAC_CATEGORIA SET ESTATUSREGISTRO = %s, FECHAMODIFICACION = %s WHERE IDCATEGORIA = %s'
			vals = (estatus, fechamodificacion, idcat)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err	

	def lectura_estados(self):
		try:
			sql = 'SELECT descripcion FROM FAC_ESTADO'
			self.cursor.execute(sql)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def lectura_ciudades(self, idce):
		try:
			sql = 'SELECT descripcion FROM FAC_CIUDAD WHERE IDESTADO = %s'
			vals=(idce,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err
	def lectura_rfc(self, idce):
		try:
			sql = 'SELECT RFC FROM FAC_CLIENTE WHERE IDCLIENTE = %s'
			vals=(idce,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err
	def lectura_nombre(self, idce):
		try:
			sql = 'SELECT NOMBRE FROM FAC_CLIENTE WHERE IDCLIENTE = %s'
			vals=(idce,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def lectura_apaterno(self, idce):
		try:
			sql = 'SELECT APATERNO FROM FAC_CLIENTE WHERE IDCLIENTE = %s'
			vals=(idce,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def lectura_amaterno(self, idce):
		try:
			sql = 'SELECT AMATERNO FROM FAC_CLIENTE WHERE IDCLIENTE = %s'
			vals=(idce,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def lectura_calle(self, idce):
		try:
			sql = 'SELECT CALLE FROM FAC_CLIENTE WHERE IDCLIENTE = %s'
			vals=(idce,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def lectura_numint(self, idce):
		try:
			sql = 'SELECT NUMINT FROM FAC_CLIENTE WHERE IDCLIENTE = %s'
			vals=(idce,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def lectura_numext(self, idce):
		try:
			sql = 'SELECT NUMEXT FROM FAC_CLIENTE WHERE IDCLIENTE = %s'
			vals=(idce,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def lectura_colonia(self, idce):
		try:
			sql = 'SELECT COLONIA FROM FAC_CLIENTE WHERE IDCLIENTE = %s'
			vals=(idce,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def lectura_cp(self, idce):
		try:
			sql = 'SELECT CP FROM FAC_CLIENTE WHERE IDCLIENTE = %s'
			vals=(idce,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err
	def lectura_referencia(self, idce):
		try:
			sql = 'SELECT REFERENCIA FROM FAC_CLIENTE WHERE IDCLIENTE = %s'
			vals=(idce,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def lectura_localidad(self, idce):
		try:
			sql = 'SELECT LOCALIDAD FROM FAC_CLIENTE WHERE IDCLIENTE = %s'
			vals=(idce,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def lectura_telfijo(self, idce):
		try:
			sql = 'SELECT TELFIJO FROM FAC_CLIENTE WHERE IDCLIENTE = %s'
			vals=(idce,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def lectura_telmovil(self, idce):
		try:
			sql = 'SELECT TELMOVIL FROM FAC_CLIENTE WHERE IDCLIENTE = %s'
			vals=(idce,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def lectura_email(self, idce):
		try:
			sql = 'SELECT EMAIL FROM FAC_CLIENTE WHERE IDCLIENTE = %s'
			vals=(idce,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err


	def lectura_email2(self, idce):
		try:
			sql = 'SELECT EMAIL2 FROM FAC_CLIENTE WHERE IDCLIENTE = %s'
			vals=(idce,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err


	def lectura_clientes_rfc(self):
		try:
			sql = 'SELECT RFC FROM FAC_CLIENTE'
			self.cursor.execute(sql)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def lectura_clientes_nombre(self):
		try:
			sql = 'SELECT NOMBRE FROM FAC_CLIENTE WHERE ESTATUSREGISTRO = 0'
			self.cursor.execute(sql)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def act_mesa(self, cantidad ,estatus, fechacreacion):
		try:
			sql = 'INSERT INTO FAC_MESA (`CANTIDAD`,`ESTATUSREGISTRO`, `FECHACREACION`) VALUES (%s, %s, %s)'
			vals = (cantidad ,estatus, fechacreacion)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err	

	def add_cliente(self, idc, rfc, nombre, paterno, materno, calle, numint, numext, colonia, cp, referencia, localidad, telfijo, telmovil, email, email2, estatus, fechacreacion):
		try:
			sql = 'INSERT INTO FAC_CLIENTE (`IDCIUDAD`,`RFC`, `NOMBRE`, `APATERNO`, `AMATERNO`, `CALLE`, `NUMINT`, `NUMEXT`, `COLONIA`, `CP`, `REFERENCIA`, `LOCALIDAD`, `TELFIJO`, `TELMOVIL`, `EMAIL`, `EMAIL2`, `ESTATUSREGISTRO`, `FECHACREACION`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
			vals = (idc, rfc, nombre, paterno, materno, calle, numint, numext, colonia, cp, referencia, localidad, telfijo, telmovil, email, email2, estatus, fechacreacion)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def up_cliente(self,idcl, idc, rfc, nombre, paterno, materno, calle, numint, numext, colonia, cp, referencia, localidad, telfijo, telmovil, email, email2, estatus, fechacreacion):
		try:
			sql = 'UPDATE FAC_CLIENTE SET IDCIUDAD = %s, RFC = %s, NOMBRE = %s, APATERNO = %s, AMATERNO = %s, CALLE = %s, NUMINT = %s, NUMEXT = %s, COLONIA = %s, CP = %s, REFERENCIA= %s, LOCALIDAD = %s, TELFIJO = %s, TELMOVIL = %s, EMAIL = %s, EMAIL2 = %s, ESTATUSREGISTRO = %s, FECHAMODIFICACION = %s WHERE IDCLIENTE = %s'
			vals = (idcl, rfc, nombre, paterno, materno, calle, numint, numext, colonia, cp, referencia, localidad, telfijo, telmovil, email, email2, estatus, fechacreacion, idc)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err	
	def estatus_cli(self,estatus, fechamodificacion, idcat):
		try:
			sql = 'UPDATE FAC_CLIENTE SET ESTATUSREGISTRO = %s, FECHAMODIFICACION = %s WHERE IDCLIENTE = %s'
			vals = (estatus, fechamodificacion, idcat)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err	

	def create_mesero(self, descripcion, estatus, fechacreacion):
		try:
			sql = 'INSERT INTO FAC_MESERO (`DESCRIPCION`, `ESTATUSREGISTRO`, `FECHACREACION`) VALUES (%s, %s, %s)'
			vals = (descripcion, estatus, fechacreacion)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err	

	def edit_mesero(self,descripcion, fechamodificacion, idcat):
		try:
			sql = 'UPDATE FAC_MESERO SET DESCRIPCION = %s, FECHAMODIFICACION = %s WHERE IDMESERO = %s'
			vals = (descripcion, fechamodificacion, idcat)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err	

	def lectura_mesero(self):
		try:
			sql = 'SELECT descripcion FROM FAC_MESERO WHERE ESTATUSREGISTRO = 0'
			self.cursor.execute(sql)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def lectura_mesero_baja(self):
		try:
			sql = 'SELECT descripcion FROM FAC_MESERO '
			self.cursor.execute(sql)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def estatus_mesero(self,estatus, fechamodificacion, idcat):
		try:
			sql = 'UPDATE FAC_MESERO SET ESTATUSREGISTRO = %s, FECHAMODIFICACION = %s WHERE IDMESERO = %s'
			vals = (estatus, fechamodificacion, idcat)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err	

	def create_producto(self,idcat, descripcion, precio, iva, total, estatus, fechacreacion):
		try:
			sql = 'INSERT INTO FAC_PRODUCTO (`IDCATEGORIA`, `DESCRIPCION`, `PRECIO`, `IVA`, `TOTAL`, `ESTATUSREGISTRO`, `FECHACREACION`) VALUES (%s, %s, %s, %s, %s, %s, %s)'	
			vals = (idcat, descripcion, precio, iva, total, estatus, fechacreacion)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err	

	def lectura_producto(self):
		try:
			sql = 'SELECT DESCRIPCION FROM FAC_PRODUCTO'
			self.cursor.execute(sql)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err

	def estatus_producto(self,estatus, fechamodificacion, idcat):
		try:
			sql = 'UPDATE FAC_PRODUCTO SET ESTATUSREGISTRO = %s, FECHAMODIFICACION = %s WHERE IDPRODUCTO = %s'
			vals = (estatus, fechamodificacion, idcat)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err	