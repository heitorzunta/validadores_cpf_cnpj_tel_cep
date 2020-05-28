from Cep import Cep

cep_residencia = Cep(79112210)
print(cep_residencia)

rua, bairro, cidade, estado = cep_residencia.dados_cep()

print(rua, bairro, cidade, estado)

dados_endereco = (cep_residencia.dados_cep())
print(dados_endereco)



cep_residencia_errado = Cep(11111111)

print(cep_residencia_errado.dados_cep())