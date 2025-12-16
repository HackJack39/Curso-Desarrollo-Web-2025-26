# Importar pandas

import pandas as pd

# Paso 1: Crear el DataFrame con un diccionario
# Las claves del diccionario serán los nombres de las columnas

datos = {
    'Nombre': ['Ana', 'Carlos', 'Elena', 'Diego'],
    'Edad': [22, 25, 19, 23],
    'curso': ['Python', 'Python', 'JavaScript', 'JavaScript']
    }

# Crear el DataFrame a partir del diccionario
df = pd.DataFrame(datos)

# Paso 2: Mostrar las primeras filas
print("=== Primeras filas del DataFrame ===")
print(df.head())

# Paso 3: Información general del DataFrame
print("\n=== Información del DataFrame ===")
print(df.info())

# Paso 4: Estadísticas descriptivas (solo para columnas numéricas
print("\n=== Estadísticas descriptivas ===")
print(df.describe())

# Paso 5: Filtrar alumnos mayores de 20 años
# Usamos una condición booleana: df['edad] > 20
mayores_20 = df[df['Edad'] > 20]
print("\n=== Alumnos mayores de 20 años ===")
print(mayores_20)

# Paso 6: Filtrar alumnos que cursan Python
# Usamos == para comparar exactamente
python_students = df[df['curso'] == 'Python']
print("\n=== Alumnos que cursan Python ===")
print(python_students)