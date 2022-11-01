import pymysql

mysql = pymysql.connect(user='root',password='1234',host='localhost',database="inventario")
print("Conexion exitosa");

  


def crearTabla(mysql):
    with mysql:
        try:
            cursor=mysql.cursor(pymysql.cursors.DictCursor)
            cursor.execute("CREATE TABLE proveedores(CodProveedor INT(4) PRIMARY KEY NOT NULL, nombre varchar(60) NOT NULL, RFC varchar(20) NOT NULL, email varchar(40), telefono INT(10)NOT NULL, FechaAlta date); ")
            cursor.execute("CREATE TABLE productos(CodProducto INT(4) PRIMARY KEY NOT NULL, descripcion varchar(70) NOT NULL, Categoria varchar(20) NOT NULL,Cantidad int(5) NOT NULL, CodProveedor INT(4), FechaAlta date, FechaCaducidad date);")
            cursor.execute("CREATE TABLE entradas(IdEntrada INT(6) PRIMARY KEY NOT NULL, CodProducto INT(4) NOT NULL, cantidad INT(10) NOT NULL, FechaEntrada date);")
            cursor.execute("CREATE TABLE salidas(IdSalida INT(6) PRIMARY KEY NOT NULL, CodProducto INT(4) NOT NULL, cantidad INT(10) NOT NULL, FechaSalida date);")
            cursor.execute("ALTER TABLE productos ADD CONSTRAINT FK_PRODUCTOS FOREIGN KEY (CodProveedor) REFERENCES proveedores(CodProveedor) ON UPDATE CASCADE ON DELETE RESTRICT;")
            cursor.execute("ALTER TABLE entradas ADD CONSTRAINT FK_ENTRADAS FOREIGN KEY (CodProducto) REFERENCES productos(CodProducto) ON UPDATE CASCADE ON DELETE RESTRICT;")
            cursor.execute("ALTER TABLE salidas ADD CONSTRAINT FK_SALIDAS FOREIGN KEY (CodProducto) REFERENCES productos(CodProducto) ON UPDATE CASCADE ON DELETE RESTRICT;")
            print("La tabla ha sido creada");
        except Error as err:
            print("Something went wrong: {}".format(err))
            sys.exit(1)
            mysql.close()

   
crearTabla (mysql)
#insertarDatos(mysql)

#eliminarDatos(mysql)
#actualizaDatos(mysql)
#listarDatos(mysql)
            

