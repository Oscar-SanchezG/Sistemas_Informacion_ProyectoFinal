#Definition of the schema fo the DB
#This is a DB for managing imformation about "cinema"

#Create the DB
DROP DATABASE IF EXISTS amigo_db;
CREATE DATABASE IF NOT EXISTS amigo_db;

#Select the database to work with
USE amigo_db;
CREATE TABLE FAC_USUARIO (	
    IDUSUARIO INT NOT NULL AUTO_INCREMENT, 
	DESCRIPCION VARCHAR(500) NOT NULL , 
	PASSWORD VARCHAR(50) NOT NULL , 
	ESTATUSREGISTRO INT NOT NULL , 
	FECHACREACION DATETIME NOT NULL , 
	FECHAMODIFICACION DATETIME, 
    CONSTRAINT FAC_USUARIO_PK PRIMARY KEY (IDUSUARIO)
)ENGINE = InnoDB;

CREATE TABLE BIT_FAC_USUARIO(	
    IDBIT_IDUSUARIO INT NOT NULL AUTO_INCREMENT,
    IDUSUARIO INT NOT NULL , 
	DESCRIPCION VARCHAR(500) NOT NULL, 
	PASSWORD VARCHAR(50) NOT NULL, 
	ESTATUSREGISTRO INT NOT NULL, 
	FECHACREACION DATETIME NOT NULL , 
	FECHAMODIFICACION DATETIME, 
    REALIZADO DATE NOT NULL,
    CONSTRAINT BIT_FAC_USUARIO_PK PRIMARY KEY (IDBIT_IDUSUARIO)
)ENGINE = InnoDB;

CREATE TABLE FAC_ESTADO(
    IDESTADO INT NOT NULL AUTO_INCREMENT,
    DESCRIPCION VARCHAR(250) NOT NULL ,
    ESTATUSREGISTRO INT NOT NULL ,
    FECHACREACION DATETIME NOT NULL ,
    FECHAMODIFICACION DATETIME,
    CONSTRAINT FAC_ESTADO_PK PRIMARY KEY (IDESTADO)
)ENGINE = InnoDB;

CREATE TABLE BIT_FAC_ESTADO(
    IDBIT_IDESTADO INT NOT NULL AUTO_INCREMENT,
    IDESTADO INT NOT NULL ,
    DESCRIPCION VARCHAR(250) NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    REALIZADO DATE NOT NULL,
    CONSTRAINT BIT_FAC_ESTADO_PK PRIMARY KEY (IDBIT_IDESTADO)
)ENGINE = InnoDB;

CREATE TABLE FAC_CIUDAD(
    IDCIUDAD INT NOT NULL AUTO_INCREMENT,
    IDESTADO INT NOT NULL ,
    DESCRIPCION VARCHAR(250) NOT NULL ,
    ESTATUSREGISTRO INT NOT NULL ,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    CONSTRAINT FAC_CIUDAD_PK PRIMARY KEY (IDCIUDAD)
)ENGINE = InnoDB;

CREATE TABLE BIT_FAC_CIUDAD(
    IDBIT_IDCIUDAD INT NOT NULL AUTO_INCREMENT,
    IDCIUDAD INT NOT NULL,
    IDESTADO INT NOT NULL,
    DESCRIPCION VARCHAR(250) NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    REALIZADO DATE NOT NULL,
    CONSTRAINT BIT_FAC_CIUDAD_PK PRIMARY KEY (IDBIT_IDCIUDAD)
)ENGINE = InnoDB;

CREATE TABLE FAC_TIPOPAGO(
    IDTIPO INT NOT NULL AUTO_INCREMENT,
    DESCRIPCION VARCHAR(250) NOT NULL,
    CLAVE VARCHAR(250) NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    CONSTRAINT FAC_TIPOPAGO_PK PRIMARY KEY (IDTIPO)
)ENGINE = InnoDB;

CREATE TABLE BIT_FAC_TIPOPAGO(
    IDBIT_IDTIPO INT NOT NULL AUTO_INCREMENT,
    IDTIPO INT NOT NULL,
    DESCRIPCION VARCHAR(250) NOT NULL,
    CLAVE VARCHAR(250) NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    REALIZADO DATE NOT NULL,
    CONSTRAINT BIT_FAC_TIPOPAGO_PK PRIMARY KEY (IDBIT_IDTIPO)
)ENGINE = InnoDB;

CREATE TABLE FAC_MESERO(
    IDMESERO INT NOT NULL AUTO_INCREMENT,
    DESCRIPCION VARCHAR(250) NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    CONSTRAINT FAC_MESERO_PK PRIMARY KEY (IDMESERO)
)ENGINE = InnoDB;

