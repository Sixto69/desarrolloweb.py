"""
import random
valores = [0,4,5,6,7,8,9]
valore=[int(random.random()*20)for x in range(7)]
print(valores)

divisibles = []
for valor in valores:
    if valor % 2 == 0:
        divisibles.append('Divisible')
    else:
        divisibles.append('No Divisible')
print(divisibles)
"""
"""
valores = [0,4,5,6,7,8,9]
div2 =['Divisible' if x % 2 == 0 else 'No Divisible' for x in valores]
print(div2)
"""

"""
Generar una lista con 10 numeros que sean multiplos de 5 o sean mayores de 50, de lo cantrario coloca 0
"""
import random
valores = [int(random.random()*200) for x in range(10)]
nueva_lista = [x if x%5==0 or x > 50 else 0 for x in valores]
print(valores)
print(nueva_lista)

lista = ['1' if x % 2 == 0 else '2' for x in valores]
print(lista)