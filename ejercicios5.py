pan = input("Ingrese pan H allullas M arraquetas P ita I ntegral : ")
peso = float(input("Ingrese el peso en gramos :"))
if pan.upper() == "H":
  valor = 1990
elif pan.upper() == "M":
  valor = 2010
elif pan.upper() == "P":
  valor = 2500
else:
  valor =2600

pago = valor*peso/1000
if pan.upper() != "I":
  alfajores = int((peso/1000)//3)
  print(f"""Pan comprando {pan.upper()} precio por kilo ${valor} kilos {peso/1000:.3f} kg precio a pagar ${pago}
alfajores {alfajores}""")

  
