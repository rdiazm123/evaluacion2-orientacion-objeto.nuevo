from .publicacion import Publicacion
from datetime import datetime

class Libro(Publicacion):
    def __init__(self, id_publicacion, titulo, anio, paginas_totales):
        super().__init__(id_publicacion, titulo, anio)
        if paginas_totales <= 0:
            raise ValueError("Las páginas totales deben ser mayores que 0.")
        self._paginas_totales = paginas_totales
        self._paginas_leidas = 0
        self._eventos_lectura = []

    @property
    def paginas_totales(self):
        return self._paginas_totales

    @property
    def paginas_leidas(self):
        return self._paginas_leidas

    @property
    def eventos_lectura(self):
        return self._eventos_lectura.copy()

    def leer(self, paginas):
        if paginas <= 0:
            raise ValueError("No se pueden leer páginas negativas.")
        if self._paginas_leidas + paginas > self._paginas_totales:
            raise ValueError("No se pueden leer más páginas que las disponibles.")
        self._paginas_leidas += paginas
        self._eventos_lectura.append({
            "fecha": datetime.now(),
            "leidas": paginas,
            "acumulado": self._paginas_leidas
        })

    def consultar_progreso(self):
        return round((self._paginas_leidas / self._paginas_totales) * 100, 2)

