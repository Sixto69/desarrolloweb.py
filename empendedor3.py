import math
#utilidades
valor_suscripcion = int(input("Ingrese el valor de  suscripción : "))
usuarios = int(input("Ingrese la cantidad de  usuarios : "))
utilidades_anteriores = int(input("Ingrese las utilidades del periodo anteriores :"))
gastos_totales = int(input("Ingrese el gastos_total :"))
#calculos
utilidades_actuales = (valor_suscripcion * usuarios - gastos_totales)
razon_ganancia = utilidades_actuales / utilidades_anteriores
print(f""" las utilidades en base a un valor ${valor_suscripcion} de suscripcion y una cantidad de usuario de {usuarios} 
      menos los gastos totales ${gastos_totales} es igual a ${utilidades_actuales}. 
      La razon de ganancia del periodo actual versus el anterior es {razon_ganancia:.2f}""")
