class Persona:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion

    def getNombre(self) -> str:
        return self.nombre

    def getDireccion(self) -> str:
        return self.direccion

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def setDireccion(self, direccion: str):
        self.direccion = direccion


class Estudiante(Persona):
    def __init__(self, nombre: str, direccion: str, carrera: str, semestre: int):
        super().__init__(nombre, direccion)
        self.carrera = carrera
        self.semestre = semestre

    def getCarrera(self) -> str:
        return self.carrera

    def getSemestre(self) -> int:
        return self.semestre

    def setCarrera(self, carrera: str):
        self.carrera = carrera

    def setSemestre(self, semestre: int):
        self.semestre = semestre


class Profesor(Persona):
    def __init__(self, nombre: str, direccion: str, departamento: str, categoria: str):
        super().__init__(nombre, direccion)
        self.departamento = departamento
        self.categoria = categoria

    def getDepartamento(self) -> str:
        return self.departamento

    def getCategoria(self) -> str:
        return self.categoria

    def setDepartamento(self, departamento: str):
        self.departamento = departamento

    def setCategoria(self, categoria: str):
        self.categoria = categoria


if __name__ == "__main__":
    estudiante = Estudiante("Juan Perez", "Calle X 123", "Ingeniería", 4)
    profesor = Profesor("Maria Lopez", "Avenida Primavera 456", "Ciencias", "Asociado")

    print(f"Estudiante: {estudiante.getNombre()}, Carrera: {estudiante.getCarrera()}, Semestre: {estudiante.getSemestre()}")
    print(f"Profesor: {profesor.getNombre()}, Departamento: {profesor.getDepartamento()}, Categoría: {profesor.getCategoria()}")
