"""
import sys
# solicitamos el número de pares a generar
n = 10
# generamos una lista vacía para almacenar los pares
lista_par = []
for i in range(n):
# podemos hacer append de los valores generados
# en este caso partimos desde el 2
    lista_par.append(2*i + 2)
# mostramos el resultado 
print(lista_par)
"""
"""
notas = []
for i in range(int(input("ingrese la cantidad de elementos:"))):
    x = float(input("Ingrese una nota:"))
    notas.append(x)
print(notas, min(notas), max(notas))
"""
"""
lista = [x**3 for x in range(8)]
print(lista)
"""


a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = []
for i in range(n):
    if a[i] >= 1000:
        filtered_array.append(a[i])
print(filtered_array)

filtro = {x for x in a if x >= 1000}
print(filtro)

minutos = [120, 50, 600, 30, 90, 10, 200, 0, 500]
resultado = ["bien" if x < 90 else "mal" for x in minutos]
print(resultado)

seconds = [100, 50, 1000, 5000, 1000, 500]
s = [ int(x//60) for x in seconds]
print(s)
