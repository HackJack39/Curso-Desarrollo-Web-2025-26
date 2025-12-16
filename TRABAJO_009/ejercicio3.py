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

# Paso 2: Escribir el DataFrame en una tabla SQL
# if_exists='replace' para sobrescribir si ya existe la tabla
# index=False para no guardar el índice del DataFrame como columna adicional

df.to_sql('alumnos', conexion, if_exists='replace', index=False)
print("=== DataFrame guardado en la tabla 'alumnos' en alumnos.db ===")

# Paso 3: Verificar que la table se creó correctamente
# Ejecutamos una consulta SELECT simple

cursor = conexion.cursor()
cursor.execute("SELECT * FROM alumnos")
filas = cursor.fetchall()
print("\n=== Contenido de la tabla 'alumnos' ===")
for fila in filas:
    print(fila)

# También podemos verificar la estructura de la tabla
cursor.execute("PRAGMA table_info(alumnos)")
columnas = cursor.fetchall()
print("\n=== Estructura de la tabla 'alumnos' ===")
for col in columnas:
    print(col)

# Paso 4: Cerrar la conexión
conexion.close()
print("\nConexión cerrada.")

