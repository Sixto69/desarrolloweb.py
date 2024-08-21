
#desarrollar un programa que permita obtener el IMC de una persona 
# a partir de su peso en kilogramos y su estatura en metros.

import math as m

peso = float(input("Ingrese el peso en Kg: "))
estatura = float(input("Ingrese la estatura en mt: "))
imc = round(peso / (m.pow(estatura,2)),3)
print(f"""El IMC en base a un peso de {peso} kg y una estatura de {estatura} mts es {imc}""")