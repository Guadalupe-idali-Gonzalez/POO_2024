#Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado
suma=0
resta=0
multi=0
div=0

num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))

print("Suma")
suma=num1+num2
print(f"{num1}+{num2}={suma}")


print("Resta")
resta=num1-num2
print(f"{num1}-{num2}={resta}")

print("Multiplicacion")
multi=num1*num2
print(f"{num1}*{num2}={multi}")

print("Division")
div=num1/num2
print(f"{num1}/{num2}={div}")

