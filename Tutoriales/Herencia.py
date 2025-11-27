class Padre:
    def __init__(self):
        self._titulo="Papa"

    def mostrar(self):
        print(self._titulo,"-P-")

class Madre:
    def __init__(self):
        self._titulo="Mama"

    def mostrar(self):
        print(self._titulo,"-M-")

class Hijo(Padre,Madre):
    def __init__(self):
        self._titulo="Hijo"

    def mostrar(self,msj=""):
        super().mostrar()  #agarra por defecto el de la izquierda/primero
        Madre.mostrar(self)  #para llamar otro que no sea el de izquierda/primero
        print(msj)

object1=Padre()
object1.mostrar()
object1=Madre()
object1.mostrar()
object2=Hijo()
object2.mostrar("holapapa")