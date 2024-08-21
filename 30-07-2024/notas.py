suma=0
for x in range(5):
    while True:
      nota = float(input("Ingrese una nota : "))
      if nota >= 1 and nota <= 7:
        print("Nota valida")
        suma += nota
        break
      else:
        print("nota inválida")
        continue
print(f"El promedio es {suma/5:.2f}")