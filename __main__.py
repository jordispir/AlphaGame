import pygame
import framework

pygame.init()

Ventana = framework.ventana()
Login = framework.login()

while not Ventana.finalizar():
   Ventana.empezarFrame() 
   Login.loginPantalla()
   Ventana.acabarFrame()

pygame.quit()