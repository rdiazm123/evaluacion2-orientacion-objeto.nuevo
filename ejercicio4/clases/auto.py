from .vehiculo import Vehiculo
from datetime import datetime

class Auto(Vehiculo):
    def __init__(self, id_vehiculo, patente, peso_kg, asientos_totales):
        super().__init__(id_vehiculo, patente, peso_kg)
        if asientos_totales < 1:
            raise ValueError("Debe tener al menos 1 asiento.")
        self._asientos_totales = asientos_totales
        self._ocupantes_actuales = 0
        self._eventos_ocupacion = []

    @property
    def asientos_totales(self):
        return self._asientos_totales

    @property
    def ocupantes_actuales(self):
        return self._ocupantes_actuales

    @property
    def eventos_ocupacion(self):
        return self._eventos_ocupacion.copy()

    def subir_personas(self, n):
        if self.estado != 'habilitado':
            raise ValueError("No se puede subir personas en un vehículo inhabilitado.")
        if n < 1 or self._ocupantes_actuales + n > self._asientos_totales:
            raise ValueError("Cantidad inválida o excede capacidad.")
        antes = self._ocupantes_actuales
        self._ocupantes_actuales += n
        self._registrar_ocupacion("subida", n, antes, self._ocupantes_actuales)

    def bajar_personas(self, n):
        if self.estado != 'habilitado':
            raise ValueError("No se puede bajar personas en un vehículo inhabilitado.")
        if n < 1 or self._ocupantes_actuales - n < 0:
            raise ValueError("Cantidad inválida o negativa.")
        antes = self._ocupantes_actuales
        self._ocupantes_actuales -= n
        self._registrar_ocupacion("bajada", n, antes, self._ocupantes_actuales)

    def reconfigurar_asientos(self, nuevo_total, motivo):
        if nuevo_total < 1 or nuevo_total < self._ocupantes_actuales:
            raise ValueError("Nuevo total inválido o menor que ocupantes actuales.")
        anterior = self._asientos_totales
        self._asientos_totales = nuevo_total
        self._registrar_evento("asientos_totales", anterior, nuevo_total, motivo)

    def vaciar_auto(self, motivo):
        antes = self._ocupantes_actuales
        self._ocupantes_actuales = 0
        self._registrar_ocupacion("vaciado", antes, antes, 0)
        self._registrar_evento("ocupantes_actuales", antes, 0, motivo)

    def consultar_ocupacion(self):
        libres = self._asientos_totales - self._ocupantes_actuales
        tasa = round((self._ocupantes_actuales / self._asientos_totales) * 100, 2)
        return {
            "ocupantes": self._ocupantes_actuales,
            "libres": libres,
            "tasa_ocupacion": f"{tasa}%"
        }

    def _registrar_ocupacion(self, accion, cantidad, antes, despues):
        self._eventos_ocupacion.append({
            "fecha": datetime.now(),
            "accion": accion,
            "cantidad": cantidad,
            "antes": antes,
            "despues": despues
        })
        
    def _registrar_evento(self, atributo, antes, despues, motivo):
        self._eventos_ocupacion.append({
            "fecha": datetime.now(),
            "atributo": atributo,
            "antes": antes,
            "despues": despues,
            "motivo": motivo
        })
        