class Inmueble:
    def __init__(self, identificadorInmobiliario, area, direccion):
        self.identificadorInmobiliario = identificadorInmobiliario
        self.area = area
        self.direccion = direccion
        self.precioVenta = 0.0

    def calcularPrecioVenta(self, valorArea):
        self.precioVenta = self.area * valorArea
        return self.precioVenta

    def imprimir(self):
        print("Identificador inmobiliario =", self.identificadorInmobiliario)
        print("Area =", self.area)
        print("Dirección =", self.direccion)
        print("Precio de venta = $", self.precioVenta)


class InmuebleVivienda(Inmueble):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos):
        super().__init__(identificadorInmobiliario, area, direccion)
        self.numeroHabitaciones = numeroHabitaciones
        self.numeroBanos = numeroBanos

    def imprimir(self):
        super().imprimir()
        print("Número de habitaciones =", self.numeroHabitaciones)
        print("Número de baños =", self.numeroBanos)


class Casa(InmuebleVivienda):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos)
        self.numeroPisos = numeroPisos

    def imprimir(self):
        super().imprimir()
        print("Número de pisos =", self.numeroPisos)


class Apartamento(InmuebleVivienda):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos)

    def imprimir(self):
        super().imprimir()


class CasaRural(Casa):
    valorArea = 1500000

    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos, distanciaCabera, altitud):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos)
        self.distanciaCabera = distanciaCabera
        self.altitud = altitud

    def imprimir(self):
        super().imprimir()
        print("Distancia a la cabecera municipal = ", self.distanciaCabera, " km.")
        print("Altitud sobre el nivel del mar = ", self.altitud, " metros.")


class CasaUrbana(Casa):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos)

    def imprimir(self):
        super().imprimir()


class ApartamentoFamiliar(Apartamento):
    valorArea = 2000000

    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, valorAdministracion):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos)
        self.valorAdministracion = valorAdministracion

    def imprimir(self):
        super().imprimir()
        print("Valor de la administración = $", self.valorAdministracion)


class Apartaestudio(Apartamento):
    valorArea = 1500000

    def __init__(self, identificadorInmobiliario, area, direccion):
        super().__init__(identificadorInmobiliario, area, direccion, 1, 1)

    def imprimir(self):
        super().imprimir()


class CasaConjuntoCerrado(Casa):
    valorArea = 2500000

    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos, valorAdministracion, tienePiscina, tieneCamposDeportivos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos)
        self.valorAdministracion = valorAdministracion
        self.tienePiscina = tienePiscina
        self.tieneCamposDeportivos = tieneCamposDeportivos

    def imprimir(self):
        super().imprimir()
        print("Valor de la administración =", self.valorAdministracion)
        print("Tiene piscina? =", self.tienePiscina)
        print("Tiene campos deportivos? =", self.tieneCamposDeportivos)


class CasaIndependiente(Casa):
    valorArea = 3000000

    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos, numeroPisos)

    def imprimir(self):
        super().imprimir()


class Local(Inmueble):
    class Tipo:
        INTERNO = "INTERNO"
        CALLE = "CALLE"

    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal):
        super().__init__(identificadorInmobiliario, area, direccion)
        self.tipoLocal = tipoLocal

    def imprimir(self):
        super().imprimir()
        print("Tipo de local =", self.tipoLocal)


class LocalComercial(Local):
    valorArea = 3000000

    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal, centroComercial):
        super().__init__(identificadorInmobiliario, area, direccion, tipoLocal)
        self.centroComercial = centroComercial

    def imprimir(self):
        super().imprimir()
        print("Centro comercial =", self.centroComercial)


class Oficina(Local):
    valorArea = 3500000

    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal, esGobierno):
        super().__init__(identificadorInmobiliario, area, direccion, tipoLocal)
        self.esGobierno = esGobierno

    def imprimir(self):
        super().imprimir()
        print("Es oficina gubernamental =", self.esGobierno)


def main():
    apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
    print("Datos apartamento")
    apto1.calcularPrecioVenta(ApartamentoFamiliar.valorArea)
    apto1.imprimir()

    print("\nDatos apartaestudio")
    aptestudio1 = Apartaestudio(12354, 50, "Avenida Caracas 30-15")
    aptestudio1.calcularPrecioVenta(Apartaestudio.valorArea)
    aptestudio1.imprimir()


if __name__ == "__main__":
    main()
  
