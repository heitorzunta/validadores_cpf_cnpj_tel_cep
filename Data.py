from datetime import datetime, timedelta

class Data:
    def __init__(self):
        self.data_cadastro = (datetime.now()

    def format_data(self):
        dia = self.data_cadastro.strftime("%d")
        mes = self.data_cadastro.strftime("%m")
        ano = self.data_cadastro.strftime("%Y")
        hora = self.data_cadastro.strftime('%H')
        minuto = self.data_cadastro.strftime('%M')
        segundo = self.data_cadastro.strftime("%S")
        return 'DATA: {}/{}/{} -- HORA: {}:{}:{}'.format(dia, mes, ano, hora, minuto, segundo)

    def tempo_de_cadastro(self):
        tempo =  (datetime.now() - self.data_cadastro).days
        return f'DIAS: {tempo}'

    def __str__(self):
        return self.format_data()    
