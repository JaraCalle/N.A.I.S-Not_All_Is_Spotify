import pygame
import os
import time

def cargar_cancion(ruta_cancion):
    pygame.mixer.init()
    pygame.mixer.music.load(ruta_cancion)

def reproducir():
    pygame.mixer.music.play()

def pausar():
    pygame.mixer.music.pause()

def continuar():
    pygame.mixer.music.unpause()

def detener():
    pygame.mixer.music.stop()

def adelantar(segundos):
    tiempo_actual = pygame.mixer.music.get_pos() // 1000
    nuevo_tiempo = tiempo_actual + segundos
    pygame.mixer.music.set_pos(nuevo_tiempo)

if __name__ == "__main__":
    # Ruta de la canción que deseas reproducir
    ruta_cancion = "src/songs/cancion.mp3"

    # Comprueba si el archivo de la canción existe
    if os.path.exists(ruta_cancion):
        cargar_cancion(ruta_cancion)
        reproducir()

        while pygame.mixer.music.get_busy():
            # Controles avanzados
            accion = input("A: Adelantar, P: Pausar, C: Continuar, D: Detener, Q: Salir\n").upper()

            if accion == "A":
                segundos = int(input("Número de segundos para adelantar: "))
                adelantar(segundos)
            elif accion == "P":
                pausar()
                while True:
                    resume = input("Presiona 'C' para continuar o 'D' para detener: ").upper()
                    if resume == "C":
                        continuar()
                        break
                    elif resume == "D":
                        detener()
                        break
            elif accion == "D":
                detener()
                break
            elif accion == "Q":
                detener()
                break