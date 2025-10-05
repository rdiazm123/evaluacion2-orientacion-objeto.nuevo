from datetime import datetime

class Actividad:
    def __init__(self, id_actividad, nombre, duracion_min):
        self.id_actividad = id_actividad
        self._nombre = None
        self._duracion_min = None
        self._historial_eventos = []
        self.nombre = nombre
        self.duracion_min = duracion_min

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value

    @property
    def duracion_min(self):
        return self._duracion_min

    @duracion_min.setter
    def duracion_min(self, value):
        if value < 1:
            raise ValueError("La duración debe ser al menos 1 minuto.")
        self._duracion_min = value

    def actualizar_nombre(self, nuevo_nombre):
        anterior = self.nombre
        self.nombre = nuevo_nombre
        self._registrar_evento("nombre", anterior, nuevo_nombre)

    def actualizar_duracion(self, nueva_duracion):
        anterior = self.duracion_min
        self.duracion_min = nueva_duracion
        self._registrar_evento("duracion_min", anterior, nueva_duracion)

    def _registrar_evento(self, campo, anterior, nuevo):
        self._historial_eventos.append({
            "fecha": datetime.now(),
            "campo": campo,
            "anterior": anterior,
            "nuevo": nuevo
        })

    @property
    def historial_eventos(self):
        return self._historial_eventos.copy()
    def __str__(self):
        return f"Actividad(id={self.id_actividad}, nombre={self.nombre}, duracion_min={self.duracion_min})"
    
