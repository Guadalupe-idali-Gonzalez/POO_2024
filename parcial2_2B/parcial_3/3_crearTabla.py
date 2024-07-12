import mysql.connector 

conexion=mysql.connector.connect(
    host='localhost'
    user=='root'




if conexion.is_connected():
    print("se conecto con la BD ")

#crear una tabla dentro de una BD existente
sql="create table clientes (id int primary kry auto_increment,nombre varchar(60), direccion varchar(120))"