from datetime import datetime

class Publicacion:
    def __init__(self, id_publicacion, titulo, anio):
        self.id_publicacion = id_publicacion
        self._titulo = None
        self._anio = None
        self._historial_eventos = []
        self.titulo = titulo
        self.anio = anio

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        if not value:
            raise ValueError("El título no puede estar vacío.")
        self._titulo = value

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, value):
        if value < 1450:
            raise ValueError("El año debe ser igual o mayor a 1450.")
        self._anio = value

    def actualizar_titulo(self, nuevo_titulo):
        anterior = self.titulo
        self.titulo = nuevo_titulo
        self._registrar_evento("titulo", anterior, nuevo_titulo)

    def actualizar_anio(self, nuevo_anio):
        anterior = self.anio
        self.anio = nuevo_anio
        self._registrar_evento("anio", anterior, nuevo_anio)

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
