
from clases.libro import Libro
from clases.publicacion import Publicacion

def mostrar_historial_eventos(eventos):
    print("\n🕓 Historial de eventos:")
    for i, evento in enumerate(eventos, 1):
        fecha = evento['fecha'].strftime('%Y-%m-%d %H:%M:%S')
        campo = evento['campo']
        print(f"  [{i}] {fecha} | {campo}: {evento['anterior']} → {evento['nuevo']}")

def mostrar_eventos_lectura(eventos):
    print("\n📖 Eventos de lectura:")
    for i, evento in enumerate(eventos, 1):
        fecha = evento['fecha'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"  [{i}] {fecha} | Leídas: {evento['leidas']} | Acumulado: {evento['acumulado']}")

if __name__ == "__main__":
    try:
        pub1 = Publicacion(1, "Don Quijote", 1605)
        print("✅ Publicación creada:", pub1.titulo, pub1.anio)
    except ValueError as e:
        print("❌ Error al crear publicación:", e)

    try:
        pub2 = Publicacion(2, "Libro inválido", 1400)
    except Exception:
        print("❌ Año inválido:")

    try:
        libro = Libro(3, "Cien años de soledad", 1967, 500)
        print("✅ Libro creado:", libro.titulo, libro.anio, "páginas:", libro.paginas_totales)
    except Exception:
        print("❌ Error al crear libro:")

    try:
        libro.leer(120)
        print("📖 Leídas 120 páginas. Progreso:", libro.consultar_progreso(), "%")
    except ValueError as e:
        print("❌ Error al leer:", e)

    try:
        libro.leer(400)
    except Exception:
        print("❌ Error al leer demasiadas páginas")

    try:
        libro.actualizar_anio(1967)
    except Exception:
        print("❌ Error al actualizar año")

    try:
        libro.paginas_leidas = 999  # acceso directo prohibido
    except Exception:
        print("❌ No se puede modificar páginas directamente")

    mostrar_eventos_lectura(libro.eventos_lectura)
#mo
    mostrar_historial_eventos(libro.historial_eventos)
#mostrar_historial_eventos(pub1.historial_eventos)
    try:
        pub1.actualizar_titulo("El ingenioso hidalgo Don Quijote de la Mancha")
        print("✅ Título actualizado:", pub1.titulo)
    except ValueError as e:
        print("❌ Error al actualizar título:", e)

    try:
        pub1.actualizar_anio(1615)
        print("✅ Año actualizado:", pub1.anio)
    except ValueError as e:
        print("❌ Error al actualizar año:", e)

    mostrar_historial_eventos(pub1.historial_eventos)   
    try:
        pub1.actualizar_anio(1400)
    except Exception:
        print("❌ Error al actualizar a un año inválido")
    mostrar_historial_eventos(pub1.historial_eventos)
    try:
        pub1.actualizar_titulo("")
    except Exception:
        print("❌ Error al actualizar a un título vacío")
    mostrar_historial_eventos(pub1.historial_eventos)
    try:
        pub1.anio = 1400
    except Exception:
        print("❌ Error al asignar un año inválido directamente")
    mostrar_historial_eventos(pub1.historial_eventos)
    try:
        pub1.titulo = ""
    except Exception:
        print("❌ Error al asignar un título vacío directamente")
    mostrar_historial_eventos(pub1.historial_eventos)
    mostrar_eventos_lectura(libro.eventos_lectura)
    mostrar_historial_eventos(libro.historial_eventos)
    try:
        libro.leer(-10)
    except Exception:
        print("❌ Error al leer un número negativo de páginas")
    mostrar_eventos_lectura(libro.eventos_lectura)
    mostrar_historial_eventos(libro.historial_eventos)
    
    

        
