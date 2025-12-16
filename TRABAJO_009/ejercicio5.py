import pandas as pd
import sqlite3

# Paso 1: Crear conexión
conexion = sqlite3.connect('alumnos.db')
cursor = conexion.cursor()

# Paso 2: Crear tabla 'cursos' si no existe
cursor.execute("""
DROP TABLE IF EXISTS cursos
""")

cursor.execute("""
CREATE TABLE cursos (
    id_curso INTEGER PRIMARY KEY,
    nombre_curso TEXT,
    horas INTEGER
)
""")

# Insertar datos de cursos
cursos_data = [
    (1, 'Python', 40),
    (2, 'JavaScript', 35)
]
cursor.executemany("INSERT INTO cursos VALUES (?, ?, ?)", cursos_data)

# Crear tabla de alumnos con id_curso
cursor.execute("""
DROP TABLE IF EXISTS alumnos_cursos
""")

cursor.execute("""
CREATE TABLE alumnos_cursos (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER,
    id_curso INTEGER,
    nota REAL,
               FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
)
""")

# Insertar datos de alumnos con id_curso
alumnos_data = [
    (1, 'Ana', 22, 1, 8.5),
    (2, 'Carlos', 25, 1, 9.0),
    (3, 'Elena', 19, 2, 7.8),
    (4, 'Diego', 23, 2, 7.5)
]
cursor.executemany("INSERT INTO alumnos_cursos VALUES (?, ?, ?, ?, ?)", alumnos_data)

conexion.commit()

print("Tablas creadas e insertadas correctamente.")

# Paso 3: Realizar JOIN

consulta_join = """
SELECT a.nombre, a.edad, c.nombre_curso, c.horas, a.nota
FROM alumnos_cursos a
INNER JOIN cursos c ON a.id_curso = c.id_curso
ORDER BY c.nombre_curso, a.nombre DESC
"""

# Paso 4: Cargar resultado en DataFrame
df_join = pd.read_sql_query(consulta_join, conexion)
print("\n=== Resultado del JOIN entre alumnos y cursos ===")
print(df_join)

# Calcular nota media por curso
print("\n=== Nota media por curso ===")
nota_por_curso = df_join.groupby('nombre_curso')['nota'].mean()
print(nota_por_curso)

# Calcular número de alumnos por curso
print("\n=== Número de alumnos por curso ===")
alumnos_por_curso = df_join.groupby('nombre_curso').size()
print(alumnos_por_curso)

# Cerrar conexión
conexion.close()
print("\nConexión cerrada.")

