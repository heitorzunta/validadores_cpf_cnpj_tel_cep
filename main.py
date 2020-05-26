from Telefone import Telefone

'''texto = "este é um teste contém o meu telefone fixo: 556733616439 e o meu celular é: 67981402225"
#mascara = '[0-9]{10,11}'
mascara1 = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
busca = re.findall(mascara1, texto)
print(busca) '''

numero_fixo = '556733616439'
numero_celular = '67991402225'

telefone1 = Telefone(numero_fixo)
telefone2 = Telefone(numero_celular)

print(telefone1)
print(telefone2)