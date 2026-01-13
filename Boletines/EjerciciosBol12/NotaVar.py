"""Modifica el programa de forma que haya dos tipos de notas: una normal (como las descritas
anteriormente) y otra urgente que será siempre en rojo y que, cuando las listemos,
aparecerán siempre encima de las otras. Haz las modificaciones de forma que tengas una
clase abstracta de la que deriven los dos tipos de notas. Las notas urgentes, además,
pediran confirmación por teclado cuando tratemos de eliminarlas y se visualizaran con algún
detalle que las distinga de las normales."""

from enum import Enum
from datetime import datetime
from abc import abstractmethod, ABCMeta
from pickle import NONE


class ColorOpciones(Enum):
    AMARILLO = "amarillo"
    VERDE = "verde"
    BLANCO = "blanco"
    CYAN = "cyan"
    ROJO = "rojo"

class Nota(metaclass=ABCMeta):
    def crear(self, titulo, descripcion, color: ColorOpciones):
        if not isinstance(color, ColorOpciones):
            raise ValueError("Color no válido. Debe ser una opción de ColorOpciones")
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__color = color
        self.__fecha = datetime.now()

    @abstractmethod
    def __str__(self):
        return (
            f"TÍTULO : {self.__titulo}\n"
            f"DESCRIPCIÓN : {self.__descripcion}\n"
            f"COLOR : {self.__color.value.capitalize()}\n"
            f"FECHA : {self.__fecha.strftime('%d/%m/%Y')}"
        )

class NotaUrgente(Nota):
    def __init__(self, titulo, descripcion):
        super().crear(titulo, descripcion, ColorOpciones.ROJO)

    def __str__(self):
        return f"\n{'=' * 40}\n" + f"!!!{"URGENTE":^34}!!!\n" + super().__str__() + f"\n{'=' * 40}"


class NotaNormal(Nota):
    def __init__(self, titulo, descripcion, color):
        super().crear(titulo, descripcion, color)

    def __str__(self):
        return f"\n{'=' * 40}\n" + super().__str__() + f"\n{'=' * 40}"


class GestorNotas:
    def __init__(self):
        self.notas = []

    def crearNotaNormal(self, titulo, descripcion, color):
        try:
            nota = NotaNormal(titulo, descripcion, color)
        except ValueError as error:
            print(f'Error no se ha podido crear la nota.\nRazon: {error}')
        else:
            self.notas.append(nota)

    def crearNotaUrgente(self, titulo, descripcion):
        try:
            nota = NotaUrgente(titulo, descripcion)
        except ValueError as error:
            print(f'Error no se ha podido crear la nota.\nRazon: {error}')
        else:
            self.notas.append(nota)

    def eliminarNota(self, titulo):
        self.notas = [notas for notas in self.notas if notas._Nota__titulo != titulo]

    def listarNotas(self):
        if not self.notas:
            print("\nNo hay notas disponibles.")
            return

        urgentes = [nota for nota in self.notas if isinstance(nota, NotaUrgente)]
        normales = [nota for nota in self.notas if isinstance(nota, NotaNormal)]

        if urgentes:
            for nota in urgentes:
                print(nota)
        if normales:
            for nota in normales:
                print(nota)

        #aqui no esta ordenado
        #print("\n".join(str(nota) for nota in self.notas))

gestor = GestorNotas()

gestor.crearNotaNormal(
    "Examen Python",
    "Repasar clases y enums",
    ColorOpciones.VERDE
)

gestor.crearNotaNormal(
    "Examen Java",
    "Repasar clases y enums",
    ColorOpciones.BLANCO
)

gestor.crearNotaNormal(
    "Examen Pepe",
    "Repasar clases y enums",
    ColorOpciones.CYAN
)

gestor.crearNotaUrgente(
    "Examen Pepe",
    "Repasar clases y enums"
)

gestor.crearNotaNormal(
    "Compra",
    "Comprar leche y pan",
    "dsdsd"
)

gestor.listarNotas()

gestor.eliminarNota("Examen Python")

gestor.listarNotas()


