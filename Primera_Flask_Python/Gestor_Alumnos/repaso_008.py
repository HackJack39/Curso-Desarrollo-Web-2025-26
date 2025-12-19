import sqlite3             # Librería estándar para SQLite
import pandas as pd        # Librería para manejar datos en tablas (DataFrame)


# ========================================================================
# INICIALIZACIÓN DE LA BASE DE DATOS
# ========================================================================

def init_db():
    """
    Crea la base de datos 'alumnos_cursos.db' (si no existe) y crea
    las tablas necesarias (cursos_2, alumnos_2).
    
    También inserta datos de prueba la primera vez.
    """
    
    # Conectar (o crear) la base de datos SQLite.
    # El archivo 'alumnos_cursos.db' se crea en la carpeta actual.
    conn = sqlite3.connect("alumnos_cursos.db")
    
    # 'cursor' es el objeto que ejecuta sentencias SQL.
    cursor = conn.cursor()
    
    # Crear tabla CURSOS si no existe.
    # PRIMARY KEY: identifica cada curso de forma única (id_curso).
    # AUTOINCREMENT: genera automáticamente el id.
    # UNIQUE: no puede haber dos cursos con el mismo nombre.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cursos_2 (
            id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_curso TEXT UNIQUE NOT NULL
        )
    """)
    
    # Crear tabla ALUMNOS si no existe.
    # FOREIGN KEY: vincular cada alumno a un curso (id_curso).
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alumnos_2 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER,
            id_curso INTEGER,
            nota REAL,
            FOREIGN KEY (id_curso) REFERENCES cursos_2(id_curso)
        )
    """)
    
    # Comprobar si la tabla cursos_2 ya tiene datos.
    # COUNT(*) devuelve el número de filas.
    cursor.execute("SELECT COUNT(*) FROM cursos_2")
    num_cursos = cursor.fetchone()[0]
    
    # Si la tabla está vacía (num_cursos == 0), insertar datos de prueba.
    if num_cursos == 0:
        
        # Datos de prueba: lista de tuplas (id, nombre).
        cursos_2_data = [
            (1, "Python"),
            (2, "JavaScript"),
            (3, "Big Data"),
        ]
        
        # executemany() permite insertar varias filas de una vez.
        # El '?' son placeholders seguros contra inyecciones SQL.
        cursor.executemany(
            "INSERT INTO cursos_2 (id_curso, nombre_curso) VALUES (?, ?)",
            cursos_2_data,
        )
        
        # Datos de prueba: alumnos (id, nombre, edad, id_curso, nota).
        alumnos_2_data = [
            (1, "Ana",    22, 1, 8.5),
            (2, "Carlos", 25, 1, 9.0),
            (3, "Elena",  19, 2, 7.8),
            (4, "Diego",  23, 2, 8.2),
            (5, "Laura",  21, 1, 8.9),
            (6, "Marta",  24, 3, 9.5),
        ]
        
        cursor.executemany(
            "INSERT INTO alumnos_2 (id, nombre, edad, id_curso, nota) VALUES (?, ?, ?, ?, ?)",
            alumnos_2_data,
        )
        
        print("✓ Base de datos inicializada con datos de prueba.")
    
    # commit() confirma los cambios en la BD.
    conn.commit()
    
    # Cerrar la conexión (libera recursos).
    conn.close()


# ========================================================================
# FUNCIONES QUE DEVUELVEN DATAFRAMES (para usar con Flask)
# ========================================================================

def cursos_df():
    """
    Devuelve un DataFrame con todos los cursos.
    
    Útil para: mostrar un desplegable <select> en HTML con los cursos disponibles.
    
    Retorna:
      DataFrame con columnas: id_curso, nombre_curso
    """
    conn = sqlite3.connect("alumnos_cursos.db")
    
    # read_sql_query ejecuta una consulta SQL y devuelve un DataFrame.
    df = pd.read_sql_query(
        "SELECT id_curso, nombre_curso FROM cursos_2",
        conn
    )
    
    conn.close()
    return df


