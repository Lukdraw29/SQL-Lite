1
import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("NBA.db")
cursor = conexion.cursor()

# Crear tabla de equipos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS equipos (
        id_equipo INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        ciudad TEXT NOT NULL,
        arena TEXT,
        anyo_de_fundacion INTEGER
    );
''')

# Crear tabla de jugadores
cursor.execute('''
    CREATE TABLE IF NOT EXISTS jugadores (
        id_jugador INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        id_equipo INTEGER,
        posicion TEXT,
        altura REAL,
        peso REAL,
        fecha_de_nacimiento DATE,
        FOREIGN KEY (id_equipo) REFERENCES equipos(id_equipo)
    );
''')

# Crear tabla de partidos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS partidos (
        id_partido INTEGER PRIMARY KEY,
        fecha DATE NOT NULL,
        id_equipo_local INTEGER,
        id_equipo_visitante INTEGER,
        puntuacion_local INTEGER,
        puntuacion_visitante INTEGER,
        FOREIGN KEY (id_equipo_local) REFERENCES equipos(id_equipo),
        FOREIGN KEY (id_equipo_visitante) REFERENCES equipos(id_equipo)
    );
''')

# Crear tabla de estadísticas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS estadisticas (
        stat_id INTEGER PRIMARY KEY,
        id_jugador INTEGER,
        id_partido INTEGER,
        puntos INTEGER,
        rebotes INTEGER,
        asistencias INTEGER,
        robos INTEGER,
        bloqueos INTEGER,
        minutos_jugados INTEGER,
        FOREIGN KEY (id_jugador) REFERENCES jugadores(id_jugador),
        FOREIGN KEY (id_partido) REFERENCES partidos(id_partido)
    );
