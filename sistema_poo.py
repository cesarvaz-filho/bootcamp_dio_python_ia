class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        print("Classe inicializada")
        self.cor = cor,
        self.modelo = modelo,
        self.ano = ano,
        self.valor = valor

    def buzinhar(self):
        print("Plin Plin")

    def parar(self):
        print(f"A bicicleta {self.modelo} parou")

    def correr(self):
        print("A bicicleta está correndo")

    def trocar_marcha(self, nr_marcha):
        print("Marcha trocada")
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
    def __del__(self):
        print("Instância de classe destruída")

caloi = Bicicleta("preta", "rx12", 2024, 1200)

print(caloi)