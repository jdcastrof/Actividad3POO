from enum import Enum

class RazaPerroPequeño(Enum):
    CANICHE = "Caniche"
    YORKSHIRE_TERRIER = "Yorkshire Terrier"
    SCHNAUZER = "Schnauzer"
    CHIHUAHUA = "Chihuahua"


class RazaPerroMediano(Enum):
    COLLIE = "Collie"
    DALMATA = "Dálmata"
    BULLDOG = "Bulldog"
    GALGO = "Galgo"
    SABUESO = "Sabueso"


class RazaPerroGrande(Enum):
    PASTOR_ALEMAN = "Pastor Alemán"
    DOBERMAN = "Dóberman"
    ROTTWEILER = "Rottweiler"


class RazaGatoSinPelo(Enum):
    ESFINGE = "Esfinge"
    ELFO = "Elfo"
    DONSKOY = "Donskoy"


class RazaGatoPeloLargo(Enum):
    ANGORA = "Angora"
    HIMALAYO = "Himalayo"
    BALINES = "Balinés"
    SOMALI = "Somalí"


class RazaGatoPeloCorto(Enum):
    AZUL_RUSO = "Azul Ruso"
    BRITANICO = "Británico"
    MANX = "Manx"
    DEVON_REX = "Devon Rex"


class Mascota:
    def __init__(self, nombre: str, edad: int, color: str):
        self.nombre = nombre
        self.edad = edad
        self.color = color


class Perro(Mascota):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde

    @staticmethod
    def sonido():
        print("Los perros ladran.")


class PerroPequeño(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool, raza: RazaPerroPequeño):
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza


class PerroMediano(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool, raza: RazaPerroMediano):
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza


class PerroGrande(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool, raza: RazaPerroGrande):
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza


class Gato(Mascota):
    def __init__(self, nombre: str, edad: int, color: str, alturaSalto: float, longitudSalto: float):
        super().__init__(nombre, edad, color)
        self.alturaSalto = alturaSalto
        self.longitudSalto = longitudSalto

    @staticmethod
    def sonido():
        print("Los gatos maúllan y ronronean.")


class GatoSinPelo(Gato):
    def __init__(self, nombre: str, edad: int, color: str, alturaSalto: float, longitudSalto: float, raza: RazaGatoSinPelo):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
        self.raza = raza


class GatoPeloLargo(Gato):
    def __init__(self, nombre: str, edad: int, color: str, alturaSalto: float, longitudSalto: float, raza: RazaGatoPeloLargo):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
        self.raza = raza


class GatoPeloCorto(Gato):
    def __init__(self, nombre: str, edad: int, color: str, alturaSalto: float, longitudSalto: float, raza: RazaGatoPeloCorto):
        super().__init__(nombre, edad, color, alturaSalto, longitudSalto)
        self.raza = raza


if __name__ == "__main__":
    perro1 = PerroPequeño("Max", 2, "Marrón", 5.0, False, RazaPerroPequeño.CANICHE)
    perro2 = PerroMediano("Bolt", 3, "Blanco", 15.0, True, RazaPerroMediano.DALMATA)
    
    gato1 = GatoSinPelo("Sphinx", 1, "Beige", 1.5, 3.0, RazaGatoSinPelo.ESFINGE)
    gato2 = GatoPeloLargo("Nube", 4, "Gris", 2.0, 2.5, RazaGatoPeloLargo.ANGORA)

    Perro.sonido()
    Gato.sonido()
  
