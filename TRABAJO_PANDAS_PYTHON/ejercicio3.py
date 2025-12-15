import pandas as pd

# Crear datos en un diccionario

data = {
    'Comercial' : ['Ana', 'Ana', 'Ana', 'Luis', 'Luis', 'Luis', 'Marta', 'Marta', 'Marta'],
    'Mes' : ['Ene', 'Feb', 'Mar', 'Ene', 'Feb', 'Mar', 'Ene', 'Feb', 'Mar'],
    'Ventas': [1000, 1200, 1100, 900, 950, 1000, 1300, 1250, 1400]
}

# Crear DataFrame a partir del diccionario
df = pd.DataFrame(data)

# Añadir columna nueva (operación vectorizada)

df['Comisión'] = df['Ventas'] * 0.05
print("DataFrame con Comisión:")
print(df)

# Eliminar columna (axis=1 significa columna, inplace=True modifica el DataFrame original)

df.drop('Comisión', axis=1, inplace=True)
print("\nDataFrame después de eliminar Comisión:")
print(df)

# Renombrar columna
df.rename(columns={'Ventas': 'Importe'}, inplace=True)
print("\nDataFrame con columna renombrada:")
print(df)