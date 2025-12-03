"""
Queremos implementar una clase para gestionar un juego de Pokemon con las siguientes
características:
- Los atributos base que manejaremos serán código, nombre y tipo
- Sólo trabajaremos con pokemon de primera generación por lo que el código estará entre el
1 y el 151, ambos incluidos
- Los posibles tipos son Normal, Agua, Fuego, Planta, Volador, Lucha, Veneno, Eléctrico,
Tierra, Roca, Psíquico, Hielo, Bicho, Fantasma y Dragón.
- Cada pokemon debe de ser de un tipo, pero podría ser de dos. Nunca más
- No necesitamos setters (ya que un pokemon una vez creado no puede modificar sus
características) pero si getters apropiados para todas ellas
- Además, crearemos una función que se llame evolución que permitirá que un pokemon
evolucione en otro diferente. Para ello si un pokemon puede evolucionar en otro debe de
tener de alguna forma una referencia al pokemon en el que evoluciona.
"""
import random

from sympy import false


class Pokemon:
    def __init__(self,nombre,codigo,evolucion=None):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__evolucion=evolucion
        self.__Hp = random.randint(50, 100)

#region Properties
    @property
    def evolucion(self):
        return self.__evolucion
    @property
    def nombre(self):
        return self.__nombre
    @property
    def codigo(self):
        return self.__codigo
    @property
    def Hp(self):
        return self.__Hp
#endregion

#region Funciones
    def evoluciona(self):
        if self.evolucion is None:   #self.__evolucion==None:
            print("No evoluciono, ya soy todo poderoso")
            return self
        return self.evolucion

    def __str__(self):
        return (f"Codigo: {str(self.codigo).zfill(3)}\nNombre: {self.nombre}\n"
                f"{'' if self.evolucion is None else f"Evolucion: {self.evolucion.nombre}\n"}HP: {self.Hp}\n")

    def ataca(self,adversario):
        if self.checkHp():
            atk=random.randint(25,75)
            print(f"{self.nombre}: Ataco a {adversario.nombre} haciendo {atk} de daño")
            adversario.reciboDaño(atk)

    def reciboDaño(self,daño):
        if self.checkHp():
            self.__Hp=0 if self.Hp-daño<=0 else self.Hp-daño
            if self.Hp == 0:
                print(f"{self.nombre}: He sido derrotado")

    def checkHp(self):
        if self.Hp<=0:
            return False
        return True
    #endregion

Poke3=Pokemon("Charizard",3)
Poke2=Pokemon("Charmeleon",2,Poke3)
Poke1=Pokemon("Charmander",1,Poke2)

print(Poke1)
print(Poke2)
print(Poke3)

"""Poke1=Poke1.evoluciona()
print(Poke1)
Poke3=Poke3.evoluciona()
print(Poke3)"""

while Poke1.checkHp() and Poke2.checkHp():
    Poke1.ataca(Poke2)
    Poke2.ataca(Poke1)