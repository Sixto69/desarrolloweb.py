class Medicamento:
    def __init__(self, valor=35000, descuento=0.05, iva=0.18):
        self.valor = valor
        self.descuento = descuento
        self.iva = iva

    def calcular_precio_final(self):
        valor_descuento = self.valor * self.descuento
        valor_con_descuento = self.valor - valor_descuento
        valor_iva = valor_con_descuento * self.iva
        precio_final = valor_con_descuento + valor_iva
        return precio_final

    def mostrar_informacion(self):
        print(f"El valor del medicamento es: {self.valor}")
        print(f"El descuento es: {self.descuento * 100}%")
        print(f"El IVA es: {self.iva * 100}%")
        print(f"El precio final es: {self.calcular_precio_final()}")

# Ejemplo de uso
med = Medicamento()
med.mostrar_informacion()
