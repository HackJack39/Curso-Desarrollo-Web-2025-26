import pandas as pd
import sqlite3
import time

conexion = sqlite3.connect('alumnos.db')

# ========= OPCIÓN A: GROUP BY en SQL =========

print("=== OPCIÓN A: GROUP BY en SQL ===")
inicio_a = time.time()

consulta_sql = """
SELECT
    c.nombre_curso,
    COUNT(a.nombre) as cantidad_alumnos,
    ROUND(AVG(a.nota), 2) as nota_media
FROM alumnos_cursos a
INNER JOIN cursos c ON a.id_curso = c.id_curso
GROUP BY c.nombre_curso
ORDER BY nota_media DESC
"""

df_sql = pd.read_sql_query(consulta_sql, conexion)
tiempo_a = time.time() - inicio_a

print("Resultado:")
print(df_sql)
print(f"Tiempo: {tiempo_a:.6f} segundos")

# ========= OPCIÓN B: GROUP BY en Pandas =========

print("\n=== OPCIÓN B: GROUP BY en Pandas ===")
inicio_b = time.time()

# Leer todos los datos primero

consulta_completa = """
SELECT
    a.nombre,
    c.nombre_curso,
    a.nota
FROM alumnos_cursos a
INNER JOIN cursos c ON a.id_curso = c.id_curso
"""

df_datos = pd.read_sql_query(consulta_completa, conexion)
df_pandas = df_datos.groupby('nombre_curso').agg({
    'nombre': 'count',
    'nota': 'mean'
}).round(2)

# Renombrar columnas para que coincidan

df_pandas.rename(columns={'nombre': 'cantidad_alumnos', 'nota': 'nota_media'}, inplace=True)

# Ordenar por nota_media descendente

df_pandas = df_pandas.sort_values(by='nota_media', ascending=False)

tiempo_b = time.time() - inicio_b

print("Resultado:")
print(df_pandas)
print(f"Tiempo: {tiempo_b:.6f} segundos")

# ========= COMPARACIÓN =========

print("\n=== COMPARACIÓN ===")
print(f"Opción A (SQL) fue {tiempo_b/tiempo_a:.2f} veces más rápida.")
print("\n Nota: En bases de datos pequeñas, la diferencia es mínima.")
print(" En grandes volúmenes de datos, GROUP BY en SQL suele ser más eficiente.")

conexion.close()
