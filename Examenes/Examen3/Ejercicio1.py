class Sucursal:
    codigoBanco="ES68 1234"

    def __init__(self,direccion,provincia,codigo):
        self.__direccion=direccion
        self.__provincia=provincia
        self.__codigo=codigo
        self.__cuentas=set()

    @property
    def codigo(self):
        return self.__codigo

    @property
    def provincia(self):
        return self.__provincia

    def mostrarCuentas(self):
        total=0
        print(f"Cuentas de la sucursal {self.__codigo} ({self.__provincia})")
        for cuenta in self.__cuentas:
            total += cuenta.saldo
            print(Sucursal.codigoBanco, self.__codigo, cuenta.codigo, "-", f"{cuenta.saldo:.2f}")
        print(f"Saldo total: {total: .2f}")

    def agregarCuentas(self,cuenta):
        self.__cuentas.add(cuenta)

class Cliente:
    def __init__(self,nombre,apellidos,nif,tlf,sucursalAlta):
        self.__nombre=nombre
        self.__apellidos=apellidos
        self.__nif=nif
        self.__tlf=tlf
        self.__sucursalAlta=sucursalAlta
        self.__cuentas=[]

    @property
    def cuentas(self):
        return self.__cuentas

    def mostrarCuentas(self):
        total=0
        print(f"{self.__nombre} {self.__apellidos}. Cliente de la sucursal {self.__sucursalAlta.codigo} ({self.__sucursalAlta.provincia})")
        for cuenta in self.__cuentas:
            if cuenta.titular2 is not None:
                print(f"Segundo Titular: {cuenta.titular2.__nombre} {cuenta.titular2.__apellidos}:",Sucursal.codigoBanco,
                      cuenta.sucursal.codigo, cuenta.codigo, "-", f"{cuenta.saldo:.2f}")
            else:
                print(Sucursal.codigoBanco, cuenta.sucursal.codigo, cuenta.codigo, "-", f"{cuenta.saldo:.2f}")
            total+=cuenta.saldo
        print(f"Saldo total: {total: .2f}")

    def agregarCuentas(self, cuenta):
        self.__cuentas.append(cuenta)

class Cuenta:
    def __init__(self,codigo,saldo,titular1,sucursal,titular2=None):
        self.__codigo=codigo
        self.__saldo=saldo
        self.__titular1=titular1
        self.__sucursal=sucursal
        self.__titular2=titular2
        self.__titular1.agregarCuentas(self)
        if self.__titular2 is not None:
            self.__titular2.agregarCuentas(self)
        self.sucursal.agregarCuentas(self)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def codigo(self):
        return self.__codigo

    @property
    def sucursal(self):
        return self.__sucursal

    @property
    def titular2(self):
        return self.__titular2

madrid = Sucursal("dsadasdas","Madrid","0055")
p1 = Cliente("Pepe","Aguilar","y6324022F","611058826",madrid)
p2 = Cliente("Javier","Estrachi","y6324022F","611058826",madrid)
c1 = Cuenta("4444 5555 6666",46,p1,madrid)
c2 = Cuenta("6666 5555 6666",2,p1,madrid)
c3 = Cuenta("3333 1111 2222",135.2,p1,madrid,p2)

madrid.mostrarCuentas()
p1.mostrarCuentas()