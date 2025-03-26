import time
import sys
import random

# Duración en segundos antes de que el programa termine
tiempo_limite = 1836  # Puedes ajustar este valor según tus necesidades
print(f"El programa se cerrará automáticamente en 30 minutos.")

# Portada
print("******************************************")
print("*                                        *")
print("*          USMLE Simulación              *")
print("*                                        *")
print("*  Un examen para demostrar su           *")
print("*  competencia profesional               *")
print("*                                        *")
print("******************************************")
input("\nPresiona Enter para continuar...")

# Limpiar la pantalla y mover el cursor al inicio para la siguiente página
def limpiar_pantalla():
    print("\033[2J\033[H", end="")

limpiar_pantalla()

# Abrir y leer el archivo de preguntas
with open("Preguntas_largas.txt", "r", encoding='utf-8') as archivo:
    contenido = archivo.read().strip().split("\n\n")  # Divide las preguntas por bloques de líneas en blanco

# Mezclar las preguntas de manera aleatoria
random.shuffle(contenido)

# Solicitar el nombre del usuario
usuario = input("¿Nombre y apellido?")

# Inicializar el contador de respuestas correctas
respuestas_correctas = 0

# Registrar el tiempo de inicio
tiempo_inicio = time.time()

# Procesar cada pregunta y respuesta
for bloque in contenido:
    # Limpiar la pantalla antes de mostrar cada pregunta
    limpiar_pantalla()

    # Verificar si el tiempo límite ha sido alcanzado
    if time.time() - tiempo_inicio > tiempo_limite:
        print("¡Tiempo cumplido! El programa terminará ahora.")
        break

    lineas = bloque.split("\n")
    pregunta = lineas[0]
    opciones = lineas[1:-1]
    respuesta_correcta = lineas[-1].split(";")[-1].strip().strip('"')

    print(f"\n{pregunta}")
    for opcion in opciones:
        print(opcion)
    
    respuesta = input("Tu respuesta: ")

    if respuesta.upper() == respuesta_correcta:
        
        respuestas_correctas += 1
    else:
        print()

    

# Calcular porcentaje
porcentaje = respuestas_correctas / len(contenido) * 100
print(f"Porcentaje de respuestas correctas: {porcentaje:.2f}%")

# Guardar la puntuacion del usuario en un archivo
with open("scores.txt", "a", encoding='utf-8') as archivo_scores:
    archivo_scores.write(f"{usuario}: {porcentaje:.2f}% {respuestas_correctas} de {len(contenido)}\n")

# Esperar el tiempo especificado antes de cerrar el programa
time.sleep(5)
limpiar_pantalla()  # Limpiar la pantalla antes de cerrar el programa
print("¡Tiempo cumplido! El programa terminará ahora.")
sys.exit()  # Cierra el programa