CREATE TABLE BIT_FAC_MESERO(
    IDBIT_IDMESERO INT NOT NULL AUTO_INCREMENT,
    IDMESERO INT NOT NULL,
    DESCRIPCION VARCHAR(250) NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    REALIZADO DATE NOT NULL,
    CONSTRAINT BIT_FAC_MESERO_PK PRIMARY KEY (IDBIT_IDMESERO)
)ENGINE = InnoDB;

CREATE TABLE FAC_CATEGORIA(
    IDCATEGORIA INT NOT NULL AUTO_INCREMENT,
    DESCRIPCION VARCHAR(250) NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    CONSTRAINT FAC_CATEGORIA_PK PRIMARY KEY (IDCATEGORIA)
)ENGINE = InnoDB;

CREATE TABLE BIT_FAC_CATEGORIA(
    IDBIT_IDCATEGORIA INT NOT NULL AUTO_INCREMENT,
    IDCATEGORIA INT NOT NULL,
    DESCRIPCION VARCHAR(250) NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    REALIZADO DATE NOT NULL,
    CONSTRAINT BIT_FAC_CATEGORIA_PK PRIMARY KEY (IDBIT_IDCATEGORIA)
)ENGINE = InnoDB;

CREATE TABLE FAC_PRODUCTO(
    IDPRODUCTO INT NOT NULL AUTO_INCREMENT,
    IDCATEGORIA INT NOT NULL,
    DESCRIPCION VARCHAR(250) NOT NULL,
    PRECIO INT NOT NULL,
    IVA INT NOT NULL,
    TOTAL INT NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    CONSTRAINT FAC_PRODUCTO_PK PRIMARY KEY (IDPRODUCTO)
)ENGINE = InnoDB;

CREATE TABLE BIT_FAC_PRODUCTO(
    IDBIT_IDPRODUCTO INT NOT NULL AUTO_INCREMENT,
    IDPRODUCTO INT NOT NULL,
    IDCATEGORIA INT NOT NULL,
    DESCRIPCION VARCHAR(250) NOT NULL,
    PRECIO INT NOT NULL,
    IVA INT NOT NULL,
    TOTAL INT NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    REALIZADO DATE NOT NULL,
    CONSTRAINT BIT_FAC_PRODUCTO_PK PRIMARY KEY (IDBIT_IDPRODUCTO)
)ENGINE = InnoDB;

CREATE TABLE FAC_CLIENTE(
    IDCLIENTE INT NOT NULL AUTO_INCREMENT,
    IDCIUDAD INT NOT NULL,
    RFC VARCHAR(13) NOT NULL,
    NOMBRE VARCHAR(500) NOT NULL,
    APATERNO VARCHAR(500),
    AMATERNO VARCHAR(500),
    CALLE VARCHAR(500),
    NUMINT VARCHAR(50),
    NUMEXT VARCHAR(50),
    COLONIA VARCHAR(500),
    CP VARCHAR(20),
    REFERENCIA VARCHAR(500),
    LOCALIDAD VARCHAR(500),
    TELFIJO VARCHAR(50),
    TELMOVIL VARCHAR(50),
    EMAIL VARCHAR(250),
    EMAIL2 VARCHAR(250),
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    CONSTRAINT FAC_CLIENTE_PK PRIMARY KEY (IDCLIENTE)
)ENGINE = InnoDB;

CREATE TABLE BIT_FAC_CLIENTE(
    IDBIT_IDCLIENTE INT NOT NULL AUTO_INCREMENT,
    IDCLIENTE INT NOT NULL,
    IDCIUDAD INT NOT NULL,
    RFC VARCHAR(13) NOT NULL,
    NOMBRE VARCHAR(500) NOT NULL,
    APATERNO VARCHAR(500),
    AMATERNO VARCHAR(500),
    CALLE VARCHAR(500),
    NUMINT VARCHAR(50),
    NUMEXT VARCHAR(50),
    COLONIA VARCHAR(500),
    CP VARCHAR(20),
    REFERENCIA VARCHAR(500),
    LOCALIDAD VARCHAR(500),
    TELFIJO VARCHAR(50),
    TELMOVIL VARCHAR(50),
    EMAIL VARCHAR(250),
    EMAIL2 VARCHAR(250),
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    REALIZADO DATE NOT NULL,
    CONSTRAINT BIT_FAC_CLIENTE_PK PRIMARY KEY (IDBIT_IDCLIENTE)
)ENGINE = InnoDB;

