from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, ciclo):
        super().__init__(nombre, apellido)
        self.edad = edad
        self.mayor_edad = edad >= 18
        self.ciclo = ciclo
        self.grupo = None

    def __str__(self):
        return f"{self.nombre_completo()} - {self.edad} años"

class Profesor(Persona):
    DEPARTAMENTOS = ("Informática", "Empresa", "Inglés")

    def __init__(self, nombre, apellido, departamento):
        if departamento not in self.DEPARTAMENTOS:
            raise ValueError("Departamento no válido")

        super().__init__(nombre, apellido)
        self.departamento = departamento
        self.grupo_tutor = None

    def __str__(self):
        return f"{self.nombre_completo()} ({self.departamento})"

class Modulo:
    def __init__(self, nombre, curso, horas_semanales, optativo):
        self.nombre = nombre
        self.curso = curso          # 1 o 2
        self.horas_semanales = horas_semanales
        self.optativo = optativo

    def __str__(self):
        return f"{self.nombre} - {self.horas_semanales}h/semana"

class Ciclo:
    def __init__(self, nombre, grado_superior):
        self.nombre = nombre
        self.grado_superior = grado_superior
        self.modulos = []

    def añadir_modulo(self, modulo):
        self.modulos.append(modulo)

    def __str__(self):
        tipo = "Grado Superior" if self.grado_superior else "Grado Medio"
        return f"{self.nombre} ({tipo})"

class Grupo:
    def __init__(self, nombre, ciclo, curso, tutor=None):
        self.nombre = nombre
        self.ciclo = ciclo
        self.curso = curso          # 1 o 2
        self.tutor = tutor
        self.alumnos = []

        if tutor:
            tutor.grupo_tutor = self

    # Añadir alumno al grupo
    def añadir_alumno(self, alumno):
        self.alumnos.append(alumno)
        alumno.grupo = self

    # Eliminar alumno del grupo
    def eliminar_alumno(self, alumno):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)
            alumno.grupo = None

    # Listar toda la información del grupo
    def mostrar_informacion(self):
        print(f"Grupo: {self.nombre}")
        print(f"Ciclo: {self.ciclo}")
        print(f"Curso: {self.curso}")
        print(f"Tutor: {self.tutor if self.tutor else 'Sin tutor'}")
        print(f"Número de alumnos: {len(self.alumnos)}")

        print("\nAlumnos:")
        for alumno in self.alumnos:
            print(f" - {alumno}")

        print("\nMódulos del ciclo:")
        for modulo in self.ciclo.modulos:
            print(f" - {modulo}")

# Crear ciclo
dam = Ciclo("DAM", True)
dam.añadir_modulo(Modulo("Programación", 1, 8, False))
dam.añadir_modulo(Modulo("Bases de Datos", 1, 6, False))

# Crear profesor
profesor = Profesor("Ana", "López", "Informática")

# Crear grupo (sin alumnos inicialmente)
dam1 = Grupo("DAM1", dam, 1, profesor)

# Crear alumnos
alumno1 = Alumno("Juan", "Pérez", 19, dam)
alumno2 = Alumno("Laura", "Gómez", 17, dam)

# Añadir alumnos al grupo
dam1.añadir_alumno(alumno1)
dam1.añadir_alumno(alumno2)

# Mostrar información del grupo
dam1.mostrar_informacion()
