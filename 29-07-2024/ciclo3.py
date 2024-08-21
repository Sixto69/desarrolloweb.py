import getpass
password = getpass.getpass("Ingrese la clave :")


plata = int(input("Ingrese tu bolsa de dinero :")) 
ganas ="s"
while plata > 0:
  gasto = int(input("Ingrese tu gasto :"))
#plata  = plata - gasto 
  if gasto <= plata and gasto%5000==0:
     plata -= gasto  
     print(f"gastaste {gasto} y te queda {plata}")
  else:
    print("saldo insufiente")
  ganas = input("tienes ganas de seguir gastando dinero o s/n").upper()
