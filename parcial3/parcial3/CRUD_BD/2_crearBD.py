import mysql.connector

try:
    #Crear la conexion con la BD
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',

    )
#verificar la conexion
    if conexion.is_connected():
        print("Se creo la conexion exitosa")
    else:
        print("No fue posible conectarse")

#crear otro objeto para ejecutar las conecciones 
    micursor=conexion.cursor()

#crear la bd desde python
    sql="create database bd_python"
    micursor.execute(sql)

#verificar que se creo la BD 
    if micursor:
        print("Se creo la base de datos exitosamente")

#mostrar las bases de datos que existen en my servidor en mi MYSQL
    micursor.execute("show databases")

    for x in micursor:
        print(x)

except:
    print("Ocurrio un problema con el servidor... por favor intentalo mas tarde...")

else:
    #verificar la conexion
    if conexion.is_connected():
        print("Se creo la conexion exitosa")
    else:
        print("No fue posible conectarse")

#crear otro objeto para ejecutar las conecciones 
    micursor=conexion.cursor()

#crear la bd desde python
    sql="create database bd_python"
    micursor.execute(sql)

#verificar que se creo la BD 
    if micursor:
        print("Se creo la base de datos exitosamente")

#mostrar las bases de datos que existen en my servidor en mi MYSQL
    micursor.execute("show databases")

    for x in micursor:
        print(x)