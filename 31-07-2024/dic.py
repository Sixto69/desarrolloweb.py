pais = ["mexico", "chile", "argentina"]
usuario = [70, 50, 55]
filtro = {k:v for k,v in zip(pais, usuario) if v <60}
print(filtro)
