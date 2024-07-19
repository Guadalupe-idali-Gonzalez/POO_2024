#El for es una estructura de control repetitiva o ciclica que funciona con interacciones xx veces de acuerdo a los valores numericos enteros que contenga

#sintaxis

#for variable in elemento_iterable(list, range, etc)
#    bloque istrucciones

#Ejemplo 1 Crear un programa que imprima 5 veces el caracter @

for contador in range (1,6):
    print("@")

#Ejemplo 1 Crear un programa que imprima los numeros del 1 al 5, los sume e imprima la suma al final

suma=0
for contador in range (1,6):
    print(contador)
    suma+=contador
print(f"La suma es: {suma}")

#Ejemplo numero 3 Crear un programa que solicitu un numero entero y que a partir de este numero genere e imprima la tabla de multiplicar correspondiente

numero=int(input("Ingrese un numero: "))

multi=0
for i in range(1,11):
    multi=numero*i
    print(f"{numero} X {i} = {multi}")
