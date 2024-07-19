
#  1.- Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado


numeros=[12,253,36,784,905,234,755,862]
#A)
print("-----A-----")
for i in numeros:
    print(i, end=" ")

#B)
print("-----B-----")
for i in numeros:
    print(str(i))

#C)
print("-----C----")
numeros.sort()
print(numeros)

#D)
print("-----D-----")
print(len(numeros))
#E)
print("-----E-----")

buscar=int(input("¿Que numero de la lista quieres buscar?:"))
for j in numeros:
    if j==buscar:
        print(f"Se encontro la palanra {buscar} en la posicion {numeros.index(j) + 1}")

