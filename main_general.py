# main_general.py
import time
from ejercicio1.clases.parcela_con_riego import ParcelaConRiego
from ejercicio2.clases.libro import Libro
from ejercicio3.clases.carrera import Carrera
from ejercicio4.clases.auto import Auto
from ejercicio5.clases.planeta import Planeta

def separador(titulo):
    print("\n" + "="*70)
    print(f"🔍 {titulo}")
    print("="*70)

def mostrar_eventos(eventos, tipo):
    print(f"\n📋 Eventos registrados ({tipo}):")
    for i, evento in enumerate(eventos, 1):
        fecha = evento['fecha'].strftime('%Y-%m-%d %H:%M:%S')
        if tipo == "riego":
            print(f"  [{i}] {fecha} | Modo: {evento['modo']} | Litros: {evento['litros_aplicados']} | Saldo: {evento['saldo_antes']} → {evento['saldo_despues']}")
        elif tipo == "lectura":
            print(f"  [{i}] {fecha} | Leídas: {evento['leidas']} | Acumulado: {evento['acumulado']}")
        elif tipo == "registro":
            print(f"  [{i}] {fecha} | Distancia: {evento['distancia']} km | Duración: {evento['duracion']} min")
        elif tipo == "ocupación":
            print(f"  [{i}] {fecha} | Acción: {evento['accion']:<8} | Cantidad: {evento['cantidad']} | Ocupación: {evento['antes']} → {evento['despues']}")
        elif tipo == "historial":
            print(f"  [{i}] {fecha} | Campo: {evento['campo']:<10} | {evento['anterior']} → {evento['nuevo']} | Motivo: {evento['motivo']}")

