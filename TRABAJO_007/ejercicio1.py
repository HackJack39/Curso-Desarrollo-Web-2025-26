import copy

print("=== EJERCICIO 1: Shallow vs Deep Copy ===")

# Lista de inventario: [Producto, [Cantidad, Precio]]
inventario_original = ["Laptop", [10, 800]]

# 1. Hacemos una copia superficial
copia_superficial = copy.copy(inventario_original)

# 2. Hacemos una copia profunda
copia_profunda = copy.deepcopy(inventario_original)

# 3. Simulamos una venta en las copias
print(f"Original antes: {inventario_original}")

# Modificamos la cantidad en la copia superficial
copia_superficial[1][0] = 5 

# Modificamos la cantidad en la copia profunda
copia_profunda[1][0] = 0

print("\n--- Resultados tras modificar copias ---")
print(f"Copia Superficial: {copia_superficial} (Cantidad cambiada a 5)")
print(f"Copia Profunda: {copia_profunda} (Cantidad cambiada a 0)")
print(f"Original: {inventario_original}")
print("\nOBSERVACIÓN: ¡El original cambió a 5 por culpa de la copia superficial!")

