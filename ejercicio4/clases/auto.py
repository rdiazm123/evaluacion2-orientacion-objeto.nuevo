from .vehiculo import Vehiculo
from datetime import datetime

class Auto(Vehiculo):
    def __init__(self, id_vehiculo, patente, peso_kg, cantidad_asientos):
        super().__init__(id_vehiculo, patente, peso_kg)
        self._cantidad_asientos = cantidad_asientos
        self._ocupantes = 0
        self.eventos_ocupacion = []

    @property
    def ocupantes(self):
        return self._ocupantes

    def subir_personas(self, cantidad):
        if cantidad <= 0 or self._ocupantes + cantidad > self._cantidad_asientos:
            raise ValueError("Cantidad inválida o supera capacidad.")
        antes = self._ocupantes
        self._ocupantes += cantidad
        self._registrar_ocupacion("subida", cantidad, antes, self._ocupantes)
        self._registrar_evento("ocupantes", antes, self._ocupantes, f"subida de {cantidad}")

    def bajar_personas(self, cantidad):
        if cantidad <= 0 or cantidad > self._ocupantes:
            raise ValueError("Cantidad inválida o mayor a ocupantes actuales.")
        antes = self._ocupantes
        self._ocupantes -= cantidad
        self._registrar_ocupacion("bajada", cantidad, antes, self._ocupantes)
        self._registrar_evento("ocupantes", antes, self._ocupantes, f"bajada de {cantidad}")

    def vaciar_auto(self, motivo):
        antes = self._ocupantes
        self._registrar_ocupacion("vaciado", antes, antes, 0)
        self._registrar_evento("ocupantes", antes, 0, f"vaciado de {antes}")
        self._registrar_evento("ocupantes", antes, 0, motivo)
        self._ocupantes = 0

    def reconfigurar_asientos(self, nueva_cantidad, motivo):
        if nueva_cantidad < self._ocupantes:
            raise ValueError("No se puede reducir por debajo de ocupantes actuales.")
        anterior = self._cantidad_asientos
        self._cantidad_asientos = nueva_cantidad
        self._registrar_evento("asientos", anterior, nueva_cantidad, motivo)

    def _registrar_ocupacion(self, accion, cantidad, antes, despues):
        evento = {
            "fecha": datetime.now(),
            "accion": accion,
            "cantidad": cantidad,
            "antes": antes,
            "despues": despues
        }
        self.eventos_ocupacion.append(evento)

        


        
        