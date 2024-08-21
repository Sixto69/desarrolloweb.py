def calcular_precio(tipo_pan, cantidad_gramos):
    precios = {
        "Hallulla": 1990,
        "Marraqueta": 2010,
        "Pita": 2500,
        "Integral": 2600
    }
    
    if tipo_pan not in precios:
        raise ValueError("Tipo de pan no válido.")
    
    precio_por_kilo = precios[tipo_pan]
    cantidad_kilos = cantidad_gramos / 1000
    costo_total = precio_por_kilo * cantidad_kilos
    return costo_total, cantidad_kilos

def verificar_alfajores(cantidad_kilos, tipo_pan):
    if tipo_pan == "Integral":
        return 0
    alfajores = int(cantidad_kilos // 3)
    return alfajores

def main():
    print("Bienvenido a la panadería")
    
    tipo_pan = input("Ingrese el tipo de pan (Hallulla, Marraqueta, Pita, Integral): ").capitalize()
    cantidad_gramos = float(input("Ingrese la cantidad en gramos: "))
    
    try:
        costo_total, cantidad_kilos = calcular_precio(tipo_pan, cantidad_gramos)
        alfajores = verificar_alfajores(cantidad_kilos, tipo_pan)
        
        print("\n--- Datos de Entrada ---")
        print(f"Tipo de pan: {tipo_pan}")
        print(f"Cantidad en gramos: {cantidad_gramos}")
        
        print("\n--- Datos de Salida ---")
        print(f"Costo total: ${costo_total:.2f}")
        if alfajores > 0:
            print(f"¡Felicidades! Has recibido {alfajores} alfajor(es) de regalo.")
        else:
            print("No has recibido alfajores de regalo.")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
