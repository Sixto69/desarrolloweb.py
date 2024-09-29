class Pelota:
    def __init__(self, color='blanco', tamaño='mediano'):
        self.color = color
        self.tamaño = tamaño

    def mostrar_info(self):
        print(f"Pelota de color {self.color} y tamaño {self.tamaño}.")

# Creando una instancia de la clase Pelota
pelota_de_andy = Pelota()
pelota_de_andy.mostrar_info()

