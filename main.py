from cpfAndCnpj import CpfAndCnpj


cpf = 99682842115
cnpj = 17555477010603

novo_cpf = CpfAndCnpj(cpf, 'cpf')
print(novo_cpf)

novo_cnpj = CpfAndCnpj(cnpj, 'cnpj')
print(novo_cnpj)