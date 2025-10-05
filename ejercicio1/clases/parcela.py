from datetime import datetime

class Parcela:
    def __init__(self, id_parcela, superficie_ha, cultivo_actual):
        self.id_parcela = id_parcela
        self._superficie_ha = None
        self.superficie_ha = superficie_ha
        self._cultivo_actual = None
        self.cultivo_actual = cultivo_actual
        self.estado = 'activa'
        self._historial_eventos = []

    @property
    def superficie_ha(self):
        return self._superficie_ha

    @superficie_ha.setter
    def superficie_ha(self, value):
        if value > 0:
            self._superficie_ha = round(value, 2)
        else:
            raise ValueError("La superficie debe ser mayor que 0.")

    @property
    def cultivo_actual(self):
        return self._cultivo_actual

    @cultivo_actual.setter
    def cultivo_actual(self, value):
        if value:
            self._cultivo_actual = value
        else:
            raise ValueError("El cultivo no puede estar vacío.")

    def actualizar_cultivo(self, nuevo_cultivo):
        if self.estado == 'inactiva':
            raise Exception("No se puede actualizar el cultivo en una parcela inactiva.")
        self.cultivo_actual = nuevo_cultivo
        self._registrar_evento("Cultivo actualizado", f"A {nuevo_cultivo}")

    def activar(self, motivo):
        self.estado = 'activa'
        self._registrar_evento("Activación", motivo)

    def desactivar(self, motivo):
        self.estado = 'inactiva'
        self._registrar_evento("Desactivación", motivo)

    def rectificar_superficie(self, nueva_superficie, motivo):
        if nueva_superficie <= 0:
            raise ValueError("La nueva superficie debe ser mayor que 0.")
        anterior = self.superficie_ha
        self.superficie_ha = nueva_superficie
        self._registrar_evento("Rectificación", f"{anterior} → {nueva_superficie}. Motivo: {motivo}")

    def _registrar_evento(self, tipo, detalle):
        self._historial_eventos.append({
            'fecha': datetime.now(),
            'tipo': tipo,
            'detalle': detalle
        })

    @property
    def historial_eventos(self):
        return self._historial_eventos.copy()
    
