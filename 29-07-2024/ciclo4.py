chilenos = 0
extranjeros = 0
sigue = "S"
while sigue == "S":
    nacionalidad = int(input("Nacionalidad 1=CH 2=EX :")) 
    if nacionalidad == 1: ## contar chileno
        chilenos += 1
    elif nacionalidad == 2: ## contar extranjeros
        extranjeros += 1
    else:
      print("valor no valido")
    sigue = input("Desea continua s/n :").upper()
print(f"""Chilenos {chilenos}, extranjeros {extranjeros} % de chileno versus extranjeros 
            {chilenos/extranjeros:.2f}""")

    


