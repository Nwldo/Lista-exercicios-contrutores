from time import sleep

class Bicicleta:
    def __init__(self, veloc_atual, altura_cela,peso_ciclista, calibragem):
        self.veloc_atul = veloc_atual
        self.altura_cela = altura_cela
        self.calibragem = calibragem
        self.peso_ciclista = peso_ciclista
    def alterar_velocidade(self, velocidade):
        velocidade+=4
        return velocidade
    def regular_cela(self, altura):
        altura+=altura
        return altura
    def calibragem_pneus(self, peso):
        if peso <= 45:
            self.calibragem = '28 – 30 psi'
            return self.calibragem
        elif 45 < peso <= 50:
            self.calibragem = '29 – 31 psi'
            return self.calibragem
        elif 50 < peso <= 55:
            self.calibragem = '30 – 32 psi'
            return self.calibragem
        elif 55 < peso <= 60:
            self.calibragem = '31 – 33 psi'
            return self.calibragem
        elif 60 < peso <= 65:
            self.calibragem = '32 – 34 psi'
            return self.calibragem
        elif 65 < peso <= 70:
            self.calibragem = '33 – 35 psi'
            return self.calibragem

    def andar_bicicleta(self):
        self.peso_ciclista = int(input('Informe o seu peso: '))
        self.calibragem_pneus(self.peso_ciclista)
        self.altura_cela = int(input('Informe a regulagem da cela: '))
        self.regular_cela(self.altura_cela)
        print(f'Peso do Ciclista: {self.peso_ciclista}kg\n(Dianteiro/traseiro): {self.calibragem}\n'
              f'Regulagem da cela: {self.altura_cela}cm')
        while True:
            self.veloc_atul = self.alterar_velocidade(self.veloc_atul)
            sleep(2)
            print(f'Velocidade da bicicleta: {self.veloc_atul}')
            if self.veloc_atul == 20:
                break


minha_bicicleta = Bicicleta(0,0,0,0)
minha_bicicleta.andar_bicicleta()