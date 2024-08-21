import math

print("calcular el ladoC")
ladoA = float(input("ingrese el ladoA :"))
ladoB = float(input("ingrese el ladoB :"))

ladoC = math.pow(ladoA,2) + math.pow(ladoB,2)
#ladoC = math.sqrt(ladoC)
ladoC = round(math.sqrt(ladoC),2)
print(f"""El ladoC para un triangulo de cateto {ladoA} y cateto {ladoB} = {ladoC}""")