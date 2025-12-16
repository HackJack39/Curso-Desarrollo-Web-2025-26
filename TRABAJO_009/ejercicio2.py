import pandas as pd
import numpy as np

# Paso 1 y 2: Crear datos con problemas y cargar en DataFrame
# Simulamos un DataFrame con datos 'sucios'

datos_sucios = {
    'Nombre': ['Ana', 'Carlos', 'Elena', 'Diego', 'Ana'],
    'Edad': ['22', '25', '19', '23', '22'],
    'curso': ['Python', 'Python', 'JavaScript', 'JavaScript', 'Python'],
    'nota': [8.5, 9.0, np.nan, 7.5, 8.0]
    }

df = pd.DataFrame(datos_sucios)
print("=== DataFrame original con problemas ===")
print(df)
print(df.dtypes)

# Paso 3: Verificar valores faltantes
print("\n=== Valores faltantes por columna ===")
print(df.isnull().sum())

# Paso 4: Convertir edad a entero
df['Edad'] = pd.to_numeric(df['Edad'], errors='coerce').astype('Int64')
print("\n=== Después de convertir edad a entero ===")
print(df)
print(df.dtypes)

# Paso 5: Eliminar duplicados exactos
df_limpio = df.drop_duplicates()
print("\n=== DataFrame sin duplicados ===")
print(df_limpio)

# Paso 6: Nota media por curso
notas_por_curso = df_limpio.groupby('curso')['nota'].mean()
print("\n=== Nota media por curso ===")
print(notas_por_curso)

