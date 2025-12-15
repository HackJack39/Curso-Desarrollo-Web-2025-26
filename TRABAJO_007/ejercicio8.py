import threading
import time

print("\n--- EJERCICIO 8: Hilos (Threading) ---")

def descargar_archivo(nombre, segundos):
    print(f"[{nombre}] Iniciando descarga de {nombre} ({segundos})...")
    time.sleep(segundos)  # Simula el tiempo que tarda en descargar
    print(f"Descarga de {nombre} completada en {segundos} segundos.")


# Creamos los hilos

hilo1 = threading.Thread(target=descargar_archivo, args=("Foto.jpg", 7))
hilo2 = threading.Thread(target=descargar_archivo, args=("Video.mp4", 18))

print("--- Programa Principal: Lanzando hilos ---")
hilo1.start()
hilo2.start()

print("--- Programa Principal: ¡Yo sigo trabajando mientras ellos descargan ---")