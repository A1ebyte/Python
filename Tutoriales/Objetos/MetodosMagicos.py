"""
De esta manera se sobrescriben estos metodos, tiene que actuar como los originales
__init__ constructor
__del__ desconstructor
__str__ devolver texto
__len__ longitud
__add__ suma
__sub__ resta
__mul__ multiplicar
__truediv__ division
__eq__ igual a
__ne__
__gt__  mayor que
__lt__  menor que
__iter__
__next__
"""

class CuentaCorriente:
    def __init__(self,codigo,titular,saldo=5000):    #es un metodo magico
        self._codigo=codigo  # atributo "protegido"
        self.__titular=titular  # atributo "privado"
        self.saldo=saldo  # atributo "publico"
        #para llamar al statico

    def __str__(self):
        return "papa"

    def __add__(self, other: "CuentaCorriente"): #el :"CuentaCorriente" indica que se deberia pasar esa clase mas no lo verifica
        return self.saldo+other.saldo

c1=CuentaCorriente(20,"per")
print(c1.__str__())
print(str(c1))
print(c1)

print(c1.__add__(c1))
print(c1+c1)
