paises=["Mexico", "USA", "Brasil","Japon"]
numeros=[23,100,3.1416,0.100]
varios=["Hola", True, 100, 10.22] #Matices, por que se combinan tipos de datos 

#-----------------------------------------------------------------------------------------------------------------
#Ordenar nuestra lista

print(paises)
paises.sort() #Ordena alfabeticamente, unicamente con puros string o numeros, no con varios
print(paises)

# print(numeros)
# numeros.sort()
# print(numeros)

#------------------------------------------------------------------------------------------------------------------
#Como agregar Elementos 
print(numeros)
numeros.insert(len(numeros),100)#Solicita el lugar y coloca el valor, no tan recomendable si no sabes lla cantidad de tu lista
print(numeros)
numeros.append(100)#Unicamente pide el valor

#-----------------------------------------------------------------------------------------------------------------
#Como Eliminar Elementos 
print(numeros)
numeros.pop(2)#Tengo que espesificar para eliminar, unicamente se puede valor entero
print(numeros)
numeros.remove(100)#Unicamente borra la cantidad exacta que elimina 

#----------------------------------------------------------------------------------------------------------------------
#Buscar dentro de una lista un dato o un valor
encontrar="Brasil" in paises#Solo sirve para encontrar la palabra mas no la posicion, da true or false
print(encontrar)

#Dar Vuelta
print(varios)
varios.reverse()
print(varios)

#-------------------------------------------------------------------------------------------------------------------------
#Concatenar a una lista el contenido de otra, UNIR LISTAS
print(paises)
paises.extend(numeros)
print(paises)

#vaciar contenido de una lista
print(varios)
varios.clear()
print(varios)