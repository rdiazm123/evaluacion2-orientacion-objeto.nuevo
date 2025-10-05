from ejercicio3.clases.actividad import Actividad
from ejercicio3.clases.carrera import Carrera

def mostrar_historial_eventos(eventos):
    print("\n🕓 Historial de eventos:")
    for i, evento in enumerate(eventos, 1):
        fecha = evento['fecha'].strftime('%Y-%m-%d %H:%M:%S')
        campo = evento['campo']
        print(f"  [{i}] {fecha} | {campo}: {evento['anterior']} → {evento['nuevo']}")

def mostrar_eventos_registro(eventos):
    print("\n📋 Eventos de registro:")
    for i, evento in enumerate(eventos, 1):
        fecha = evento['fecha'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"  [{i}] {fecha} | Distancia: {evento['distancia']} km | Duración: {evento['duracion']} min")

if __name__ == "__main__":
    try:
        actividad = Actividad(1, "Yoga", 60)
        print("✅ Actividad creada:", actividad.nombre, actividad.duracion_min, "min")
    except ValueError as e:
        print("❌ Error al crear actividad:", e)

    try:
        actividad_invalida = Actividad(2, "Error", 0)
    except ValueError as e:
        print("❌ Duración inválida:", e)

    try:
        carrera = Carrera(3, "10K", 50, 10)
        print("✅ Carrera creada:", carrera.nombre, carrera.duracion_min, "min", "Distancia:", carrera.distancia_km, "km")
    except ValueError as e:
        print("❌ Error al crear carrera:", e)

    try:
        ritmo = carrera.calcular_ritmo()
        print("🏃 Ritmo:", ritmo, "min/km")
    except ValueError as e:
        print("❌ Error al calcular ritmo:", e)

    try:
        carrera.registrar_distancia(-3)
    except ValueError as e:
        print("❌ Error al registrar distancia:", e)

    try:
        carrera.actualizar_duracion(55)
    except ValueError as e:
        print("❌ Error al actualizar duración:", e)

    try:
        carrera.distancia_km = 42  # acceso directo prohibido
    except AttributeError as e:
        print("❌ No se puede modificar distancia directamente:", e)

    mostrar_eventos_registro(carrera.eventos_registro)
    mostrar_historial_eventos(carrera.historial_eventos)

        
        