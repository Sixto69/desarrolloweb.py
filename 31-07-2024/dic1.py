mes = ["octubre", "noviembre", "diciembre"]
venta = [65000, 68000, 72000]
filtro = {k:v  * 1.1 for k,v in zip(mes,venta)}
filtro1 = {k:v  * 0.8 for k,v in zip(mes,venta)}
print(filtro, filtro1)