CREATE TABLE FAC_NOTA(
    IDNOTA INT NOT NULL AUTO_INCREMENT,
    IDTIPO INT NOT NULL,
    IDMESERO INT NOT NULL,
    FOLIO INT NOT NULL,
    MESA INT NOT NULL,
    TOTAL INT NOT NULL,
    FECHA DATE NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATE NOT NULL,
    FECHAMODIFICACION DATETIME,
    CONSTRAINT FAC_NOTA_PK PRIMARY KEY (IDNOTA)
)
ENGINE = InnoDB;
CREATE TABLE BIT_FAC_NOTA(
    IDBIT_IDNOTA INT NOT NULL AUTO_INCREMENT,
    IDNOTA INT NOT NULL,
    IDTIPO INT NOT NULL,
    IDMESERO INT NOT NULL,
    FOLIO INT NOT NULL,
    MESA INT NOT NULL,
    TOTAL INT NOT NULL,
    FECHA DATE NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATE NOT NULL ,
    FECHAMODIFICACION DATETIME,
    REALIZADO DATE NOT NULL,
    CONSTRAINT BIT_FAC_NOTA_PK PRIMARY KEY (IDBIT_IDNOTA)
)ENGINE = InnoDB;

CREATE TABLE FAC_DETALLE(
    IDDETALLE INT NOT NULL AUTO_INCREMENT,
    IDNOTA INT NOT NULL,
    IDPRODUCTO INT NOT NULL,
    CANTIDAD INT NOT NULL,
    TOTAL INT NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATE NOT NULL,
    FECHAMODIFICACION DATETIME,
    CONSTRAINT FAC_DETALLE_PK PRIMARY KEY (IDDETALLE)
)ENGINE = InnoDB;

CREATE TABLE BIT_FAC_DETALLE(
    IDBIT_IDDETALLE INT NOT NULL AUTO_INCREMENT,
    IDDETALLE INT NOT NULL,
    IDNOTA INT NOT NULL,
    IDPRODUCTO INT NOT NULL,
    CANTIDAD INT NOT NULL,
    TOTAL INT NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATE NOT NULL,
    FECHAMODIFICACION DATETIME,
    REALIZADO DATE NOT NULL,
    CONSTRAINT BIT_FAC_DETALLE_PK PRIMARY KEY (IDBIT_IDDETALLE)
)ENGINE = InnoDB;

CREATE TABLE FAC_FACTURAV1(
    IDFACTURA INT NOT NULL AUTO_INCREMENT,
    IDTIPO INT,
    RFC VARCHAR(20),
    SUBTOTAL INT,
    IVA INT,
    TOTAL INT,
    FECHA DATE,
    LETRA VARCHAR(250),
    DETALLE VARCHAR(250),
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATE NOT NULL,
    FECHAMODIFICACION DATETIME,
    CONSTRAINT FAC_FACTURAV1_PK PRIMARY KEY (IDFACTURA)
)ENGINE = InnoDB;

CREATE TABLE FAC_FACTURAV2(
    IDFACTURA INT NOT NULL AUTO_INCREMENT,
    IDTIPO INT,
    RFC VARCHAR(20),
    FOLIO INT,
    SERIE VARCHAR(5),
    SUBTOTAL INT,
    IVA INT,
    TOTAL INT,
    FECHA DATE,
    DETALLE VARCHAR(250),
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATE NOT NULL,
    FECHAMODIFICACION DATETIME,
    CONSTRAINT FAC_FACTURAV2_PK PRIMARY KEY (IDFACTURA)
)ENGINE = InnoDB;

CREATE TABLE FAC_FACTURA(
    IDFACTURA INT NOT NULL AUTO_INCREMENT,
    EMISOR VARCHAR(750),
    RFCEMISOR VARCHAR(13),
    CLIENTE VARCHAR(1500),
    RFCCLIENTE VARCHAR(13),
    SERIE VARCHAR(15),
    FOLIO INT,
    CLAPAGO VARCHAR(15),
    DESCLAPAGO VARCHAR(250),
    CLATIPCOM VARCHAR(15),
    DESCLATIPCOM VARCHAR(250),
    CLAMON VARCHAR(15),
    DESCLAMON VARCHAR(250),
    CLAMETPAG VARCHAR(15),
    DESCLAMETPAG VARCHAR(250),
    LUGEXP VARCHAR(15),
    CLAREG VARCHAR(15),
    DESCLAREG VARCHAR(250),
    CLAUSO VARCHAR(15),
    DESCLAUSO VARCHAR(250),
    CLAPRO VARCHAR(15),
    DESCLAPRO VARCHAR(250),
    CLAUNI VARCHAR(15),
    DESCLAUNI VARCHAR(250),
    CLAIMP VARCHAR(15),
    DESCLAIMP VARCHAR(250),
    NOIDEN VARCHAR(250),
    TIPFAC VARCHAR(250),
    VALTAS VARCHAR(250),
    DESCRIPCION VARCHAR(4000),
    LETRA VARCHAR(4000),
    CANTIDAD INT,
    TOTAL INT,
    SUBTOTAL INT,
    IMPUESTOS INT,
    VALOR INT,
    IMPORTE INT,
    BASE INT,
    IMPIMP INT,
    FECHA DATE,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATE NOT NULL,
    FECHAMODIFICACION DATETIME,
    CONSTRAINT FAC_FACTURA_PK PRIMARY KEY (IDFACTURA)
)ENGINE = InnoDB;

