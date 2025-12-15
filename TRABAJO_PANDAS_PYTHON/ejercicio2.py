import pandas as pd

# Crear datos en un diccionario

data = {
    'Comercial' : ['Ana', 'Ana', 'Ana', 'Luis', 'Luis', 'Luis', 'Marta', 'Marta', 'Marta'],
    'Mes' : ['Ene', 'Feb', 'Mar', 'Ene', 'Feb', 'Mar', 'Ene', 'Feb', 'Mar'],
    'Ventas': [1000, 1200, 1100, 900, 950, 1000, 1300, 1250, 1400]
}

# Crear DataFrame a partir del diccionario
df = pd.DataFrame(data)

# Filtrado booleano: devuelve True/False por cada fila
print("Ventas > 1100:")
print(df[df['Ventas'] > 1100])

# Filtrado + selección de columnas específicas
print("\nSolo Ana (Mes y Ventas):")
print(df[df['Comercial'] == 'Ana'][['Mes', 'Ventas']])