paises=["Mexico","USA","Brasil","Japon"]
numeros=[23,100,1416,0.100]
varios=["Hola",True,100,10.22]

#Ordenar lista

print(paises)
paises.sort()
print(paises)
      #Solo se puder ordenar unicamente condatos string, y unicamente con datos numericos
# print(numeros)
# paises.sort()
# print(numeros)

#Agregar elementos
print(numeros)
numeros.insert(len(numeros),100)
print(numeros)
numeros.append(100)

#Eliminar elementos
print(numeros)
numeros.pop(2)
print(numeros)
numeros.remove(100)

#Buscar en una lista un dato o valor

encontrar="Brasil" in paises
print(encontrar)

#Dar la vuelta a una lista
print(varios)
varios.reverse()
print(varios)

#Unir listas
print (paises)
paises.extend(numeros)
print(paises)

#Vaciar una lista/borrar contenido
print(varios)
varios.clear()
print(varios)
