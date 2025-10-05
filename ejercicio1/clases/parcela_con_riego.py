
from .parcela import Parcela
from datetime import datetime

class ParcelaConRiego(Parcela):
    def __init__(self, id_parcela, superficie_ha, cultivo_actual):
        super().__init__(id_parcela, superficie_ha, cultivo_actual)
        self._litros_disponibles = 0
        self._tasa_riego_l_ha = 0
        self._umbral_min_litros = 0
        self._estado_riego = 'habilitado'
        self._eventos_riego = []

    @property
    def litros_disponibles(self):
        return self._litros_disponibles

    def configurar_tasa(self, l_ha):
        if l_ha <= 0:
            raise ValueError("La tasa de riego debe ser mayor que 0.")
        self._tasa_riego_l_ha = l_ha

    def configurar_umbral(self, litros):
        if litros < 0:
            raise ValueError("El umbral debe ser igual o mayor a 0.")
        self._umbral_min_litros = litros

    def cargar_agua(self, litros):
        if litros <= 0:
            raise ValueError("Los litros deben ser mayores que 0.")
        saldo_antes = self._litros_disponibles
        self._litros_disponibles += litros
        self._registrar_evento_riego("carga", litros, saldo_antes, self._litros_disponibles)

    def regar_automatico(self, modo):
        if self.estado != 'activa':
            raise ValueError("Riego no permitido: parcela inactiva.")
        if self._estado_riego != 'habilitado':
            raise ValueError("Riego no permitido: sistema inhabilitado.")
        if self._tasa_riego_l_ha <= 0:
            raise ValueError("Riego no permitido: tasa de riego inválida.")

        demanda = self.superficie_ha * self._tasa_riego_l_ha
        saldo_antes = self._litros_disponibles

        if modo == 'estricto':
            if saldo_antes - demanda >= self._umbral_min_litros:
                aplicado = demanda
            else:
                raise ValueError("Modo estricto rechazado: no cumple umbral mínimo.")
        elif modo == 'parcial':
            if saldo_antes <= self._umbral_min_litros:
                aplicado = 0
            else:
                aplicado = min(saldo_antes - self._umbral_min_litros, demanda)
        else:
            raise ValueError("Modo inválido.")

        self._litros_disponibles -= aplicado
        self._registrar_evento_riego(modo, aplicado, saldo_antes, self._litros_disponibles)

    def habilitar_riego(self):
        self._estado_riego = 'habilitado'

    def inhabilitar_riego(self):
        self._estado_riego = 'inhabilitado'

    def _registrar_evento_riego(self, modo, litros, antes, despues):
        self._eventos_riego.append({
            'fecha': datetime.now(),
            'modo': modo,
            'litros_aplicados': litros,
            'saldo_antes': antes,
            'saldo_despues': despues
        })

    @property
    def eventos_riego(self):
        return self._eventos_riego.copy()

    def desactivar(self, motivo):
        super().desactivar(motivo)
        self.inhabilitar_riego()
        