import pandas as pd

# Cargar CSV desde archivo

df = pd.read_csv('empleados.csv')
print('DataFrame original:')
print(df)

# PASO 1: Rellenar valores faltantes (NaN)

df['Edad'].fillna(df['Edad'].mean(), inplace=True)
print('\nEdad despuçes de rellenar NaN')
print(df)

# PASO 2: Eliminar duplicados

df.drop_duplicates(subset=['Nombre'], inplace=True)
print('\nDataFrame después de eliminar duplicados:')
print(df)

# PASO 3: Cambiar tipo de datos

df['Edad'] = df['Edad'].astype(int)
print('\nInfo después de cambiar Edad a int:')
print(df.info())

# PASO 4: Guardar en CSV limpio

df.to_csv('empleados_limpio.csv', index=False)
print('\nArchivo empleados_limpio.csv guardado')