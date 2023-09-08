

class Relógio_Digital_Simples:
    # Construtor - inicializa os atributos
    def __init__(self,hora,minuto):
        self.hora = hora
        self.minuto = minuto

    def mudar_horas(self,hora):
        self.hora=hora

    def mudar_minutos(self,minuto):
        self.minuto=minuto

    def mostrar_horario(self):
        print(f'{meu_relogio.hora:02}:{meu_relogio.minuto:02}') # formatação com dois dígitos

meu_relogio = Relógio_Digital_Simples(0,0)
meu_relogio.hora = 10
meu_relogio.minuto = 14
meu_relogio.mostrar_horario()
