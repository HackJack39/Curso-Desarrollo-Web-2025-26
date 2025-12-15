print("--- EJERCICIO 6: Generadores (Yield) ---")

import sys

# Enfoque Clásico: Crear lista completa (Ocupa memoria)

def obtener_lista_cuadrados(n):
    resultado = []
    for i in range(n):
        resultado.append(i * i)
    return resultado 

# Enfoque Generador: Devuelve uno a uno (Ahorra memoria)

def generador_cuadrados(n):
    for i in range(n):
        yield i ** 2

CANTIDAD = 10000

# Comparamos tamaño en memoria (bytes)

lista = obtener_lista_cuadrados(CANTIDAD)
generador = generador_cuadrados(CANTIDAD)

print(f"Tamaño de la LISTA en memoria: {sys.getsizeof(lista)} bytes")
print(f"Tamaño del GENERADOR en memoria: {sys.getsizeof(generador)} bytes")
print("OBSERVACIÓN: ¡El generador es minúsculo porque no guarda los datos, los crea al vuelo!")

# Cómo usar el generador

print("\nPrimeros 3 valores usando el generador:")
print(next(generador))  # 0
print(next(generador))  # 1
print(next(generador))  # 4
print(next(generador))  # 9

for x in generador_cuadrados(15): 
    print(x)