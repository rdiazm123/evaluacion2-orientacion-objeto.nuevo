from ejercicio5.clases.planeta import Planeta
from ejercicio5.clases.cuerpo_celeste import CuerpoCeleste

def mostrar_historial_eventos(eventos):
    print("\n🕓 Historial de eventos:")
    for i, evento in enumerate(eventos, 1):
        fecha = evento['fecha'].strftime('%Y-%m-%d %H:%M:%S')
        campo = evento['campo']
        print(f"  [{i}] {fecha} | {campo}: {evento['anterior']} → {evento['nuevo']}")

if __name__ == "__main__":
    try:
        estrella = CuerpoCeleste(1, "Estrella X", 2e30)
        print("✅ Cuerpo celeste creado:", estrella.nombre, "Masa:", estrella.masa_kg)
    except ValueError as e:
        print("❌ Error al crear cuerpo celeste:", e)

    try:
        tierra = Planeta(2, "Tierra", 5.97e24, 6371, 149_600_000)
        marte = Planeta(3, "Marte", 6.42e23, 3389, 227_900_000)
        print("✅ Planetas creados:")
        print("🌍", tierra.nombre, "Radio:", tierra.radio_km, "Distancia:", tierra.distancia_sol_km)
        print("🔴", marte.nombre, "Radio:", marte.radio_km, "Distancia:", marte.distancia_sol_km)
    except ValueError as e:
        print("❌ Error al crear planeta:", e)

    try:
        print("📊 Densidad Tierra:", tierra.calcular_densidad(), "kg/km³")
        print("📊 Densidad Marte:", marte.calcular_densidad(), "kg/km³")
    except ValueError as e:
        print("❌ Error al calcular densidad:", e)

    try:
        print("🪐 Comparación de distancia:", tierra.comparar_distancia(marte))
    except Exception as e:
        print("❌ Error al comparar distancias:", e)

    try:
        planeta_invalido = Planeta(4, "Error", 1e24, 0, -100)
    except ValueError as e:
        print("❌ Error al crear planeta inválido:", e)

    try:
        tierra.actualizar_masa(6e24)
    except ValueError as e:
        print("❌ Error al actualizar masa:", e)

    try:
        tierra.radio_km = 7000  # acceso directo prohibido
    except AttributeError as e:
        print("❌ No se puede modificar radio directamente:", e)

    mostrar_historial_eventos(tierra.historial_eventos)

                               