CREATE TABLE BIT_FAC_FACTURA(
    IDBIT_IDFACTURA INT NOT NULL AUTO_INCREMENT,
    IDFACTURA INT NOT NULL,
    EMISOR VARCHAR(750),
    RFCEMISOR VARCHAR(13),
    CLIENTE VARCHAR(1500),
    RFCCLIENTE VARCHAR(13),
    SERIE VARCHAR(15),
    FOLIO INT,
    CLAPAGO VARCHAR(15),
    DESCLAPAGO VARCHAR(250),
    CLATIPCOM VARCHAR(15),
    DESCLATIPCOM VARCHAR(250),
    CLAMON VARCHAR(15),
    DESCLAMON VARCHAR(250),
    CLAMETPAG VARCHAR(15),
    DESCLAMETPAG VARCHAR(250),
    LUGEXP VARCHAR(15),
    CLAREG VARCHAR(15),
    DESCLAREG VARCHAR(250),
    CLAUSO VARCHAR(15),
    DESCLAUSO VARCHAR(250),
    CLAPRO VARCHAR(15),
    DESCLAPRO VARCHAR(250),
    CLAUNI VARCHAR(15),
    DESCLAUNI VARCHAR(250),
    CLAIMP VARCHAR(15),
    DESCLAIMP VARCHAR(250),
    NOIDEN VARCHAR(250),
    TIPFAC VARCHAR(250),
    VALTAS VARCHAR(250),
    DESCRIPCION VARCHAR(4000),
    LETRA VARCHAR(4000),
    CANTIDAD INT,
    TOTAL INT,
    SUBTOTAL INT,
    IMPUESTOS INT,
    VALOR INT,
    IMPORTE INT,
    BASE INT,
    IMPIMP INT,
    FECHA DATE,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATE NOT NULL,
    FECHAMODIFICACION DATETIME,
    REALIZADO DATE NOT NULL,
    CONSTRAINT BIT_FAC_FACTURA_PK PRIMARY KEY (IDBIT_IDFACTURA)
)ENGINE = InnoDB;

CREATE TABLE FAC_MESA(
    IDMESA INT NOT NULL AUTO_INCREMENT,
    CANTIDAD INT NOT NULL ,
    ESTATUSREGISTRO INT NOT NULL ,
    FECHACREACION DATETIME NOT NULL ,
    FECHAMODIFICACION DATETIME,
    CONSTRAINT FAC_MESA_PK PRIMARY KEY (IDMESA)
)ENGINE = InnoDB;

CREATE TABLE BIT_FAC_MESA(
    IDBIT_IDMESA INT NOT NULL AUTO_INCREMENT,
    IDMESA INT NOT NULL ,
    CANTIDAD INT NOT NULL ,
    ESTATUSREGISTRO INT NOT NULL ,
    FECHACREACION DATETIME NOT NULL ,
    FECHAMODIFICACION DATETIME,
    REALIZADO DATE NOT NULL ,
    CONSTRAINT BIT_FAC_MESA_PK PRIMARY KEY (IDBIT_IDMESA)
)ENGINE = InnoDB;

CREATE TABLE FAC_LICENCIAXML(
    IDLICENCIA INT NOT NULL AUTO_INCREMENT,
    DESCRIPCION VARCHAR(250) NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    CONSTRAINT FAC_LICENCIAXML_PK PRIMARY KEY (IDLICENCIA)
)ENGINE = InnoDB;

CREATE TABLE BIT_FAC_LICENCIAXML(
    IDBIT_IDLICENCIA INT NOT NULL AUTO_INCREMENT,
    IDLICENCIA INT NOT NULL ,
    DESCRIPCION VARCHAR(250) NOT NULL ,
    ESTATUSREGISTRO INT NOT NULL ,
    FECHACREACION DATETIME NOT NULL ,
    FECHAMODIFICACION DATETIME,
    REALIZADO DATE NOT NULL ,
    CONSTRAINT BIT_FAC_LICENCIAXML_PK PRIMARY KEY (IDBIT_IDLICENCIA)
)ENGINE = InnoDB;

CREATE TABLE FAC_LICENCIACDFI(
    IDLICENCIA INT NOT NULL AUTO_INCREMENT,
    DESCRIPCION VARCHAR(250) NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    CONSTRAINT FAC_LICENCIACDFI_PK PRIMARY KEY (IDLICENCIA)
)ENGINE = InnoDB;

CREATE TABLE BIT_FAC_LICENCIACDFI(
    IDBIT_IDLICENCIA INT NOT NULL AUTO_INCREMENT,
    IDLICENCIA INT NOT NULL,
    DESCRIPCION VARCHAR(250) NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    REALIZADO DATE NOT NULL,
    CONSTRAINT BIT_FAC_LICENCIACDFI_PK PRIMARY KEY (IDBIT_IDLICENCIA)
)ENGINE = InnoDB;

