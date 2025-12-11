print("\n--- EJERCICIO 3: Decoradores ---")

#Definimos el decorador
def mi_chivato(funcion):
    def envoltura(*args, **kwargs):
        print(f"[CHIVATO] Se va a ejecutar la función '{funcion.__name__}' con los argumentos {args} y {kwargs}")
        resultado = funcion(*args, **kwargs)
        print(f"[CHIVATO] La función '{funcion.__name__}' ha terminado de ejecutarse")
        return resultado
    return envoltura

# Usamos el decorador con @
@mi_chivato
def suma_pesada(a, b):
    return a + b

@mi_chivato
def saludar(nombre):
    print(f"Hola, {nombre}!")


# Probamos las funciones decoradas
x = suma_pesada(10, 20)
print(f"Resultado de la suma: {x}\n")
saludar("Estudiante")