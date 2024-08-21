

    # Solicitar datos al usuario
descripcion = input("Ingrese la descripción del artículo: ")
costo= int(input("Ingrese el costo de producción del artículo: "))

    # Calcular el precio de venta
precio_venta = costo * 1.2 + costo * 0.19

    # Imprimir los resultados
print(f"""El precio de venta del producto {descripcion} con precio de costo ${costo} es ${precio_venta}""")