CREATE TABLE FAC_TIMBRE(
    IDTIMBRE INT NOT NULL AUTO_INCREMENT,
    TIMBRE VARCHAR(250) NOT NULL,
    CLAVE VARCHAR(250) NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    CONSTRAINT FAC_TIMBRE_PK PRIMARY KEY (IDTIMBRE)
)ENGINE = InnoDB;

CREATE TABLE BIT_FAC_TIMBRE(
    IDBIT_IDTIMBRE INT NOT NULL AUTO_INCREMENT,
    IDTIMBRE INT NOT NULL,
    TIMBRE VARCHAR(250) NOT NULL,
    CLAVE VARCHAR(250) NOT NULL,
    ESTATUSREGISTRO INT NOT NULL,
    FECHACREACION DATETIME NOT NULL,
    FECHAMODIFICACION DATETIME,
    REALIZADO DATE NOT NULL,
    CONSTRAINT BIT_FAC_TIMBRE_PK PRIMARY KEY (IDBIT_IDTIMBRE)
)ENGINE = InnoDB;

#CREAMOS EL TRIGGER DE LA BITACORA

CREATE TRIGGER TRI_BIT_FAC_USUARIO BEFORE INSERT ON FAC_USUARIO
	FOR EACH ROW 
	INSERT INTO BIT_FAC_USUARIO (IDUSUARIO, DESCRIPCION, PASSWORD, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO) 
    VALUES (NEW.IDUSUARIO, NEW.DESCRIPCION, NEW.PASSWORD, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());
		
