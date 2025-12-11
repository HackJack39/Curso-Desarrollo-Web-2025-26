import pandas as pd

print("\n--- EJERCICIO 4: Pandas Básico ---")

# 1. Crear datos ficticios
datos = {
    'Alumno': ['Ana', 'Luis', 'Marta', 'Pedro'],
    'Nota': [8.5, 4.0, 9.2, 6.5],
    'Aprobado': [True, False, True, True]
}

df = pd.DataFrame(datos)

# 2. Mostrar tabla completa
print("--- Tabla de Notas ---")
print(df)

# 3. Filtrar: ¿Quién tiene nota mayor a 8?
print("\n--- Alumnos Destacados (Nota > 8) ---")
destacados = df[df['Nota'] > 8]
print(destacados)

# 4. Estadísticas rápidas
promedio = df['Nota'].mean()
print(f"\nNota media de la clase: {promedio}")