def listar_alumnos_por_curso_df(id_curso):
    """
    Devuelve los alumnos de un curso específico, ordenados por nota (descendente).
    
    Parámetros:
      id_curso (int o str): ID del curso a consultar
    
    Retorna:
      DataFrame con columnas: nombre_curso, nombre, edad, nota
    """
    conn = sqlite3.connect("alumnos_cursos.db")
    
    # Consulta SQL con INNER JOIN.
    # INNER JOIN: une datos de dos tablas (alumnos_2 y cursos_2) usando id_curso.
    # ORDER BY alumnos_2.nota DESC: ordena por nota de mayor a menor.
    consulta = """
        SELECT
            cursos_2.nombre_curso,
            alumnos_2.nombre,
            alumnos_2.edad,
            alumnos_2.nota
        FROM alumnos_2
        INNER JOIN cursos_2 ON alumnos_2.id_curso = cursos_2.id_curso
        WHERE alumnos_2.id_curso = ?
        ORDER BY alumnos_2.nota DESC
    """
    
    # params=(id_curso,) proporciona el valor para el '?' de seguridad.
    df = pd.read_sql_query(consulta, conn, params=(id_curso,))
    conn.close()
    return df


def estadisticas_por_curso_df():
    """
    Devuelve un DataFrame con estadísticas de notas por curso.
    
    Calcula para cada curso:
      - Cantidad de alumnos
      - Nota promedio (media)
      - Nota máxima
      - Nota mínima
    
    Retorna:
      DataFrame con columnas: nombre_curso, cantidad_alumnos, nota_media, 
                             nota_maxima, nota_minima
    """
    conn = sqlite3.connect("alumnos_cursos.db")
    
    # GROUP BY: agrupa por curso para calcular estadísticas por grupo.
    # COUNT(): cuenta filas (alumnos por curso).
    # AVG(): calcula la media.
    # MAX(), MIN(): máximo y mínimo.
    # ROUND(..., 2): redondea a 2 decimales.
    consulta = """
        SELECT
            cursos_2.nombre_curso,
            COUNT(alumnos_2.nombre) AS cantidad_alumnos,
            ROUND(AVG(alumnos_2.nota), 2) AS nota_media,
            ROUND(MAX(alumnos_2.nota), 2) AS nota_maxima,
            ROUND(MIN(alumnos_2.nota), 2) AS nota_minima
        FROM alumnos_2
        INNER JOIN cursos_2 ON alumnos_2.id_curso = cursos_2.id_curso
        GROUP BY cursos_2.nombre_curso
    """
    
    df = pd.read_sql_query(consulta, conn)
    conn.close()
    return df


def buscar_alumno_df(nombre_alumno):
    """
    Busca alumnos cuyo nombre contenga la cadena proporcionada.
    La búsqueda NO distingue mayúsculas/minúsculas (case-insensitive).
    
    Parámetros:
      nombre_alumno (str): texto a buscar (ej: "ana" encontrará "Ana", "ANA", etc.)
    
    Retorna:
      DataFrame con columnas: nombre, edad, nombre_curso, nota
      (vacío si no hay coincidencias)
    """
    conn = sqlite3.connect("alumnos_cursos.db")
    
    # LOWER(): convierte a minúsculas tanto en BD como en la entrada para comparación.
    # LIKE '%texto%': busca cualquier nombre que contenga 'texto'.
    consulta = """
        SELECT
            alumnos_2.nombre,
            alumnos_2.edad,
            cursos_2.nombre_curso,
            alumnos_2.nota
        FROM alumnos_2
        INNER JOIN cursos_2 ON alumnos_2.id_curso = cursos_2.id_curso
        WHERE LOWER(alumnos_2.nombre) LIKE LOWER(?)
    """
    
    # El % antes y después permite encontrar la cadena en cualquier posición.
    df = pd.read_sql_query(consulta, conn, params=(f"%{nombre_alumno}%",))
    conn.close()
    return df


def exportar_informe_csv():
    """
    Genera un archivo CSV con un informe completo de alumnos.
    
    El archivo se crea en la carpeta del proyecto con el nombre:
      'informe_alumnos_cursos.csv'
    """
    conn = sqlite3.connect("alumnos_cursos.db")
    
    consulta = """
        SELECT
            alumnos_2.nombre AS nombre_alumno,
            alumnos_2.edad,
            cursos_2.nombre_curso,
            alumnos_2.nota
        FROM alumnos_2
        INNER JOIN cursos_2 ON alumnos_2.id_curso = cursos_2.id_curso
        ORDER BY cursos_2.nombre_curso, alumnos_2.nota DESC
    """
    
    df = pd.read_sql_query(consulta, conn)
    
    # to_csv() guarda el DataFrame en un archivo CSV.
    # index=False: no incluye el índice de pandas en el archivo.
    df.to_csv("informe_alumnos_cursos.csv", index=False)
    
    conn.close()
    return True