import mysql.connector

try:
    conexion=mysql.connector.connect(
        host="localhost",
        user='root',
        password="",
        database='bd_python'
    )
except:
    print("Ocurrio un error")
else:

    #crear una tabla dentro de una bd existente
    sql="create table clientes(id int primary key auto_increment, nombre varchar(60), direccion varchar (120), tel varchar (10))"

    micursor=conexion.cursor()

    micursor.execute(sql)

    
    print("Se creo la tabla con exito")