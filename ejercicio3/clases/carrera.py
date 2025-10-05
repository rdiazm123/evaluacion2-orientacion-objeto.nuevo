from .actividad import Actividad
from datetime import datetime

class Carrera(Actividad):
    def __init__(self, id_actividad, nombre, duracion_min, distancia_km):
        super().__init__(id_actividad, nombre, duracion_min)
        if distancia_km <= 0:
            raise ValueError("La distancia debe ser mayor que 0.")
        self._distancia_km = distancia_km
        self._eventos_registro = []

    @property
    def distancia_km(self):
        return self._distancia_km

    @property
    def eventos_registro(self):
        return self._eventos_registro.copy()

    def registrar_distancia(self, nueva_distancia):
        if nueva_distancia <= 0:
            raise ValueError("La distancia debe ser mayor que 0.")
        self._distancia_km = nueva_distancia
        self._eventos_registro.append({
            "fecha": datetime.now(),
            "distancia": nueva_distancia,
            "duracion": self.duracion_min
        })

    def calcular_ritmo(self):
        if self._distancia_km <= 0:
            raise ValueError("No hay distancia registrada válida.")
        return round(self.duracion_min / self._distancia_km, 2)

