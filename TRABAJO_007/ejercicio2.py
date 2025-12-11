print("\n--- EJERCICIO 2: Tuplas vs Listas ---")

# Lista de tareas (mutable)
tareas = ["Estudiar", "Comer", "Dormir"]
tareas [1] = "Programar"
print(f"Lista de tareas modificada: {tareas}")

# Coordenadas GPS (Inmutable - Tupla)
coordenadas = (40.416, -3.703)

try:
    print("Intentando modificar la latitud de la tupla...")
    coordenadas[0] = 40.500  # Esto generará un error
except TypeError as e:
    print(f"ERROR CAPTURADO: {e}")
    print("¡Visual Studio Code te avisará de esto. Las tuplas no se tocan")
    print(f"Coordenadas GPS: {coordenadas}")