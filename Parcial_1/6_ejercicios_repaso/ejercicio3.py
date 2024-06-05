 # Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for
#
cuadrado=0
for i in range(1,61):
    cuadrado=i*i
    print(f"{i}^2={cuadrado}")