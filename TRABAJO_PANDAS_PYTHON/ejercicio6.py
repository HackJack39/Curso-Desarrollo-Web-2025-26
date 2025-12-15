import pandas as pd

# Cargar ambos CSV

ventas = pd.read_csv('ventas.csv')
objetivos = pd.read_csv('objetivos.csv')

print("DataFrame Ventas:")
print(ventas)

# PASO 1: Merge (unión) por ID con how='left'

df_merged = pd.merge(ventas, objetivos, on='ID', how='left')
print("\nDataFrame después de merge:")
print(df_merged)

# PASO 2: Crear columna 'Cumplimiento' (%)

df_merged['Cumplimiento'] = (df_merged['Ventas'] / df_merged['Objetivo'] * 100).round(2)
print("\nDataFrame con columna 'Cumplimiento':")
print(df_merged)

# PASO 3: TOp 3 mejores cumplidores
print("\nTop 3 mejores cumplidores:")
print(df_merged.nlargest(3, 'Cumplimiento'))

# Información adicional
print('\nVendedores con objetivo (sin NaN):')
print(df_merged.dropna(subset=['Cumplimiento']))