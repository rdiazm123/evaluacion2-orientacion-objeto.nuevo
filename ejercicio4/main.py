from ejercicio4.clases.auto import Auto

def mostrar_historial_eventos(eventos):
    print("\n🕓 Historial de eventos:")
    for i, evento in enumerate(eventos, 1):
        fecha = evento['fecha'].strftime('%Y-%m-%d %H:%M:%S')
        campo = evento['campo']
        print(f"  [{i}] {fecha} | {campo}: {evento['anterior']} → {evento['nuevo']} | Motivo: {evento['motivo']}")

def mostrar_eventos_ocupacion(eventos):
    print("\n📍 Eventos de ocupación:")
    for i, evento in enumerate(eventos, 1):
        fecha = evento['fecha'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"  [{i}] {fecha} | Acción: {evento['accion']} | Cantidad: {evento['cantidad']} | Ocupación: {evento['antes']} → {evento['despues']}")

if __name__ == "__main__":
    try:
        auto = Auto(1, "ABCD12", 1450, 5)
        print("✅ Auto creado:", auto.patente, "Peso:", auto.peso_kg, "Asientos:", auto.asientos_totales)
    except ValueError as e:
        print("❌ Error al crear auto:", e)

    try:
        auto.actualizar_peso(1500)
    except ValueError as e:
        print("❌ Error al actualizar peso:", e)

    try:
        auto.actualizar_peso(0)
    except ValueError as e:
        print("❌ Peso inválido:", e)

    try:
        auto.inhabilitar("mantención")
        auto.actualizar_peso(1600)
    except ValueError as e:
        print("❌ No se puede actualizar peso:", e)

    try:
        auto.habilitar("mantención finalizada")
        auto.subir_personas(3)
    except ValueError as e:
        print("❌ Error al subir personas:", e)

    try:
        auto.subir_personas(3)
    except ValueError as e:
        print("❌ Exceso de ocupantes:", e)

    try:
        auto.bajar_personas(2)
    except ValueError as e:
        print("❌ Error al bajar personas:", e)

    try:
        auto.bajar_personas(5)
    except ValueError as e:
        print("❌ No puede quedar negativo:", e)

    try:
        auto.reconfigurar_asientos(2, "reparación")
    except ValueError as e:
        print("❌ Asientos inválidos:", e)

    try:
        auto.reconfigurar_asientos(0, "error")
    except ValueError as e:
        print("❌ Asientos inválidos:", e)

    try:
        auto.vaciar_auto("fin de turno")
    except ValueError as e:
        print("❌ Error al vaciar auto:", e)

    try:
        auto.inhabilitar("cierre")
        auto.subir_personas(1)
    except ValueError as e:
        print("❌ Estado inhabilitado:", e)

    print("\n📋 Ocupación actual:", auto.consultar_ocupacion())
    mostrar_historial_eventos(auto.historial_eventos)
    mostrar_eventos_ocupacion(auto.eventos_ocupacion)
