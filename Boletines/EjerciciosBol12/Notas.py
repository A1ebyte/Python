"""Queremos implementar una clase para gestionar una aplicación de gestión de notas. Cada
nota tendrá cuatro elementos: título, descripción, color (debe de se amarillo, verde, blanco o
cyan para una futura implementación en un entorno gráfico) y fecha de creación.
Necesitamos, además, añadir los siguientes métodos: crearNota, eliminarNota y listarNota
No hace falta que hagas entradas por teclado: crea los métodos y pruébalos llamándolos
directamente.
Trata de que la visualización de la nota sea lo mas agradable posible en pantalla usando
fstrings"""
from enum import Enum
from datetime import datetime


class ColorOpciones(Enum):
    AMARILLO = "amarillo"
    VERDE = "verde"
    BLANCO = "blanco"
    CYAN = "cyan"


class Nota:
    def __init__(self, titulo, descripcion, color: ColorOpciones):
        if not isinstance(color, ColorOpciones):
            raise ValueError("Color no válido. Debe ser una opción de ColorOpciones")

        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__color = color
        self.__fecha = datetime.now()

    def __str__(self):
        return (
            f"\n{'='*40}\n"
            f"📝 TÍTULO : {self.__titulo}\n"
            f"📄 DESCRIPCIÓN : {self.__descripcion}\n"
            f"🎨 COLOR : {self.__color.value.capitalize()}\n"
            f"📅 FECHA : {self.__fecha.strftime('%d/%m/%Y')}\n"
            f"{'='*40}"
        )

class GestorNotas:
    def __init__(self):
        self.notas = []

    def crearNota(self, titulo, descripcion, color):
        try:
            nota = Nota(titulo, descripcion, color)
        except ValueError as error:
            print(f'Error no se ha podido crear la nota.\nRazon: {error}')
        else:
            self.notas.append(nota)

    def eliminarNota(self, titulo):
        self.notas = [notas for notas in self.notas if notas._Nota__titulo != titulo]

    def listarNotas(self):
        if not self.notas:
            print("\nNo hay notas disponibles.")
        for nota in self.notas:
            print(nota)


gestor = GestorNotas()

gestor.crearNota(
    "Examen Python",
    "Repasar clases y enums",
    ColorOpciones.VERDE
)

gestor.crearNota(
    "Compra",
    "Comprar leche y pan",
    "dsdsd"
)

gestor.listarNotas()

gestor.eliminarNota("Examen Python")

gestor.listarNotas()
