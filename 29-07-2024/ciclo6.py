"""
diccionario = {"Nombre": "Carlos",
 "Apellido": "Santana",
 "Ocupación": "Guitarrista"}
for clave, valor in diccionario.items():
   print(f"Mi {clave} es {valor}")
   """
for i in range(1, 11): # Itera sobre los números del 1 al 10
 if i == 5:
   continue # Salta a la siguiente iteración si el número es 5
 print(i)  