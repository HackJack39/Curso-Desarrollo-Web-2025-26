print("--- EJERCICIO 7: Lambdas y Funcional ---")

precios_en_dolares =  [10, 25, 40, 5, 100]
TASA_CAMBIO = 0.92 # 1 USD = 0.92 EUR

# 1. MAP: Aplicar una transformación a toda la lista
# Usamos lambda para convertir a euros

precios_en_euros = list(map(lambda p: round(p * TASA_CAMBIO,2), precios_en_dolares))

# 2. FILTER: Filtrar elementos según una condición
# Usamos lambda para quedarnos solo con precios con coste menor a 20 euros

baratos = list(filter(lambda p: round(p < 20, 2) , precios_en_euros))

print(f"Precios originales ($): {precios_en_dolares}")
print(f"Precios convertidos (€): {precios_en_euros}")
print(f"Precios baratos (<20€): {baratos}")