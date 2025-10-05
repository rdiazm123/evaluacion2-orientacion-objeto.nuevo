
from datetime import datetime

class Vehiculo:
    def __init__(self, id_vehiculo, patente, peso_kg):
        self._id_vehiculo = id_vehiculo
        self._patente = patente
        self._peso_kg = peso_kg
        self._estado = "habilitado"
        self.historial_eventos = []

    @property
    def peso_kg(self):
        return self._peso_kg

    @property
    def estado(self):
        return self._estado

    def actualizar_peso(self, nuevo_peso, motivo):
        if self.estado != 'habilitado':
            raise ValueError("No se puede modificar el peso si el vehículo está inhabilitado.")
        anterior = self._peso_kg
        self._peso_kg = nuevo_peso
        self._registrar_evento("peso_kg", anterior, nuevo_peso, motivo)

    def habilitar(self, motivo):
        anterior = self._estado
        self._estado = "habilitado"
        self._registrar_evento("estado", anterior, self._estado, motivo)

    def inhabilitar(self, motivo):
        anterior = self._estado
        self._estado = "inhabilitado"
        self._registrar_evento("estado", anterior, self._estado, motivo)

    def _registrar_evento(self, campo, anterior, nuevo, motivo):
        evento = {
            "fecha": datetime.now(),
            "campo": campo,
            "anterior": anterior,
            "nuevo": nuevo,
            "motivo": motivo
        }
        self.historial_eventos.append(evento)
    @property
    def id_vehiculo(self):
        return self._id_vehiculo    
    @property
    def patente(self):
        return self._patente
    def consultar_ficha(self):
        return {
            "id_vehiculo": self.id_vehiculo,
            "patente": self.patente,
            "peso_kg": self.peso_kg,
            "estado": self.estado,
            "historial_eventos": self.historial_eventos
        }
# Fin de vehiculo.py