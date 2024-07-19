# 2.- 
# Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for


lista=[]
opcion= True
while opcion:
    opcion=input("¿Qué opcion quieres hacer?\n 1.-Agregar \n 2.- Salir \n Coloca un numero: ")
    if opcion =='1':   
        agregar=input("Coloca el numero o palabra a agregar a tu lista: ")
        lista.append(agregar)
    elif opcion=='2':
        opcion=False
    else:
        print("Coloca un de las opciones anteriores (1 o 2)")

print(lista)
    
    