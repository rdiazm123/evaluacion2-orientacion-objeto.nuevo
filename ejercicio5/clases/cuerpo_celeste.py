from datetime import datetime

class CuerpoCeleste:
    def __init__(self, id_celeste, nombre, masa_kg):
        self.id_celeste = id_celeste
        self._nombre = None
        self._masa_kg = None
        self._historial_eventos = []
        self.nombre = nombre
        self.masa_kg = masa_kg

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value

    @property
    def masa_kg(self):
        return self._masa_kg

    @masa_kg.setter
    def masa_kg(self, value):
        if value <= 0:
            raise ValueError("La masa debe ser mayor que 0.")
        self._masa_kg = value

    def actualizar_nombre(self, nuevo_nombre):
        anterior = self.nombre
        self.nombre = nuevo_nombre
        self._registrar_evento("nombre", anterior, nuevo_nombre)

    def actualizar_masa(self, nueva_masa):
        anterior = self.masa_kg
        self.masa_kg = nueva_masa
        self._registrar_evento("masa_kg", anterior, nueva_masa)

    def consultar_ficha(self):
        return {
            "id": self.id_celeste,
            "nombre": self.nombre,
            "masa_kg": self.masa_kg,
            "historial": self.historial_eventos
        }

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

