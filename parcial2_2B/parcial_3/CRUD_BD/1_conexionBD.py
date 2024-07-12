import mysql.connector

#conectar con la BD MySQL
conexion=mysql.connector.connect(
    host="localhost",
    user="miguel",
    password="",
    database="bd_python"
)


except Exception as e:
    print(f"Error:{e}")
    print (f"ocurrio un problema con el servidor por favor intentalo mas tarde ")
else: 
    print ("se creo la conexion con la BD exitosamente ")

#verificar la conexion a la BD
if conexion.is_connected():
    print(f"se creo la conexion con la BD exitosamente")
else:
    print(f"No fue posible conectar con la BD")