CREATE TRIGGER TRI_BIT_FAC_USUARIO_UP BEFORE UPDATE ON FAC_USUARIO
	FOR EACH ROW 
    INSERT INTO BIT_FAC_USUARIO (IDUSUARIO, DESCRIPCION, PASSWORD, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO)
    VALUES (NEW.IDUSUARIO, NEW.DESCRIPCION, NEW.PASSWORD, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_ESTADO BEFORE INSERT ON FAC_ESTADO
	FOR EACH ROW
    INSERT INTO BIT_FAC_ESTADO (IDESTADO, DESCRIPCION, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO) 
    VALUES (NEW.IDESTADO, NEW.DESCRIPCION, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_ESTADO_UP BEFORE UPDATE ON FAC_ESTADO
	FOR EACH ROW
    INSERT INTO BIT_FAC_ESTADO (IDESTADO, DESCRIPCION, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO) 
    VALUES (NEW.IDESTADO, NEW.DESCRIPCION, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());
    

CREATE TRIGGER TRI_BIT_FAC_CIUDAD BEFORE INSERT ON FAC_CIUDAD
	FOR EACH ROW
    INSERT INTO BIT_FAC_CIUDAD (IDCIUDAD, IDESTADO, DESCRIPCION, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO)
    VALUES (NEW.IDCIUDAD, NEW.IDESTADO, NEW.DESCRIPCION, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_CIUDAD_UP BEFORE UPDATE ON FAC_CIUDAD
	FOR EACH ROW
    INSERT INTO BIT_FAC_CIUDAD (IDCIUDAD, IDESTADO, DESCRIPCION, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO)
    VALUES (NEW.IDCIUDAD, NEW.IDESTADO, NEW.DESCRIPCION, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());


CREATE TRIGGER TRI_BIT_FAC_TIPOPAGO BEFORE INSERT ON FAC_TIPOPAGO
	FOR EACH ROW
    INSERT INTO BIT_FAC_TIPOPAGO (IDTIPO, DESCRIPCION, CLAVE, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO) 
    VALUES (NEW.IDTIPO, NEW.DESCRIPCION, NEW.CLAVE, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_TIPOPAGO_UP BEFORE UPDATE ON FAC_TIPOPAGO
	FOR EACH ROW
    INSERT INTO BIT_FAC_TIPOPAGO (IDTIPO, DESCRIPCION, CLAVE, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO) 
    VALUES (NEW.IDTIPO, NEW.DESCRIPCION, NEW.CLAVE, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());


CREATE TRIGGER TRI_BIT_FAC_MESERO BEFORE INSERT ON FAC_MESERO
FOR EACH ROW
    INSERT INTO BIT_FAC_MESERO (IDMESERO, DESCRIPCION, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO) 
    VALUES(NEW.IDMESERO, NEW.DESCRIPCION, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_MESERO_UP BEFORE UPDATE ON FAC_MESERO
FOR EACH ROW
    INSERT INTO BIT_FAC_MESERO (IDMESERO, DESCRIPCION, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO) 
    VALUES(NEW.IDMESERO, NEW.DESCRIPCION, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());


CREATE TRIGGER TRI_BIT_FAC_CATEGORIA BEFORE INSERT ON FAC_CATEGORIA
FOR EACH ROW
    INSERT INTO BIT_FAC_CATEGORIA (IDCATEGORIA, DESCRIPCION, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO) 
    VALUES (NEW.IDCATEGORIA, NEW.DESCRIPCION, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_CATEGORIA_UP BEFORE UPDATE ON FAC_CATEGORIA
FOR EACH ROW
    INSERT INTO BIT_FAC_CATEGORIA (IDCATEGORIA, DESCRIPCION, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO) 
    VALUES (NEW.IDCATEGORIA, NEW.DESCRIPCION, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());


CREATE TRIGGER TRI_BIT_FAC_PRODUCTO BEFORE INSERT ON FAC_PRODUCTO
FOR EACH ROW
    INSERT INTO BIT_FAC_PRODUCTO (IDPRODUCTO, IDCATEGORIA, DESCRIPCION, PRECIO, IVA, TOTAL, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO) 
    VALUES (NEW.IDPRODUCTO, NEW.IDCATEGORIA, NEW.DESCRIPCION, NEW.PRECIO, NEW.IVA, NEW.TOTAL, NEW.ESTATUSREGISTRO, 
    NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_PRODUCTO_UP BEFORE UPDATE ON FAC_PRODUCTO
FOR EACH ROW
    INSERT INTO BIT_FAC_PRODUCTO (IDPRODUCTO, IDCATEGORIA, DESCRIPCION, PRECIO, IVA, TOTAL, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO) 
    VALUES (NEW.IDPRODUCTO, NEW.IDCATEGORIA, NEW.DESCRIPCION, NEW.PRECIO, NEW.IVA, NEW.TOTAL, NEW.ESTATUSREGISTRO, 
    NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());


CREATE TRIGGER TRI_BIT_FAC_CLIENTE BEFORE INSERT ON FAC_CLIENTE
FOR EACH ROW
    INSERT INTO BIT_FAC_CLIENTE (IDCLIENTE, IDCIUDAD, RFC, NOMBRE, APATERNO, AMATERNO, CALLE, NUMINT, NUMEXT, COLONIA, CP, REFERENCIA,
    LOCALIDAD, TELFIJO, TELMOVIL, EMAIL, EMAIL2, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO) 
    VALUES (NEW.IDCLIENTE, NEW.IDCIUDAD, NEW.RFC, NEW.NOMBRE, NEW.APATERNO, NEW.AMATERNO, NEW.CALLE, NEW.NUMINT, NEW.NUMEXT,
    NEW.COLONIA, NEW.CP, NEW.REFERENCIA, NEW.LOCALIDAD, NEW.TELFIJO, NEW.TELMOVIL, NEW.EMAIL, NEW.EMAIL2, NEW.ESTATUSREGISTRO, NEW.FECHACREACION,
    NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_CLIENTE_UP BEFORE UPDATE ON FAC_CLIENTE
FOR EACH ROW
    INSERT INTO BIT_FAC_CLIENTE (IDCLIENTE, IDCIUDAD, RFC, NOMBRE, APATERNO, AMATERNO, CALLE, NUMINT, NUMEXT, COLONIA, CP, REFERENCIA,
    LOCALIDAD, TELFIJO, TELMOVIL, EMAIL, EMAIL2, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO) 
    VALUES (NEW.IDCLIENTE, NEW.IDCIUDAD, NEW.RFC, NEW.NOMBRE, NEW.APATERNO, NEW.AMATERNO, NEW.CALLE, NEW.NUMINT, NEW.NUMEXT,
    NEW.COLONIA, NEW.CP, NEW.REFERENCIA, NEW.LOCALIDAD, NEW.TELFIJO, NEW.TELMOVIL, NEW.EMAIL, NEW.EMAIL2, NEW.ESTATUSREGISTRO, NEW.FECHACREACION,
    NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_NOTA BEFORE INSERT ON FAC_NOTA
FOR EACH ROW
    INSERT INTO BIT_FAC_NOTA (IDNOTA, IDTIPO, IDMESERO, FOLIO, MESA, TOTAL, FECHA, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO)
    VALUES (NEW.IDNOTA, NEW.IDTIPO, NEW.IDMESERO, NEW.FOLIO, NEW.MESA, NEW.TOTAL, NEW.FECHA, NEW.ESTATUSREGISTRO, 
    NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_NOTA_UP BEFORE UPDATE ON FAC_NOTA
FOR EACH ROW
    INSERT INTO BIT_FAC_NOTA (IDNOTA, IDTIPO, IDMESERO, FOLIO, MESA, TOTAL, FECHA, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO)
    VALUES (NEW.IDNOTA, NEW.IDTIPO, NEW.IDMESERO, NEW.FOLIO, NEW.MESA, NEW.TOTAL, NEW.FECHA, NEW.ESTATUSREGISTRO, 
    NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_DETALLE BEFORE INSERT ON FAC_DETALLE
FOR EACH ROW
    INSERT INTO BIT_FAC_DETALLE (IDDETALLE, IDNOTA, IDPRODUCTO, CANTIDAD, TOTAL, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO)
    VALUES (NEW.IDDETALLE, NEW.IDNOTA, NEW.IDPRODUCTO, NEW.CANTIDAD, NEW.TOTAL, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, 
    NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_DETALLE_UP BEFORE UPDATE ON FAC_DETALLE
FOR EACH ROW
    INSERT INTO BIT_FAC_DETALLE (IDDETALLE, IDNOTA, IDPRODUCTO, CANTIDAD, TOTAL, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO)
    VALUES (NEW.IDDETALLE, NEW.IDNOTA, NEW.IDPRODUCTO, NEW.CANTIDAD, NEW.TOTAL, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, 
    NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_FACTURA BEFORE INSERT ON FAC_FACTURA
FOR EACH ROW
    INSERT INTO BIT_FAC_FACTURA (IDFACTURA, EMISOR, RFCEMISOR, CLIENTE, RFCCLIENTE, SERIE, FOLIO, CLAPAGO, 
    DESCLAPAGO, CLATIPCOM, DESCLATIPCOM, CLAMON, DESCLAMON, CLAMETPAG, DESCLAMETPAG, LUGEXP, CLAREG, DESCLAREG, 
    CLAUSO, DESCLAUSO, CLAPRO, DESCLAPRO, CLAUNI, DESCLAUNI, CLAIMP, DESCLAIMP, NOIDEN,
    TIPFAC, VALTAS, DESCRIPCION, LETRA, CANTIDAD, TOTAL, SUBTOTAL, IMPUESTOS, VALOR,
    IMPORTE, BASE, IMPIMP, FECHA, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO) 
    VALUES (NEW.IDFACTURA, NEW.EMISOR, NEW.RFCEMISOR, NEW.CLIENTE, NEW.RFCCLIENTE, NEW.SERIE, NEW.FOLIO, NEW.CLAPAGO,
    NEW.DESCLAPAGO, NEW.CLATIPCOM, NEW.DESCLATIPCOM, NEW.CLAMON, NEW.DESCLAMON, NEW.CLAMETPAG, NEW.DESCLAMETPAG, NEW.LUGEXP, NEW.CLAREG, NEW.DESCLAREG,
    NEW.CLAUSO, NEW.DESCLAUSO, NEW.CLAPRO, NEW.DESCLAPRO, NEW.CLAUNI, NEW.DESCLAUNI, NEW.CLAIMP, NEW.DESCLAIMP, NEW.NOIDEN,
    NEW.TIPFAC, NEW.VALTAS, NEW.DESCRIPCION, NEW.LETRA, NEW.CANTIDAD, NEW.TOTAL, NEW.SUBTOTAL, NEW.IMPUESTOS, NEW.VALOR,
    NEW.IMPORTE, NEW.BASE, NEW.IMPIMP, NEW.FECHA, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_FACTURA_UP BEFORE UPDATE ON FAC_FACTURA
FOR EACH ROW
    INSERT INTO BIT_FAC_FACTURA (IDFACTURA, EMISOR, RFCEMISOR, CLIENTE, RFCCLIENTE, SERIE, FOLIO, CLAPAGO, 
    DESCLAPAGO, CLATIPCOM, DESCLATIPCOM, CLAMON, DESCLAMON, CLAMETPAG, DESCLAMETPAG, LUGEXP, CLAREG, DESCLAREG, 
    CLAUSO, DESCLAUSO, CLAPRO, DESCLAPRO, CLAUNI, DESCLAUNI, CLAIMP, DESCLAIMP, NOIDEN,
    TIPFAC, VALTAS, DESCRIPCION, LETRA, CANTIDAD, TOTAL, SUBTOTAL, IMPUESTOS, VALOR,
    IMPORTE, BASE, IMPIMP, FECHA, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO) 
    VALUES (NEW.IDFACTURA, NEW.EMISOR, NEW.RFCEMISOR, NEW.CLIENTE, NEW.RFCCLIENTE, NEW.SERIE, NEW.FOLIO, NEW.CLAPAGO,
    NEW.DESCLAPAGO, NEW.CLATIPCOM, NEW.DESCLATIPCOM, NEW.CLAMON, NEW.DESCLAMON, NEW.CLAMETPAG, NEW.DESCLAMETPAG, NEW.LUGEXP, NEW.CLAREG, NEW.DESCLAREG,
    NEW.CLAUSO, NEW.DESCLAUSO, NEW.CLAPRO, NEW.DESCLAPRO, NEW.CLAUNI, NEW.DESCLAUNI, NEW.CLAIMP, NEW.DESCLAIMP, NEW.NOIDEN,
    NEW.TIPFAC, NEW.VALTAS, NEW.DESCRIPCION, NEW.LETRA, NEW.CANTIDAD, NEW.TOTAL, NEW.SUBTOTAL, NEW.IMPUESTOS, NEW.VALOR,
    NEW.IMPORTE, NEW.BASE, NEW.IMPIMP, NEW.FECHA, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());


CREATE TRIGGER TRI_BIT_FAC_MESA BEFORE INSERT ON FAC_MESA
FOR EACH ROW
    INSERT INTO BIT_FAC_MESA (IDMESA, CANTIDAD, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO)
    VALUES (NEW.IDMESA, NEW.CANTIDAD, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, sysdate());

CREATE TRIGGER TRI_BIT_FAC_MESA_UP BEFORE UPDATE ON FAC_MESA
FOR EACH ROW
    INSERT INTO BIT_FAC_MESA (IDMESA, CANTIDAD, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO)
    VALUES (NEW.IDMESA, NEW.CANTIDAD, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());


CREATE TRIGGER TRI_DELETE_FAC_NOTA BEFORE DELETE ON FAC_NOTA
FOR EACH ROW
    DELETE FROM FAC_DETALLE WHERE IDNOTA = OLD.IDNOTA;

CREATE TRIGGER TRI_BIT_FAC_LICENCIAXML BEFORE INSERT ON FAC_LICENCIAXML
FOR EACH ROW
    INSERT INTO BIT_FAC_LICENCIAXML (IDLICENCIA, DESCRIPCION, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO)
    VALUES (NEW.IDLICENCIA, NEW.DESCRIPCION, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_LICENCIAXML_UP BEFORE UPDATE ON FAC_LICENCIAXML
FOR EACH ROW
    INSERT INTO BIT_FAC_LICENCIAXML (IDLICENCIA, DESCRIPCION, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO)
    VALUES (NEW.IDLICENCIA, NEW.DESCRIPCION, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());


CREATE TRIGGER TRI_BIT_FAC_LICENCIACDFI BEFORE INSERT ON FAC_LICENCIACDFI
FOR EACH ROW
    INSERT INTO BIT_FAC_LICENCIACDFI (IDLICENCIA, DESCRIPCION, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO)
    VALUES (NEW.IDLICENCIA, NEW.DESCRIPCION, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_LICENCIACDFI_UP BEFORE UPDATE ON FAC_LICENCIACDFI
FOR EACH ROW
    INSERT INTO BIT_FAC_LICENCIACDFI (IDLICENCIA, DESCRIPCION, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO)
    VALUES (NEW.IDLICENCIA, NEW.DESCRIPCION, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());


CREATE TRIGGER TRI_BIT_FAC_TIMBRE BEFORE INSERT ON FAC_TIMBRE
FOR EACH ROW
    INSERT INTO BIT_FAC_TIMBRE (IDTIMBRE, TIMBRE, CLAVE, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO)
    VALUES (NEW.IDTIMBRE, NEW.TIMBRE, NEW.CLAVE, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());

CREATE TRIGGER TRI_BIT_FAC_TIMBRE_UP BEFORE UPDATE ON FAC_TIMBRE
FOR EACH ROW
    INSERT INTO BIT_FAC_TIMBRE (IDTIMBRE, TIMBRE, CLAVE, ESTATUSREGISTRO, FECHACREACION, FECHAMODIFICACION, REALIZADO)
    VALUES (NEW.IDTIMBRE, NEW.TIMBRE, NEW.CLAVE, NEW.ESTATUSREGISTRO, NEW.FECHACREACION, NEW.FECHAMODIFICACION, SYSDATE());


#INSERTAR EL NUMERO DE MESAS DISPONIBLES
INSERT INTO FAC_MESA (CANTIDAD, ESTATUSREGISTRO, FECHACREACION) VALUES (50, 0, sysdate());

#INSERTAMOS LA LICENCIA DE ARCHIVOS XML
INSERT INTO FAC_LICENCIAXML (DESCRIPCION, ESTATUSREGISTRO, FECHACREACION) VALUES ('uRmWcOE93pzOu9TiVMMGpNC6uJlGlRzTuqa/ANAEGtu03+D2n+/ks0oGpIMuPE9N', 0, sysdate());

#INSERTAMOS LA LICENCIA DE ARCHIVOS CDFI
INSERT INTO FAC_LICENCIACDFI (DESCRIPCION, ESTATUSREGISTRO, FECHACREACION) VALUES ('uRmWcOE93pzOu9TiVMMGpNC6uJlGlRzTuqa/ANAEGtsC32yMyqFTcoNnKU0IrOt8', 0, sysdate());

#INSERTAMOS LAS CLAVES DE TIMBRADO DE PRODUCCION
INSERT INTO FAC_TIMBRE (TIMBRE, CLAVE, ESTATUSREGISTRO, FECHACREACION) VALUES ('2tRmp8SLzV', 'tagcode', 0, SYSDATE());



