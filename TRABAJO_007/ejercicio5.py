# Creamos una plantilla (clase) para crear múltiples objetos y entender cómo funciona __init__ y self.

print("--- EJERCICIO 5: Clases y Objetos ---")

class Robot:
    # El constructor: inicializa los atributos
    def __init__(self, nombre, bateria=100):
        self.nombre = nombre  # Atributo nombre
        self.bateria = bateria  # Atributo batería

    # Un método (acción)
    def saludar(self):
        if self.bateria > 0:
            print(f" [{self.nombre}] ¡Hola humanos! Mi batería está al {self.bateria}%.")
            self.bateria -= 10  # Disminuye la batería en 10% cada vez que saluda
        else:
            print(f" [{self.nombre}] No puedo saludar, mi batería está agotada.")


# Creamos dos instancias (objetos) diferentes

r1 = Robot("R2-D2")
r2 = Robot("C-3PO", bateria=20)

# Interactuamos con ellos
r1.saludar()  # R2-D2 saluda
r2.saludar()  # C-3PO saluda
r2.saludar()  # C-3PO intenta saludar de nuevo, pero su batería es baja
r2.saludar()  # Aquí C-3PO no podrá saludar más al quedarse sin batería

print(f"\nEstado final -> {r1.nombre}: {r1.bateria}%, {r2.nombre}: {r2.bateria}%")


