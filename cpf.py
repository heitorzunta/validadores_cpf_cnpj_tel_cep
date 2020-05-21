# Instancia e valida o CPF do usuário

from validate_docbr import CPF

class Cpf:

    def __init__(self, documento):
        documento = str(documento)

        if (self.validar_um_cpf(documento)):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido!')   
    
    def validar_um_cpf(self, documento):
        if len(documento) == 11:
            validar = CPF()
            return validar.validate(documento)
        else:
            raise ValueError ("Quantidade de digitos do CPF é inválida!")

    def mascara_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.mascara_cpf()        
