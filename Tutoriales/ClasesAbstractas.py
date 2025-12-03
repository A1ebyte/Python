from abc import abstractmethod, ABCMeta


class Abstracta(metaclass=ABCMeta):
    @abstractmethod
    def metodoAbstracto(self):
        pass

    def metodoNormal(self):
        print("hola")

class Hija(Abstracta):
    def metodoAbstracto(self):
        print("adios")