# main.py
from clases.auto import Auto
from datetime import datetime
from clases.vehiculo import Vehiculo    

def separador():
    print("\n" + "="*60)

if __name__ == "__main__":
    separador()
    print("🚗 Ejercicio 4 — Validación extendida de Auto y Vehículo")
    separador()

    try:
        auto = Auto(4, "ABCD12", 1450, 5)
        auto.subir_personas(3)
        auto.bajar_personas(2)
        auto.reconfigurar_asientos(4, "ajuste técnico")
        auto.vaciar_auto("fin de jornada")
        auto.actualizar_peso(1500, "recalibración oficial")
        auto.inhabilitar("mantenimiento programado")
        try:
            auto.actualizar_peso(1600, "intento inválido")  # ✔️ Rechazo esperado
        except ValueError as e:
            print("✅ Rechazo ético:", e)
        auto.habilitar("revisión completada")
        auto.actualizar_peso(1550, "ajuste final")
        try:
            auto.peso_kg = 9999  # ✔️ Acceso directo prohibido
        except Exception:
            print("❌ No se puede modificar litros directamente:")
    except Exception as e:
        print("❌ Error general en Ejercicio 4:", e)

    # ✔️ Mostrar eventos de ocupación
    print("\n📋 Eventos de ocupación:")
    for i, evento in enumerate(auto.eventos_ocupacion, 1):
        fecha = evento['fecha'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"  [{i}] {fecha} | Acción: {evento['accion']} | Cantidad: {evento['cantidad']} | Ocupación: {evento['antes']} → {evento['despues']}")

    # ✔️ Mostrar historial de eventos
    print("\n📋 Historial de eventos:")
    for i, evento in enumerate(auto.historial_eventos, 1):
        fecha = evento['fecha'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"  [{i}] {fecha} | Campo: {evento['campo']} | {evento['anterior']} → {evento['nuevo']} | Motivo: {evento['motivo']}")
    separador()
# Fin de main.py
