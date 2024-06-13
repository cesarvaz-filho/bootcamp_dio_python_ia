from abc import ABC, abstractmethod

class Controle_remoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Controle_tv():
    def ligar(self):
        print("Ligado")

    def desligar(self):
        print("Desligado")

controle = Controle_tv()
controle.ligar()
controle.desligar()