''')

# CRUD: Insertar equipo
def insertar_equipo(id_equipo, nombre, ciudad, arena, anyo):
    cursor.execute("INSERT INTO equipos (id_equipo, nombre, ciudad, arena, anyo_de_fundacion) VALUES (?, ?, ?, ?, ?)",
                   (id_equipo, nombre, ciudad, arena, anyo))
    conexion.commit()

# CRUD: Listar equipos
def listar_equipos():
    cursor.execute("SELECT * FROM equipos")
    for equipo in cursor.fetchall():
        print(equipo)

# CRUD: Actualizar equipo
def actualizar_equipo(id_equipo, nombre, ciudad, arena, anyo):
    cursor.execute("UPDATE equipos SET nombre=?, ciudad=?, arena=?, anyo_de_fundacion=? WHERE id_equipo=?",
                   (nombre, ciudad, arena, anyo, id_equipo))
    conexion.commit()

# CRUD: Eliminar equipo
def eliminar_equipo(id_equipo):
    cursor.execute("DELETE FROM equipos WHERE id_equipo=?", (id_equipo,))
    conexion.commit()

    # CRUD para jugadores
def insertar_jugador(id_jugador, nombre, apellido, id_equipo, posicion, altura, peso, fecha):
    cursor.execute("INSERT INTO jugadores (id_jugador, nombre, apellido, id_equipo, posicion, altura, peso, fecha_de_nacimiento) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (id_jugador, nombre, apellido, id_equipo, posicion, altura, peso, fecha))
    conexion.commit()

def listar_jugadores():
    cursor.execute("SELECT * FROM jugadores")
    for jugador in cursor.fetchall():
        print(jugador)

def actualizar_jugador(id_jugador, nombre, apellido, id_equipo, posicion, altura, peso, fecha):
    cursor.execute("UPDATE jugadores SET nombre=?, apellido=?, id_equipo=?, posicion=?, altura=?, peso=?, fecha_de_nacimiento=? WHERE id_jugador=?",
                   (nombre, apellido, id_equipo, posicion, altura, peso, fecha, id_jugador))
    conexion.commit()

def eliminar_jugador(id_jugador):
    cursor.execute("DELETE FROM jugadores WHERE id_jugador=?", (id_jugador,))
    conexion.commit()

    # CRUD para partidos
def insertar_partido(id_partido, fecha, id_local, id_visitante, puntuacion_local, puntuacion_visitante):
    cursor.execute("INSERT INTO partidos (id_partido, fecha, id_equipo_local, id_equipo_visitante, puntuacion_local, puntuacion_visitante) VALUES (?, ?, ?, ?, ?, ?)",
                   (id_partido, fecha, id_local, id_visitante, puntuacion_local, puntuacion_visitante))
    conexion.commit()

def listar_partidos():
    cursor.execute("SELECT * FROM partidos")
    for partido in cursor.fetchall():
        print(partido)

def actualizar_partido(id_partido, fecha, id_local, id_visitante, puntuacion_local, puntuacion_visitante):
    cursor.execute("UPDATE partidos SET fecha=?, id_equipo_local=?, id_equipo_visitante=?, puntuacion_local=?, puntuacion_visitante=? WHERE id_partido=?",
                   (fecha, id_local, id_visitante, puntuacion_local, puntuacion_visitante, id_partido))
    conexion.commit()

def eliminar_partido(id_partido):
    cursor.execute("DELETE FROM partidos WHERE id_partido=?", (id_partido,))
    conexion.commit()

# CRUD para estadísticas
def insertar_estadistica(stat_id,id_jugador, id_partido, puntos, rebotes, asistencias, robos, bloqueos, minutos):
    cursor.execute("INSERT INTO estadisticas (stat_id, id_jugador, id_partido, puntos, rebotes, asistencias, robos, bloqueos, minutos_jugados) VALUES (? ,?, ?, ?, ?, ?, ?, ?, ?)",
                   (stat_id,id_jugador, id_partido, puntos, rebotes, asistencias, robos, bloqueos, minutos))
    conexion.commit()

def listar_estadisticas():
    cursor.execute("SELECT * FROM estadisticas")
    for estadistica in cursor.fetchall():
        print(estadistica)

def actualizar_estadistica(stat_id, id_jugador, id_partido, puntos, rebotes, asistencias, robos, bloqueos, minutos):
    cursor.execute("UPDATE estadisticas SET id_jugador=?, id_partido=?, puntos=?, rebotes=?, asistencias=?, robos=?, bloqueos=?, minutos_jugados=? WHERE stat_id=?",
                   (id_jugador, id_partido, puntos, rebotes, asistencias, robos, bloqueos, minutos, stat_id))
    conexion.commit()

def eliminar_estadistica(stat_id):
    cursor.execute("DELETE FROM estadisticas WHERE stat_id=?", (stat_id,))
    conexion.commit()


# CRUD: Eliminar registros
def eliminar_equipo(id_equipo):
    cursor.execute("DELETE FROM equipos WHERE id_equipo=?", (id_equipo,))
    conexion.commit()

def eliminar_jugador(id_jugador):
    cursor.execute("DELETE FROM jugadores WHERE id_jugador=?", (id_jugador,))
    conexion.commit()

def eliminar_partido(id_partido):
    cursor.execute("DELETE FROM partidos WHERE id_partido=?", (id_partido,))
    conexion.commit()

def eliminar_estadistica(stat_id):
    cursor.execute("DELETE FROM estadisticas WHERE stat_id=?", (stat_id,))
    conexion.commit()

# Menú interactivo
def menu():
    while True:
        print("\nMenú Principal")
        print("1. Insertar equipo")
        print("2. Listar equipos")
        print("3. Insertar jugador")
        print("4. Listar jugadores")
        print("5. Insertar partido")
        print("6. Listar partidos")
        print("7. Insertar estadística")
        print("8. Listar estadísticas")
        print("9. Eliminar equipo")
        print("10. Eliminar jugador")
        print("11. Eliminar partido")
        print("12. Eliminar estadística")
        print("13. Actualizar equipo")
        print("14. Actualizar jugador")
        print("15. Actualizar partido")
        print("16. Actualizar estadística")
        print("17. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_equipo= input("Id Equipo: ")
            nombre = input("Nombre: ")
            ciudad = input("Ciudad: ")
            arena = input("Arena: ")
            anyo = input("Año de fundación: ")
            insertar_equipo(id_equipo, nombre, ciudad, arena, anyo)
        elif opcion == "2":
            listar_equipos()
        elif opcion == "3":
            id_jugador=input("Id Jugador: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            id_equipo = input("ID Equipo: ")
            posicion = input("Posición: ")
            altura = input("Altura: ")
            peso = input("Peso: ")
            fecha = input("Fecha de nacimiento (YYYY-MM-DD): ")
            insertar_jugador(id_jugador,nombre, apellido, id_equipo, posicion, altura, peso, fecha)
        elif opcion == "4":
            listar_jugadores()
        elif opcion == "5":
            id_partido= input("ID Partido: ")
            fecha = input("Fecha (YYYY-MM-DD): ")
            id_local = input("ID Equipo Local: ")
            id_visitante = input("ID Equipo Visitante: ")
            puntuacion_local = input("Puntuación Local: ")
            puntuacion_visitante = input("Puntuación Visitante: ")
            insertar_partido(id_partido, fecha, id_local, id_visitante, puntuacion_local, puntuacion_visitante)
        elif opcion == "6":
            listar_partidos()
        elif opcion == "7":
            stat_id= input("ID estadistica: ")
            id_jugador = input("ID Jugador: ")
            id_partido = input("ID Partido: ")
            puntos = input("Puntos: ")
            rebotes = input("Rebotes: ")
            asistencias = input("Asistencias: ")
            robos = input("Robos: ")
            bloqueos = input("Bloqueos: ")
            minutos = input("Minutos jugados: ")
            insertar_estadistica(stat_id, id_jugador, id_partido, puntos, rebotes, asistencias, robos, bloqueos, minutos)
        elif opcion == "8":
            listar_estadisticas()
        elif opcion == "9":
            id_equipo = input("ID del equipo: ")
            eliminar_equipo(id_equipo)
        elif opcion == "10":
            id_jugador = input("ID del jugador: ")
            eliminar_jugador(id_jugador)
        elif opcion == "11":
            id_partido = input("ID del partido: ")
            eliminar_partido(id_partido)
        elif opcion == "12":
            stat_id = input("ID de la estadística: ")
            eliminar_estadistica(stat_id)
        if opcion == "13":
            id_equipo = input("ID equipo: ")
            nombre = input("Nombre: ")
            ciudad = input("Ciudad: ")
            arena = input("Arena: ")
            anyo = input("Año de fundación: ")
            actualizar_equipo(id_equipo, nombre, ciudad, arena, anyo)
        elif opcion == "14":
            id_jugador = input("ID jugador: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            id_equipo = input("ID equipo: ")
            posicion = input("Posición: ")
            altura = input("Altura: ")
            peso = input("Peso: ")
            fecha = input("Fecha de nacimiento: ")
            actualizar_jugador(id_jugador, nombre, apellido, id_equipo, posicion, altura, peso, fecha)
        elif opcion == "15":
            id_partido = input("ID partido: ")
            fecha = input("Fecha: ")
            id_local = input("ID local: ")
            id_visitante = input("ID visitante: ")
            puntuacion_local = input("Puntuación local: ")
            puntuacion_visitante = input("Puntuación visitante: ")
            actualizar_partido(id_partido, fecha, id_local, id_visitante, puntuacion_local, puntuacion_visitante)
        elif opcion == "16":
            stat_id = input("ID estadística: ")
            id_jugador = input("ID jugador: ")
            id_partido = input("ID partido: ")
            puntos = input("Puntos: ")
            rebotes = input("Rebotes: ")
            asistencias = input("Asistencias: ")
            robos = input("Robos: ")
            bloqueos = input("Bloqueos: ")
            minutos = input("Minutos: ")
            actualizar_estadistica(stat_id, id_jugador, id_partido, puntos, rebotes, asistencias, robos, bloqueos, minutos)
        elif opcion == "17":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

# Ejecutar menú al iniciar
if __name__ == "__main__":
    menu()
# Guardar cambios y cerrar conexión
conexion.commit()
conexion.close()