if __name__ == "__main__":
    # 🟩 Ejercicio 1 — Parcela con riego
    separador("Ejercicio 1 — Parcela con riego")
    try:
        parcela = ParcelaConRiego(1, 10.5, "Trigo")
        parcela.actualizar_cultivo("Maíz")
        parcela.configurar_tasa(1500)
        parcela.configurar_umbral(2000)
        parcela.cargar_agua(20000)
        parcela.regar_automatico("estricto")
        parcela.desactivar("Mantenimiento")
        try:
            parcela.regar_automatico("estricto")
        except ValueError as e:
            print("✅ Rechazo ético:", e)
        parcela.cargar_agua(3000)
        parcela.regar_automatico("parcial")
        try:
            parcela.litros_disponibles = 99999
        except AttributeError as e:
            print("✅ Acceso prohibido:", e)
        mostrar_eventos(parcela.eventos_riego, "riego")
        mostrar_eventos(parcela.historial_eventos, "historial")
    except Exception as e:
        print("❌ Error en Ejercicio 1:", e)

    # 🟩 Ejercicio 2 — Club de lectura
    separador("Ejercicio 2 — Club de lectura")
    try:
        libro = Libro(2, "Cien años de soledad", 1967, 500)
        libro.leer(120)
        try:
            libro.leer(400)
        except ValueError as e:
            print("✅ Rechazo ético:", e)
        print("📚 Progreso:", libro.consultar_progreso(), "%")
        libro.actualizar_anio(1970, "actualización editorial")
        try:
            libro.paginas_leidas = 999
        except AttributeError as e:
            print("✅ Acceso prohibido:", e)
        mostrar_eventos(libro.eventos_lectura, "lectura")
        mostrar_eventos(libro.historial_eventos, "historial")
    except Exception as e:
        print("❌ Error en Ejercicio 2:", e)

    # 🟩 Ejercicio 3 — Registro de actividades físicas
    separador("Ejercicio 3 — Registro de actividades físicas")
    try:
        carrera = Carrera(3, "10K", 50, 10)
        carrera.registrar_distancia(10)
        print("🏃 Ritmo:", carrera.calcular_ritmo(), "min/km")
        carrera.actualizar_duracion(55, "ajuste por semáforo")
        try:
            carrera.distancia_km = 42
        except AttributeError as e:
            print("✅ Acceso prohibido:", e)
        mostrar_eventos(carrera.eventos_registro, "registro")
        mostrar_eventos(carrera.historial_eventos, "historial")
    except Exception as e:
        print("❌ Error en Ejercicio 3:", e)

    # 🟩 Ejercicio 4 — Parque de estacionamiento
    separador("Ejercicio 4 — Parque de estacionamiento")
    try:
        auto = Auto(4, "ABCD12", 1450, 5)
        print(f"✅ Auto creado: {auto._patente} | Peso: {auto.peso_kg} kg | Asientos: {auto._cantidad_asientos}")
        time.sleep(1)

        auto.subir_personas(3)
        time.sleep(1.2)

        auto.bajar_personas(2)
        time.sleep(1.2)

        auto.reconfigurar_asientos(4, "ajuste técnico")
        time.sleep(1.5)

        auto.vaciar_auto("fin de jornada")
        time.sleep(1.5)

        auto.actualizar_peso(1500, "recalibración oficial")
        time.sleep(1.5)

        auto.inhabilitar("mantenimiento programado")
        time.sleep(1.5)

        try:
            auto.actualizar_peso(1600, "intento inválido")
        except ValueError as e:
            print(f"✅ Rechazo ético al modificar peso inhabilitado: {e}")
        time.sleep(1.2)

        auto.habilitar("revisión completada")
        time.sleep(1.2)

        auto.actualizar_peso(1550, "ajuste final")
        time.sleep(1.2)

        try:
            auto.peso_kg = 9999
        except Exception:
            print("❌ No se puede modificar el peso directamente (acceso denegado)")
        time.sleep(1)

        mostrar_eventos(auto.eventos_ocupacion, "ocupación")
        time.sleep(1)
        mostrar_eventos(auto.historial_eventos, "historial")
        time.sleep(1)

    except Exception as e:
        print("❌ Error en Ejercicio 4:", e)

    # 🟩 Ejercicio 5 — Catálogo de planetas
    separador("Ejercicio 5 — Catálogo de planetas")
    try:
        tierra = Planeta(5, "Tierra", 5.97e24, 6371, 149_600_000)
        marte = Planeta(6, "Marte", 6.42e23, 3389, 227_900_000)
        print("🌍 Densidad Tierra:", tierra.calcular_densidad(), "kg/km³")
        print("🔴 Comparación:", tierra.comparar_distancia(marte))
        tierra.actualizar_masa(6e24, "revisión científica")
        try:
            tierra.radio_km = 7000
        except AttributeError as e:
            print("✅ Acceso prohibido:", e)
        mostrar_eventos(tierra.historial_eventos, "historial")
    except Exception as e:
        print("❌ Error en Ejercicio 5:", e)


        auto.subir_personas(3)
        time.sleep(1.2)

        auto.bajar_personas(2)
        time.sleep(1.2)

        auto.reconfigurar_asientos(4, "ajuste técnico")
        time.sleep(1.5)

        auto.vaciar_auto("fin de jornada")
        time.sleep(1.5)

        auto.actualizar_peso(1500, "recalibración oficial")
        time.sleep(1.5)

        auto.inhabilitar("mantenimiento programado")
        time.sleep(1.5)

        try:
            auto.actualizar_peso(1600, "intento inválido")
        except ValueError as e:
            print(f"✅ Rechazo ético al modificar peso inhabilitado: {e}")
        time.sleep(1.2)

        auto.habilitar("revisión completada")
        time.sleep(1.2)

        auto.actualizar_peso(1550, "ajuste final")
        time.sleep(1.2)

        try:
            auto.peso_kg = 9999
        except Exception:
            print("❌ No se puede modificar el peso directamente (acceso denegado)")
        time.sleep(1)

        mostrar_eventos(auto.eventos_ocupacion, "ocupación")
        time.sleep(1)
        mostrar_eventos(auto.historial_eventos, "historial")
        time.sleep(1)

    except Exception as e:
        print("❌ Error en Ejercicio 4:", e)

    # 🟩 Ejercicio 5 — Catálogo de planetas
    separador("Ejercicio 5 — Catálogo de planetas")
    try:
        tierra = Planeta(5, "Tierra", 5.97e24, 6371, 149_600_000)
        marte = Planeta(6, "Marte", 6.42e23, 3389, 227_900_000)
        print("🌍 Densidad Tierra:", tierra.calcular_densidad(), "kg/km³")
        print("🔴 Comparación:", tierra.comparar_distancia(marte))
        tierra.actualizar_masa(6e24)
        try:
            tierra.radio_km = 7000
        except AttributeError as e:
            print("✅ Acceso prohibido:", e)
        mostrar_eventos(tierra.historial_eventos, "historial")
    except Exception as e:
        print("❌ Error en Ejercicio 5:", e)
    separador("Fin de la validación general")
# Fin de main_general.py