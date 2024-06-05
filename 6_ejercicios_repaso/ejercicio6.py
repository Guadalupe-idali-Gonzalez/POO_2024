#Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10
multi=0
for i in range(1,11):
    print(f"Tabla de multiplicar del {i}")
    for e in range(1,11):
        multi=i*e
        print(f"{i}*{e}={multi}")