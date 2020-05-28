#classe por validar e buscar informações de um determinado CEP por meio da API https://viacep.com.br/ws/
# Para instalar a biblioteca request use : pip install requests

import requests

class Cep:
    def __init__(self, cep):
        cep = str(cep)
        if self.validar_cep(cep):
            self.cep = cep
        else:
            raise ValueError('CEP inválido!')    

    def __str__(self):
        return self.formatar_cep()

    def validar_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formatar_cep(self):
        parte1 = self.cep[:5]
        parte2 = self.cep[5:]
        return "{}-{}".format(parte1, parte2)

    def dados_cep(self):
        endereco = 'https://viacep.com.br/ws/'+self.cep+'/json/'
        r = requests.get(endereco)
        dados = r.json()   

        if 'erro' in dados:
             raise ValueError ("O CEP não existe no banco de dados do VIACEP")
        
        else:
            return (
                dados['logradouro'],
                dados['bairro'],
                dados['localidade'],
                dados['uf']
            )
