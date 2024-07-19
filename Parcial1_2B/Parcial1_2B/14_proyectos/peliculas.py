import os
from otras_funciones import *


peliculas=[]
print("...:::Gestor de peliculas:::... \n 1.-- Agregar pelicula \n 2.-- Eliminar una pelicula \3.-- Actualizar pelicula \n 4.-- Consultar \n 5.-- Buscar \n 6.- Salir").upper()
opcion=input ("Selecciona una opcuion")

if opcion =='1':
    insertarPeliculas()
elif opcion =='2':
    eliminarPeliculas()
elif opcion=='3':
    actualizarLista()
elif opcion=='4':
    print(peliculas)