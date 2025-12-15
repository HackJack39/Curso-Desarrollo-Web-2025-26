import pandas as pd

# Crear datos en un diccionario

data = {
    'Comercial' : ['Ana', 'Ana', 'Ana', 'Luis', 'Luis', 'Luis', 'Marta', 'Marta', 'Marta'],
    'Mes' : ['Ene', 'Feb', 'Mar', 'Ene', 'Feb', 'Mar', 'Ene', 'Feb', 'Mar'],
    'Ventas': [1000, 1200, 1100, 900, 950, 1000, 1300, 1250, 1400]
}

# Crear DataFrame a partir del diccionario
df = pd.DataFrame(data)

# Mostrar las primeras filas (por defecto 5)
print("Primeras filas:")
print(df.head())

# Información general del DataFrame: tipos, memoria, valores no nulos
print("\nInformación del DataFrame:")
print(df.info())

# Estadísticas descriptivas: media, std, min, max, percentiles
print("\nEstadísticas descriptivas:")
print(df.describe())