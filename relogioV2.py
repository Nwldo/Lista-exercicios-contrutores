

class Relógio_Digital_Simples:
    # Construtor - inicializa os atributos
    def __init__(self,hora,minuto):
        self.hora = hora
        self.minuto = minuto

    def checar_horario(self, hora, minuto):# checa se o horário digitado é válido
        # Checar se o horario é válido
        if 1 <= hora <= 23:
            self.editar_horas(hora)
        if 1 <= minuto <= 59:
            self.editar_minutos(minuto)
        # caso não digite no intervalo válido mostrar horário padrão


    def editar_horas(self,hora):
        self.hora=hora

    def editar_minutos(self,minuto):
        self.minuto=minuto

    def mostrar_horario(self):
        print('Ajustar horário')
        hora = int(input('Informe tempo em horas: '))
        minuto = int(input('Informe tempo em minutos: '))
        self.checar_horario(hora, minuto)
        print(f'{meu_relogio.hora:02}:{meu_relogio.minuto:02}') # formatação com dois dígitos

meu_relogio = Relógio_Digital_Simples(0,0)
meu_relogio.mostrar_horario()
