import math
# datos de entrada
# gravedad y el radio
gravedad = float(input("Ingrese la gravedad"))
radio = float(input("Ingrese el radio"))
velocidad_escape = math.sqrt(2*gravedad*radio*1000)
print(f"""La velocidad de escape en base a {gravedad} de gravedad y en base a {radio} radio es {velocidad_escape:.1f } m/s""")