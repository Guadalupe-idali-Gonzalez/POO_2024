from conexionBD import *

micursor=conexion.cursor()
sql="delete from clientes where id=1"

micursor.execute(sql)
conexion,commit()


except:
print (f"Ocurrio un problema con el servidor... por favor intentarlo mas tarde 
..")
else:
 print (f"Registro Actualizado Correctamente ")