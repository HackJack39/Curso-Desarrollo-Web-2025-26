import pandas as pd
import sqlite3

# ========= INICIALIZAR BASE DE DATOS =========
def inicializar_bd():
    conexion = sqlite3.connect('alumnos.db')
    cursor = conexion.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS alumnos")
    cursor.execute("DROP TABLE IF EXISTS cursos")
    
    # Crear tabla de cursos
    cursor.execute("""
    CREATE TABLE cursos (
        id_curso INTEGER PRIMARY KEY,
        nombre_curso TEXT UNIQUE
        )
    """)

    # Crear tabla de alumnos
    cursor.execute("""
    CREATE TABLE alumnos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER,
        id_curso INTEGER,
        nota REAL,
        FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
        )
    """) 

    # Insertar datos de prueba
    # Nota: Ya no necesitamos la comprobación "if cursor.fetchone()[0] == 0:" porque acabamos de borrar las tablas.
    
    cursos_data = [(1, 'Python'), (2, 'JavaScript')]
    cursor.executemany("INSERT INTO cursos VALUES (?, ?)", cursos_data)

    alumnos_data = [
        (1, 'Ana', 22, 1, 8.5),
        (2, 'Carlos', 25, 1, 9.0),
        (3, 'Elena', 19, 2, 7.8),
        (4, 'Diego', 23, 2, 8.2),
        (5, 'Laura', 21, 1, 8.9)
    ]

    cursor.executemany("INSERT INTO alumnos VALUES (?, ?, ?, ?, ?)", alumnos_data)
    print("Base de datos inicializada con datos de prueba.")
        
    conexion.commit()
    conexion.close()


# ========= FUNCIONES DE CONSULTA =========

def listar_alumnos_por_curso():
    """Listar alumnos de un curso específico."""
    conexion = sqlite3.connect('alumnos.db')

    # Obtener cursos disponibles
    df_cursos = pd.read_sql_query("SELECT id_curso, nombre_curso FROM cursos", conexion)
    print("\n=== Cursos disponibles ===")
    print(df_cursos.to_string(index=False))

    try:
        id_curso = int(input("Ingresa id_curso: "))
    except ValueError:
        print("Entrada no válida. Debe ser un número entero.")
        conexion.close()
        return

    consulta = """
    SELECT a.nombre, a.edad, c.nombre_curso, a.nota
    FROM alumnos a
    INNER JOIN cursos c ON a.id_curso = c.id_curso
    WHERE a.id_curso = ?
    ORDER BY a.nota DESC
    """

    # Usamos una lista como params, la tupla (id_curso,) también es válida
    df = pd.read_sql_query(consulta, conexion, params=[id_curso]) 
    print("\n=== Alumnos del curso ===")
    print(df.to_string(index=False))

    conexion.close()

def estadisticas_por_curso():
    """Mostrar estadísticas de alumnos por curso."""
    conexion = sqlite3.connect('alumnos.db')

    consulta = """
    SELECT
        c.nombre_curso,
        COUNT(a.nombre) as cantidad,
        ROUND(AVG(a.nota), 2) as media,
        ROUND(MAX(a.nota), 2) as maxima,
        ROUND(MIN(a.nota), 2) as minima
    FROM alumnos a
    INNER JOIN cursos c ON a.id_curso = c.id_curso
    GROUP BY c.nombre_curso    
    """

    df = pd.read_sql_query(consulta, conexion)
    print("\n=== Estadísticas por curso ===")
    print(df.to_string(index=False))

    conexion.close()

def buscar_alumno():
    """Buscar alumno por nombre."""
    conexion = sqlite3.connect('alumnos.db')

    nombre = input("Ingresa el nombre del alumno a buscar: ")

    consulta = """
    SELECT a.nombre, a.edad, c.nombre_curso, a.nota
    FROM alumnos a
    INNER JOIN cursos c ON a.id_curso = c.id_curso
    WHERE LOWER(a.nombre) LIKE LOWER(?)
    """

    df = pd.read_sql_query(consulta, conexion, params=[f'%{nombre}%'])

    if len(df) == 0:
        print("No se encontraron resultados")
    else:
        print("\n=== Resultados de la búsqueda ===")
        print(df.to_string(index=False))   

    conexion.close()


def exportar_informe():
    """Exportar informe completo a CSV."""
    conexion = sqlite3.connect('alumnos.db')

    consulta = """
    SELECT
        a.nombre, a.edad, c.nombre_curso, a.nota
    FROM alumnos a
    INNER JOIN cursos c ON a.id_curso = c.id_curso
    ORDER BY c.nombre_curso, a.nota DESC  
    """

    df = pd.read_sql_query(consulta, conexion)
    df.to_csv('informe_alumnos.csv', index=False)

    print("\nInforme exportado a 'informe_alumnos.csv'")

    conexion.close()


# ========= MENÚ PRINCIPAL =========

def menu_principal():
    """Menú interactivo de la aplicación"""
    while True:
        print("""
=== APP DE GESTIÓN DE ALUMNOS Y NOTAS ===
1. Listar alumnos por curso
2. Estadísticas de notas por curso
3. Buscar alumno por nombre
4. Exportar informe completo a CSV
5. Salir
        """)
        
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '1':
            listar_alumnos_por_curso()
        elif opcion == '2':
            estadisticas_por_curso()
        elif opcion == '3':
            buscar_alumno()
        elif opcion == '4':
            exportar_informe()
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

        input("Presiona Enter para continuar...")

# ========= EJECUTAR =========

if __name__ == "__main__":
    inicializar_bd()
    menu_principal()