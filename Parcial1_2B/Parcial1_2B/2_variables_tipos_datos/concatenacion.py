#Formas de concatenar en python

nombre="Edgar Reta"
especialidad="Area de SW Multiplataforma"
carrera="Ingenieria en Gestion y Desarrollo de SW"

#1er forma
print("Mi nombre es: "+nombre+ " estoy en especialidad de: "+especialidad+ " y estudio la carrear de: "+carrera+" :D" )
print("\n")

#2da forma
print("Mi nombre es: ",nombre, " estoy en especialidad de: ",especialidad, " y estudio la carrear de: ",carrera," :D" )
print("\n")

#3ra forma Mas Comun
print(f"Mi nombre es: {nombre}  estoy en especialidad de: {especialidad}  y estudio la carrear de: {carrera}" )
print("\n")

#4ta forma
print("Mi nombre es: ,{}, estoy en especialidad de: ,{}, y estudio la carrear de: ,{},".format(nombre,especialidad,carrera) )
print("\n")

#5ta forma
print('Mi nombre es: '+nombre+ ' estoy en especialidad de:'+especialidad+ ' y estudio la carrear de: '+carrera+' :D' )
print("\n")
