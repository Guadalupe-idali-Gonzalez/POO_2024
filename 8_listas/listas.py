import os
from otras_funciones import remover_pelicula,agregar_pelicula,consultar_pelicula
# """

# List (Array)
# son collecciones o conjuntos de datos/valores bajo
# un mismo nombre, para acceder a los valores se
# hace con un indice numerico

# # Nota: sus valores si son modificables

# # La lista es una coleccion ordenada y nodificable.
# # Permite miembros duplicados.


# #Ejemplo 1 crear una lista de numeros e imprimir el contenido 
# #Arreglo o vector unidimencional
# numeros=[23,34]
# print(numeros)

# #Recorrer lista con ciclo for
# for i in numeros:
#     print(i)

# #Recorrer la lista con ciclo while

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
# while i<len(palabras):
#     if palabras[i]==palabra__buscar:
#         print("Se encontro la palabra Se encontro la palabra {palabra__buscar} a buscar en a la posicion {palabras.index(i)}")
#         encontro=True
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
# # print(numeros)


# #Ejemplo 4 crear lista multilinea (matriz) para agregar los nombres y numeros telefonicos

# agenda=[
#     ["Carlos",6181234567],
#     ["Leo",6181234567],
#     ["Sebastian",6181234567],
#     ["Pedro",6181234567]
# ]

# print(agenda)

# for i in agenda:
#     print(f"{agenda.index(i)+1}.-{i}")





#Ejemplo 5, crear un programa que permita Gestionar (Administrar) peliculas, colocar un menu de opciones para agregar , remover, consultar peliculas.
#Notas
# 1 Utilizar funciones y mandar llamar desde otro archivo
# 2 Utilizar litas para almacenar los nombres de peliculas
def agregar_pelicula():
    global peliculas_catalogo
    peli_nom=input("Ingrese el nombre de la pelicula: ")
    peliculas_catalogo.append(peli_nom)

def remover_pelicula():
    global peliculas_catalogo
    try:
        peli_elim=input("Ingrese el nombre de la pelicula a eliminar: ")
        peliculas_catalogo.remove(peli_elim)
    except:
        print("Esa pelicula no existe en el catalogo")
def consultar_pelicula():
    global peliculas_catalogo
    print (peliculas_catalogo)

print("Pelisclonfix")
peliculas_catalogo=[]
repetir=True
while repetir==True:
    print("Menu")
    print("Agregar [1]\nRemover [2]\nConsultar [3]\nSalir[4] ")
    opc=int(input("Ingrese la opcion: "))
    if opc==1:
        print("Agregar pelicula")
        agregar_pelicula()
        repetir=True
    elif opc==2:
        print("Remover pelicula")
        remover_pelicula()
        repetir=True
    elif opc==3:
        print ("Consultar pelicula")
        consultar_pelicula()
        repetir=True
    elif opc==4:
        print("Programa terminado")
        repetir=False
    else:
        print("Esa no es una opcion valida")
        repetir=True
   
   
 


