departamentos1 = ("linea_blanca")
departamentos2 = ("Aseo y limpieza")
departamentos3 = ("Refrigeracion")

cant_producto = int(input("Ingrese cantidad"))
precio_unitario = int(input("Ingres el precio"))
departamentos = int(input("Ingrese depto 1.Linea blanca, 2.Aseo y Limpieza, 3.Refrigeracion"))

if cant_producto >10 and departamentos == 2:
   a_pagar = (precio_unitario * cant_producto)*0.92


