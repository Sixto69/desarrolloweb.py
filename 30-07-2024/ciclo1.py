"""
Generar un algoritmo que permita ingresar dos números.
Si el primer número es mayor que el segundo muestra la suma
Si son iguales muestra la multiplicación
Si el segundo es mayor que el primero muestra la tabla del 5 de ese número
"""


num1 = int(input("Ingrese primer numero :"))
num2 = int(input("Ingrese segundo numero :"))
if num1 > num2:
    print(num1 + num2)
elif  num1 == num2:
    print(num1 * num2)
else:
    for x in range(1,11):
        print(f"{num2} * {5} = {num2 * 5}")
    
