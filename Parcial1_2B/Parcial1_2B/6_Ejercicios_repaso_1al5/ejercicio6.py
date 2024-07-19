#Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

cont1=0
cont2=0
for cont1 in range (1,11):
    print(f"-----La tabla de multiplicar del numero: {cont1} es: ------")
    for cont2 in range (1,11):
        multi= cont1*cont2
        print(f"{cont1} X {cont2} = {multi} ")
        