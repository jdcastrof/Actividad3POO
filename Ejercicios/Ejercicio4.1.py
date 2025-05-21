class Cuenta:
    def __init__(self, saldo: float, tasaAnual: float):
        self._saldo = saldo
        self._numeroConsignaciones = 0
        self._numeroRetiros = 0
        self._tasaAnual = tasaAnual
        self._comisionMensual = 0

    def consignar(self, cantidad: float):
        self._saldo = self._saldo + cantidad
        self._numeroConsignaciones = self._numeroConsignaciones + 1

    def retirar(self, cantidad: float):
        nuevoSaldo = self._saldo - cantidad
        if nuevoSaldo >= 0:
            self._saldo = self._saldo - cantidad
            self._numeroRetiros = self._numeroRetiros + 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calcularInteres(self):
        tasaMensual = self._tasaAnual / 12
        interesMensual = self._saldo * tasaMensual
        self._saldo = self._saldo + interesMensual

    def extractoMensual(self):
        self._saldo = self._saldo - self._comisionMensual
        self.calcularInteres()


class CuentaAhorros(Cuenta):
    def __init__(self, saldo: float, tasa: float):
        super().__init__(saldo, tasa)
        if saldo<10000:
          self._activa=False
        else:
          self._activa = True

    def retirar(self, cantidad: float):
        if self._activa:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        if self._activa:
            super().consignar(cantidad)

    def extractoMensual(self):
        if self._numeroRetiros > 4:
            self._comisionMensual = self._comisionMensual + (self._numeroRetiros - 4) * 1000
        super().extractoMensual()
        if self._saldo<10000:
            self._activa = False

    def imprimir(self):
        print(f"Saldo = $ {self._saldo}")
        print(f"Comisión mensual = ${self._comisionMensual}")
        print(f"Número de transacciones = {self._numeroConsignaciones + self._numeroRetiros}\n")


class CuentaCorriente(Cuenta):
    def __init__(self, saldo: float, tasa: float):
        super().__init__(saldo, tasa)
        self._sobregiro = 0

    def retirar(self, cantidad: float):
        resultado = self._saldo - cantidad
        if resultado < 0:
            self._sobregiro = self._sobregiro - resultado
            self._saldo = 0
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        residuo = self._sobregiro - cantidad
        if self._sobregiro > 0:
            if residuo > 0:
                self._sobregiro = 0
                self._saldo = residuo
            else:
                self._sobregiro = residuo * (-1)
                self._saldo = 0
        else:
            super().consignar(cantidad)

    def extractoMensual(self):
        super().extractoMensual()

    def imprimir(self):
        print(f"Saldo = ${self._saldo}")
        print(f"Cargo mensual = ${self._comisionMensual}")
        print(f"Número de transacciones = {self._numeroConsignaciones + self._numeroRetiros}")
        print(f"Valor de sobregiro = ${self._sobregiro}\n")


if __name__ == "__main__":
    print("Cuenta de ahorros")
    saldoInicialAhorros = float(input("Ingrese saldo inicial = $"))
    tasaAhorros = float(input("Ingrese tasa de interés = "))

    cuenta1 = CuentaAhorros(saldoInicialAhorros, tasaAhorros)

    cantidadDepositar = float(input("Ingresar cantidad a consignar: $"))
    cuenta1.consignar(cantidadDepositar)

    cantidadRetirar = float(input("Ingresar cantidad a retirar: $"))
    cuenta1.retirar(cantidadRetirar)

    cuenta1.extractoMensual()
    cuenta1.imprimir()
