"""
 Queremos implementar una clase para gestionar nuestra colección de mangas con las
siguientes características:
- Por cada manga guardaremos el nombre del mangaka (autor) el título de la colección (en
japonés, obligatorio y en español, opcional), el género prinicpal (shonen, shojo, seinen, josei,
kodomo, yuri, spokon, isekai y hentai) y el último número publicado en la colección. Crea
getters para todos ellos y setter para el título en castellano (por si originalmente no lo
sabemos y luego lo queremos añadir) y para el número por el que va la colección.
- Queremos, además, poder actualizar los números que tenemos y saber que números nos
faltan. Para ello crearemos dos métodos: uno que nos permitirá introducir los números que
vamos comprando (permitiendo una entrada variable de argumentos para cuando
compramos mas de uno a la vez) y otro que nos diga que números nos faltan para completar
la colección.
- Si cuando introducimos los números que compramos resulta que ya tenemos alguno de
ellos repetido debería de advertirnos
- También necesitaremos una funcion que nos permita eliminar un número (lo hemos perdido,
etc.). Si tratamos de eliminar un número que no tenemos debería de advertírsenos
"""
from enum import Enum

class MangaGenero(Enum):
    shonen="Shonen"
    shojo="Shojo"
    seinen="Seinen"
    josei="Josei"
    kodomo="Kodomo"
    yuri="Yuri"
    spokon="Spokon"
    isekai="Isekai"
    hentai="Hentai"


class ColeccionManga:
    def __init__(self, autor,titulo,genero,ultimaPublicacion,*tomos,tituloCastellano=None):
        if not isinstance(genero,MangaGenero): raise ValueError("Genero no valido.")
        self.__tomos=list(tomos)
        self.__autor = autor
        self.__genero = genero
        self.__titulo=titulo
        self.__ultimaPublicacion = ultimaPublicacion
        self.__tituloCastellano = tituloCastellano

    # region Properties
    @property
    def autor(self):
        return self.__autor

    @property
    def genero(self):
            return self.__genero

    @property
    def titulo(self):
            return self.__titulo

    @property
    def tomos(self):
            return self.__tomos

    @property
    def ultimaPublicacion(self):
        return self.__ultimaPublicacion
    @ultimaPublicacion.setter
    def ultimaPublicacion(self,valor):
        self.__ultimaPublicacion = valor

    @property
    def tituloCastellano(self):
        return self.__tituloCastellano
    @tituloCastellano.setter
    def tituloCastellano(self,valor):
        self.__tituloCastellano = valor
    # endregion0

    #region Funciones
    def cuantosFaltanParaCompletar(self):
        if self.evolucion is None:   #self.__evolucion==None:
            print("No evoluciono, ya soy todo poderoso")
            return self
        return self.evolucion

    def agregarAColeccion(self):
        tipos_str = ", ".join(t.value for t in self.tipos)
        return (f"Codigo: {str(self.codigo).zfill(3)}\nNombre: {self.nombre}\nTipo: {tipos_str}\n"
                f"{'' if self.evolucion is None else f"Evolucion: {self.evolucion.nombre}\n"}HP: {self.Hp}\n")

    #endregion

manga=ColeccionManga("yuyo ito","Uzumaki",MangaGenero.shojo,6,1,2,4)
