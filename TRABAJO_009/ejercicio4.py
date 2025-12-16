import pandas as pd
import sqlite3

# Suponemos que tenemos el df_limpio del ejercicio anterior
# Igualmente lo recreamos por si acaso

datos = {
    'Nombre': ['Ana', 'Carlos', 'Elena', 'Diego'],
    'Edad': [22, 25, 19, 23],
    'curso': ['Python', 'Python', 'JavaScript', 'JavaScript'],
    'nota': [8.5, 9.0, 7.8, 7.5]
    }

df = pd.DataFrame(datos)

# Paso 1: Crear conexión a la base de datos SQLite (en memoria para este ejemplo)
# Si el archivo no existe, se crea automáticamente

conexion = sqlite3.connect('alumnos.db')

# Paso 2: Crear la consulta SQL para crear la tabla
# SELECT: traer columnas específicas
# WHERE nota > 8: filtrar por nota
# ORDER BY nota DESC: ordenar descendente (mayor primero)

consulta = "SELECT Nombre, curso, nota " \
"FROM alumnos " \
"WHERE nota > 8 ORDER BY nota DESC"

# Paso 3: Ejecutar consulta y cargar en DataFrame
# pd.read_sql_query combina la consulta + conexión en un DataFrame

df_filtrado = pd.read_sql_query(consulta, conexion)
print("=== Alumnos con nota mayor a 8 ===")
print(df_filtrado)

# Paso 4: Calcular nota media de los filtrados
nota_media = df_filtrado['nota'].mean()
print(f"\n=== Nota media de los alumnos filtrados: {nota_media:.2f} ===")

# Información adicional
print("\nTotal de alumnos con nota superior a 8: ", len(df_filtrado))

# Cerrar conexión
conexion.close()