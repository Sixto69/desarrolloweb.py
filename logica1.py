color = "verde", "azul", "rojo"
peso = [1, 100]
color = input("Ingrese el color:")
peso = int(input("Ingrese peso:"))
if color.lower() == "verde" and peso >= 1 and peso < 50:
    print("OK")
elif color.lower() == "azul":
    print("paso")
elif color.lower() == "rojo" and peso >= 10 and peso <= 50:
    print("tamo")
else:
    print("Error")


