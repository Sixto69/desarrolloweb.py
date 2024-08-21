"""
Generar un algoritmo que permita ingresar un número, debe ser mayor a 10.
En caso contrario escribe 5 veces la palabra error y vuelve a pedir el número.
El usuario decide cuando terminar.
"""

while True:
      num = int(input("Ingrese el numero :"))
      if num <= 10:
            for x in range (5):
                  print("ERROR")
      else:
            print(f"Numero ingresado : {num}")
            op = input("Desea continuar? S/N :").upper()
            if op == 'N':
                  break