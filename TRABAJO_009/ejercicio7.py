import pandas as pd
import sqlite3
from io import StringIO

# Paso 1: Crear datos CSV de prueba

datos_csv = """vendedor,fecha,importe,zona
Juan,2024-01-15,1500.50,Norte
María,2024-01-16,2300.00,Sur
Juan,2024-01-17,1800.75,Norte
Pedro,,950.25,Este
,2024-01-19,3200.00,Sur
María,2024-01-20,2150.00,Sur"""

# Paso 2: Cargar y limpiar con pandas

df_ventas = pd.read_csv(StringIO(datos_csv))
print("=== DataFrame original con problemas ===")
print(df_ventas)
print(f"\nValores faltantes: {df_ventas.isnull().sum().sum()}")

# Eliminar filas con valores faltantes

df_ventas = df_ventas.dropna()
print("\n=== DataFrame después de eliminar filas con valores faltantes ===")
print(df_ventas)

# Convertir fecha a tipo datetime

df_ventas['fecha'] = pd.to_datetime(df_ventas['fecha'])

# Convertir importe a float

df_ventas['importe'] = pd.to_numeric(df_ventas['importe'], errors='coerce')

print("\n=== Tipos de datos después de conversión ===")
print(df_ventas.dtypes)

# Paso 3: Guardar en SQLite
conexion = sqlite3.connect('ventas.db')
df_ventas.to_sql('ventas', conexion, if_exists='replace', index=False)
print("\nDatos guardados en la base de datos 'ventas.db' en la tabla 'ventas'.")

# Paso 4: Ejecutar consultas SQL
consulta_zona = """
SELECT
    zona,
    COUNT(*) as num_transacciones,
    ROUND(SUM(importe), 2) as ventas_totales,
    ROUND(AVG(importe), 2) as promedio_importe
FROM ventas
GROUP BY zona
ORDER BY ventas_totales DESC
"""

df_por_zona = pd.read_sql_query(consulta_zona, conexion)
print("\n=== Ventas por zona ===")
print(df_por_zona)

# Ventas por vendedor
consulta_vendedor = """
SELECT
    vendedor,
    COUNT(*) as num_ventas,
    ROUND(SUM(importe), 2) as total_vendido,
    ROUND(AVG(importe), 2) as promedio
FROM ventas
GROUP BY vendedor
ORDER BY total_vendido DESC
"""

df_por_vendedor = pd.read_sql_query(consulta_vendedor, conexion)
print("\n=== Ventas por vendedor ===")
print(df_por_vendedor)

# Paso 5: Exportar informes a CSV
df_por_zona.to_csv('informe_por_zona.csv', index=False)
df_por_vendedor.to_csv('informe_por_vendedor.csv', index=False)

print("\n Informes exportados:)")
print(" - informe_por_zona.csv")
print(" - informe_por_vendedor.csv")    

conexion.close()