import mysql.connector

try:
#conectarse con la base de datos de mysql
    conexion=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bd_python"
    )


except Exception as e:
    # print(f"Error: {e}")
    # print(f"Tipo de error: {type(e).__name__}")
    print(f"Ocurrio un problema con el servidor, por favor intentalo mas tarde...")
# else:

#     print("Se creo la conexion con la base de datos")
