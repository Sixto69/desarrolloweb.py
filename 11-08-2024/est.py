import math

#funciones
def media(lista):
    return sum(lista)/len(lista)

def sdd(lista, media):
    diff = [(elemento-media)**2 for elemento in lista]
    return math.sqrt(sum(diff)/len(lista)-1)

def resultado(lista):
    m = media(lista)
    sd = sdd(lista, m)
    lista_estanderizada = [(valor-m)/sd for valor in lista]
    return m, sd, lista_estanderizada

lista = [1,2,3,4,5,6]

m, desv_st, l_e = resultado(lista)
print('La media es :', m)
print('La desviacion estandar es :', desv_st)
print('La lista estandarizada es :', l_e)