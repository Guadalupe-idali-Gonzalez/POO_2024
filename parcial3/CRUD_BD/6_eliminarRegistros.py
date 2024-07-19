from conexionBD import *
try:
    micursor=conexion.cursor()
    sql="delete from clientes where id=1"

    micursor.execute(sql)
    conexion.commit()

    
except:
    print(f"Ocurrio un problema con el servidor, por favor intentalo mas tarde...")
else:

    print(f"Registros Eliminado Correctamente")