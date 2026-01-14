class Biblioteca:
    def __init__(self):
        self._libros = {}

    @property
    def libros(self):
        return self._libros

    def agregarLibro(self, ejemplar):
        if ejemplar.codigo in self.libros:
            print("Añadiendo Ejemplar a la biblioteca")
            self.libros[ejemplar.codigo]["stock"]=self.libros[ejemplar.codigo].get("stock")+1
            print(ejemplar)
            print(f"Ahora hay {self.libros[ejemplar.codigo]["stock"]} ejemplares disponibles")
        else:
            print("Añadiendo a la biblioteca")
            print(ejemplar)
            self.libros[ejemplar.codigo] = {"libro": ejemplar, "stock": 1, "prestados": 0, "cantidadPrestados": 0}

class Libro:
    def __init__(self, codigo, titulo, autor, numPaginas, formato="papel"):
        self._autor = autor
        self._titulo = titulo
        self._codigo = codigo
        self._numPaginas = numPaginas
        self._formato = formato

    def __str__(self):
        return f"{self._autor} - {self._titulo} - {self._formato}"

    @property
    def codigo(self):
        return self._codigo

class Comic(Libro):
    def __init__(self, codigo, titulo, autor, numPaginas, color):
        super().__init__(codigo, titulo, autor,numPaginas)
        self.__color = color

    def __str__(self):
        return f"{self._autor} - {self._titulo} - {self.__color}"

biblio=Biblioteca()
pepe=Comic("123456","patata","patete",42,"BYW")
pepe2=Libro("333333","patata","patete",42,"papel")
biblio.agregarLibro(pepe)
biblio.agregarLibro(pepe2)
biblio.agregarLibro(pepe)