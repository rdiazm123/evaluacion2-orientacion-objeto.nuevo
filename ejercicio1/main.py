   
from clases.parcela_con_riego import ParcelaConRiego

def mostrar_historial_eventos(eventos):
    print("\n🕓 Historial de eventos:")
    for i, evento in enumerate(eventos, 1):
        fecha = evento['fecha'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"  [{i}] {fecha} | {evento['tipo']}: {evento['detalle']}")

def mostrar_eventos_riego(eventos):
    print("\n💧 Eventos de riego:")
    for i, evento in enumerate(eventos, 1):
        fecha = evento['fecha'].strftime('%Y-%m-%d %H:%M:%S')
        modo = evento.get('modo', 'N/A')
        litros = evento.get('litros_aplicados', evento.get('litros', 'N/A'))
        saldo_antes = evento.get('saldo_antes', 'N/A')
        saldo_despues = evento.get('saldo_despues', evento.get('saldo_final', 'N/A'))
        print(f"  [{i}] {fecha} | Modo: {modo} | Litros: {litros} | Saldo: {saldo_antes} → {saldo_despues}")

if __name__ == "__main__":
    try:
        parcela = ParcelaConRiego(1, 10.50, "Trigo")
        parcela.actualizar_cultivo("Maíz")
        parcela.configurar_tasa(1500)
        parcela.configurar_umbral(2000)
        parcela.cargar_agua(20000)
        parcela.regar_automatico("estricto")
    except ValueError as e:
        print("❌ Error en configuración inicial:", e)

    try:
        parcela.desactivar("Mantenimiento")
        parcela.regar_automatico("estricto")
    except ValueError as e:
        print("❌ Error al regar en modo estricto:", e)

    try:
        parcela.cargar_agua(3000)
        parcela.regar_automatico("parcial")
    except ValueError as e:
        print("❌ Error al regar en modo parcial:", e)

    try:
        parcela.litros_disponibles = 99999  # acceso directo prohibido
    except Exception:
        print("❌ No se puede modificar litros directamente")

    mostrar_eventos_riego(parcela.eventos_riego)
    mostrar_historial_eventos(parcela.historial_eventos)
    