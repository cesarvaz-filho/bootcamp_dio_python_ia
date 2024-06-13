class Veiculo:
    def __init__(self, cor, placa, nro_rodas):
        self.cor = cor
        self.placa = placa
        self.nro_rodas = nro_rodas
    
    def ligar_motor(self):
        print("Ligando motor...")

    def __str__(self):
         return self.cor

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, nro_rodas, carregado):
        super().__init__(cor, placa, nro_rodas)
        self.carregado = carregado
    def esta_carregado(self):
            print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("Vermelha", "abc-123", 2)
moto.ligar_motor()

carro = Carro("Branco", "cde-123", 4)
carro.ligar_motor()

caminhao = Caminhao("Preto", "fgh-789", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()