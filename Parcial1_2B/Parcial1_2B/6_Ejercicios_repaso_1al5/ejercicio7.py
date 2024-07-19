#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

num1=int(input("Coloca el primer numero: "))
num2=int(input("Coloca el segundo numero: "))

print("Los numeros impares entre ", num1, " y ", num2, " es:")
if num1 < num2:
    for num in range (num1, num2 + 1):
         if num % 2 != 0:
              print (num)
else:
     print("Coloca un numero valido")