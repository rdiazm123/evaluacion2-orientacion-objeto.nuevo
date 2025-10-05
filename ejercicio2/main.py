from ejercicio2.clases.libro import Libro
from ejercicio2.clases.publicacion import Publicacion

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
    except ValueError as e:
        print("❌ Año inválido:", e)

    try:
        libro = Libro(3, "Cien años de soledad", 1967, 500)
        print("✅ Libro creado:", libro.titulo, libro.anio, "páginas:", libro.paginas_totales)
    except ValueError as e:
        print("❌ Error al crear libro:", e)

    try:
        libro.leer(120)
        print("📖 Leídas 120 páginas. Progreso:", libro.consultar_progreso(), "%")
    except ValueError as e:
        print("❌ Error al leer:", e)

    try:
        libro.leer(400)
    except ValueError as e:
        print("❌ Error al leer demasiadas páginas:", e)

    try:
        libro.actualizar_anio(1967)
    except ValueError as e:
        print("❌ Error al actualizar año:", e)

    try:
        libro.paginas_leidas = 999  # acceso directo prohibido
    except AttributeError as e:
        print("❌ No se puede modificar páginas directamente:", e)

    mostrar_eventos_lectura(libro.eventos_lectura)
    mostrar_historial_eventos(libro.historial_eventos)
    

        
