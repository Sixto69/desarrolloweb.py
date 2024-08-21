"""
Generar un algoritmo que permita ingresar 10 números y mostrar el promedio de los números múltiplos de 3 ingresados
"""




numeros = 0
suma = 0
for i in range(10):
    n = int(input("Ingrese el numero:"))
    if n%3 == 0:
        numeros += 1
        suma += 1
        print(suma/numeros)
