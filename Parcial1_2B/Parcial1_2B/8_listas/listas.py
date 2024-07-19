# """

# List (Array)
# son collecciones o conjuntos de datos/valores bajo
# un mismo nombre, para acceder a los valores se
# hace con un indice numerico

# Nota: sus valores si son modificables

# La lista es una coleccion ordenada y nodificable.
# Permite miembros duplicados.


#Ejemplo 1 crear una lista de numeros e imprimir el contenido 
#Arreglo o vector unidimencional
# numeros=[23,34]
# print(numeros)

#Recorrer lista con ciclo for
# for i in numeros:
#     print(i)

#Recorrer la lista con ciclo while

# i=0
# while i <= len(numeros) -1:
#     print(numeros[i])
#     i+=1


#Ejemplo 2 crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 

# palabras=["naranja", "utd", "america", "azul"]

# palabra__buscar=input("Ingresa la palabra a buscar: ")

# encontro=False

# for i in palabras:
    

#     if i == palabra__buscar:
#         print(f"Se encontro la palabra {palabra__buscar} a buscar en a la posicion {palabras.index(i)}")
#         encontro=True

#While
# i=0
# while i<=len(palabras) -1:
#     if palabras[i]==palabra__buscar:
#         print(f"Se encontro la palabra {palabra__buscar} en la posicion {i}")
#         encontro = True
#     i+=1
# #ejemplo 3 Agregar y eliminar elementod de una lsita os.system("clear")

# numeros=[23,34,23]
# print(numeros)

# #Agredar un elemento
# numeros.append(100)
# print(numeros)
# numeros.insert(3,200)
# print(numeros)

# #Eliminar un elemento
# numeros.remove(100)#indicar el elemnto a borar 
# print(numeros)
# numeros.pop(2)#indicar la posicion del elemento a borrar 
# print(numeros)

#ejemplo 4 crear una lista multilinea (matriz) para agregar nombrea y numeros telefonicos

# agenda=[
#     ["Carlos",618234567 ],
#     ["Leo",665121485],
#     ["Sebastian",6182341223],
#     ["Pedro", 6171236789]
# ]

# print(agenda)
# for i in agenda:
#     print(f"{agenda.index(i)+1}.-{i}")

#ejemplo 5 Crear un programa que permita gestionar (administrar) pelicula, colocar un menu de opciones para agregar, remover, consultar peliculas
#Notas:
#1.- Utilizar funciones y mandar a llamar desde otro archivo
#2.- Utilizar listas para almacenar los nombres de las peliculas
# import os
# peliculas=[]
# opciones=True
# while opciones:
#     print("...:::Gestor de peliculas:::... \n 1.-- Agregar pelicula \n 2.-- Eliminar una pelicula \3.-- Consultar pelicula \n 4.-- Salir")
#     hacer=input(print("Selecciona una opcion: "))
#     if hacer != '5':
#         print("hola")
#     else:
#         print("Gracias por usar el SW")
#         break


# def opcionesHacer(hacer):

#     if hacer == '1':
#         peliculas.append(hacer)

import os

def insertarPeliculas():
    pelicula=input("Ingresa el nombre de la pelicula: ")
    peliculas.append(pelicula)
    espereTecla()

def eliminarPeliculas():
    pelicula=input("Ingresa el nombre de la pelicula: ")
    for i in peliculas:
        if i==pelicula:
            print(f"Se elimino {pelicula}")
            peliculas.remove(pelicula)
    espereTecla()
    
def espereTecla():
    print("Coloque cualquier tecla para continuar...")
    input()

peliculas=[]
print("...:::Gestor de peliculas:::... \n 1.-- Agregar pelicula \n 2.-- Eliminar una pelicula \3.-- Actualizar pelicula \n 4.-- Consultar \n 5.-- Buscar \n 6.- Salir").upper()
opcion=input ("Selecciona una opcuion")

if opcion =='1':
    insertarPeliculas()
elif opcion =='2':
    eliminarPeliculas()
elif opcion=='3':
    print("Flata actualizar...")