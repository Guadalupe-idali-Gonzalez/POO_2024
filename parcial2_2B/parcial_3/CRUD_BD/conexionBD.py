import mysql.connector

#conectar con la BD MySQL
conexion=mysql.connector.connect(
    host="localhost",
    user="miguel",
    password="1234",
    database="bd_python"
)

#verificar la conexion a la BD
if conexion.is_connected():
    print(f"se creo la conexion con la BD exitosamente")
else:
    print(f"No fue posible conectar con la BD")
