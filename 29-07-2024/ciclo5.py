
import time
import sys
i = int(sys.argv[1]) # fijar valor inicial
while i > 0:
 print(i) # Muestra el valor de i
 time.sleep(1) # espera un segundo
 i -=1 # Descuenta 1 al valor de i.

print("BOOM!") # al salir del ciclo la bomba explota!!