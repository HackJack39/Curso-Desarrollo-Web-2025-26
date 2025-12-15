import pandas as pd

# Crear datos en un diccionario

data = {
    'Comercial' : ['Ana', 'Ana', 'Ana', 'Luis', 'Luis', 'Luis', 'Marta', 'Marta', 'Marta'],
    'Mes' : ['Ene', 'Feb', 'Mar', 'Ene', 'Feb', 'Mar', 'Ene', 'Feb', 'Mar'],
    'Importe': [1000, 1200, 1100, 900, 950, 1000, 1300, 1250, 1400]
}

# Crear DataFrame a partir del diccionario
df = pd.DataFrame(data)

# Agrupación por 'Comercial' y sumar de 'Importe'

totales = df.groupby('Comercial')['Importe'].sum()
print("\nTotales por Comercial:")
print(totales)

# Agrupación por 'Mes' y calcular media de 'Importe'

medias_mes = df.groupby('Mes')['Importe'].mean().round(2)
print("\nMedia de Importe por Mes:")
print(medias_mes)

# Múltiples agregaciones a la vez
# Primero creamos variable para poder redondear con dos decimales
mul_agr = df.groupby('Comercial')['Importe'].agg(['sum', 'mean', 'count', 'std'])
print("\nMúltiples estadísticas por Comercial:")
print(mul_agr.round(2))