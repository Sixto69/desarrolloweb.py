
plata = int(input("Ingrese tu bolsa de dinero"))
while plata > 0:
  gasto = int(input("Ingrese tu gasto"))
#plata  = plata - gasto 
  if gasto <= plata:
     plata -= gasto  
     print(f"gastaste {gasto} y te queda {plata}")
  else:
    print("saldo insufiente")
