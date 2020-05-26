import re

class Telefone:
    mascara = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
    
    def __init__(self, numero):
        if self.verifica_telefone(numero):
            self.n_telefone = numero
        else:
            raise NameError("Número telefonico inválido")
        
    def __str__(self):
        return self.telefone_formatado()
        
    def verifica_telefone(self, numero):

        if re.search(Telefone.mascara, numero):
            return True
        else:
            return False

    def telefone_formatado(self):
        string_tel = re.search(Telefone.mascara, self.n_telefone)
        
        if string_tel[1] is None:
            return '({}){}-{}'.format(string_tel[2], string_tel[3], string_tel[4])
        else:
            return '+{}({}){}-{}'.format(string_tel[1], string_tel[2], string_tel[3], string_tel[4])    
