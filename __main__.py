import pygame
import framework

pygame.init()

Ventana = framework.ventana()
Juego = framework.juego()

while not Ventana.finalizar():
   Ventana.empezarFrame() 
   Juego.login()
   Juego.dibuja()
   Ventana.acabarFrame()

pygame.quit()