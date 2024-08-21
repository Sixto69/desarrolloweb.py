claves = ['nombre','apellido','edad','altura']
valores = ['Juan','Pérez', 33, 1.75]
print({k:v for k,v in zip(claves, valores)})