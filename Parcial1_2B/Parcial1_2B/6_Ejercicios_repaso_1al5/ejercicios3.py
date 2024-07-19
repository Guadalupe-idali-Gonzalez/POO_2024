# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

#while
acumulador=0
contador=1
while contador<=60 and contador >=1:
    acumulador= contador * contador
    print("Con while, el cuadrado de ", contador, " es: ", acumulador)
    contador += 1
    
#for
acumulador=0
contador=1
print("---------------------------------------")
for contador in range (1,61):
    acumulador = contador*contador
    print("Con For, el cuadrado de: ", contador , " es", acumulador )
    contador +=1
