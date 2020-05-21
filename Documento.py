# Instancia e valida o CPF do usuário
# Instancia e valida o CNPJ da empresa
# Utilizaremos o conceito de Factory para dividir a classe em 3 classes mais simples de compreender

from validate_docbr import CPF, CNPJ

class Documento:
    
    @classmethod
    def cria_documento(self, documento):
        documento = str(documento)

        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError("Erro: O documento não é um CPF/CNPJ")         


class Cpf():
    def __init__(self, documento):
        if self.validar(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.format()

    def validar(self, documento):
        dado = CPF()
        return dado.validate(documento)

    def format(self):
        cpf = CPF()
        return cpf.mask(self.cpf)


class Cnpj():
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido!')

    def __str__(self):
        return self.format()

    def valida(self, documento):
        dado = CNPJ()
        return dado.validate(documento)

    def format(self):
        cnpf = CNPJ()
        return cnpf.mask(self.cnpj)
