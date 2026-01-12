from abc import abstractmethod, ABCMeta

class Vehiculo(metaclass=ABCMeta):
    def __init__(self,matricula,fechaCompra):
        self.matricula = matricula
        self.fechaCompra = fechaCompra

    @abstractmethod
    def descripcion(self):
        pass

class Carro(Vehiculo):
    def __init__(self,matricula,fechaCompra):
        super().__init__(matricula,fechaCompra)

class Moto(Vehiculo):
    def __init__(self,matricula,fechaCompra):
        super().__init__(matricula,fechaCompra)

v = Vehiculo("Vidal",1)
print(v.matricula)