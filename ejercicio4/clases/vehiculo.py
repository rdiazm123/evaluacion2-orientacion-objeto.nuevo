# from datetime import datetime

# class Vehiculo:
#     def __init__(self, id_vehiculo, patente, peso_kg):
#         self.id_vehiculo = id_vehiculo
#         self._patente = patente
#         self._peso_kg = None
#         self.peso_kg = peso_kg
#         self.estado = 'habilitado'
#         self._historial_eventos = []

#     @property
#     def patente(self):
#         return self._patente

#     @property
#     def peso_kg(self):
#         return self._peso_kg

#     @peso_kg.setter
#     def peso_kg(self, value):
#         if value <= 0:
#             raise ValueError("El peso debe ser mayor que 0.")
#         self._peso_kg = value

#     def actualizar_peso(self, nuevo_peso):
#         if self.estado != 'habilitado':
#             raise ValueError("No se puede actualizar el peso de un vehículo inhabilitado.")
#         anterior = self.peso_kg
#         self.peso_kg = nuevo_peso
#         self._registrar_evento("peso_kg", anterior, nuevo_peso)

#     def habilitar(self, motivo):
#         self.estado = 'habilitado'
#         self._registrar_evento("estado", "inhabilitado", "habilitado", motivo)

#     def inhabilitar(self, motivo):
#         self.estado = 'inhabilitado'
#         self._registrar_evento("estado", "habilitado", "inhabilitado", motivo)

#     def consultar_ficha(self):
#         return {
#             "id": self.id_vehiculo,
#             "patente": self.patente,
#             "peso_kg": self.peso_kg,
#             "estado": self.estado,
#             "historial": self.historial_eventos
#         }

#     def _registrar_evento(self, campo, anterior, nuevo, motivo=""):
#         self._historial_eventos.append({
#             "fecha": datetime.now(),
#             "campo": campo,
#             "anterior": anterior,
#             "nuevo": nuevo,
#             "motivo": motivo
#         })

#     @property
#     def historial_eventos(self):
#         return self._historial_eventos.copy()

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