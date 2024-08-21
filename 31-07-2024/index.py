#Método insert(i,x)

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
lista_de_numeros.insert(11, 20)
print(lista_de_numeros)

#Método pop()
colores = ['verde', 'rojo', 'rosa', 'azul']
colores.pop(3)
'azul'
color = colores.pop(0)
print(color)

#Método reverse()

numeros = [100, 20, 70, 500]
animales = ["perro", "gato", "hurón", "erizo"]
numeros.reverse()
animales.reverse()
print(numeros)
print(animales)

#Método sort()
animales.sort()
numeros.sort()
print(animales)
print(numeros)

#max, min, sum
#Funciones de uso intuitivo
numeros = [ 5, 2, 9, 1, 7]
maximo = max(numeros)
minimo = min(numeros)
suma = sum(numeros)
print("El máximo valor en la lista es:" , maximo)
print("El mínimo valor en la lista es:" , minimo)
print("La suma de todos los elementos en la lista es:" , suma)

"""
Método sorted()
Obtiene los mismos resultados del método sort, y en el caso de querer ordenar de manera
descendente se utiliza el argumento reverse = True
"""
# ordenamiento ascendente
#num = (3,6,7,4,1)
num_ordenados =sorted([3,6,7,4,1])
print(num_ordenados)


# ordenamiento descendente
num = (3,6,7,4,1)
num_ordenados =sorted(num, reverse = True)
print(num_ordenados)

#descendente (de la Z a la A)?
# Ordenar la lista en orden descendente
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letras_ordenadas = sorted(letras, reverse=True)
print(letras_ordenadas)
