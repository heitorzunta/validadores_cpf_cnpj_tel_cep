# Instancia e valida o CPF do usuário
# Instancia e valida o CNPJ da empresa

from validate_docbr import CPF, CNPJ

class CpfAndCnpj:

    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)

        if self.tipo_documento == 'cpf':
            if (self.validar_um_cpf(documento)):
                self.cpf = documento
            else:
                raise ValueError('CPF inválido!')

        if self.tipo_documento == 'cnpj':
            if (self.validar_um_cnpj(documento)):
                self.cnpj = documento
            else:
                raise ValueError('CNPJ inválido!')       
    
    def validar_um_cpf(self, documento):
        if len(documento) == 11:
            validar = CPF()
            return validar.validate(documento)
        else:
            raise ValueError ("Quantidade de digitos do CPF é inválida!")

    def validar_um_cnpj (self, documento):
        if len(documento) == 14:
            validar = CNPJ()
            return validar.validate(documento)
        else:
            raise ValueError('Quantidade de dígitos do CNPJ é inválida!')    

    def mascara_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def mascara_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)    

    def __str__(self):

        if self.tipo_documento == 'cpf':
            return self.mascara_cpf()
        else:
            return self.mascara_cnpj()            
