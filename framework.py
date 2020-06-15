import pygame
import os

def obtenPath(directorio):
    pathFicheroScript = os.path.realpath(__file__)
    directorioTrabajo = os.path.dirname(pathFicheroScript)
    pathRecurso = os.path.join(directorioTrabajo, directorio)

    return pathRecurso

def obtenPathDeRecurso(directorio, elemento):
    path = obtenPath(directorio)
    return os.path.join(path, elemento)

class ventana():
    def __init__(self):
        self.ventana = pygame.display.set_mode((300, 500))
        self.reloj = pygame.time.Clock()

    def devolverVentana(self):
        return self.ventana

    def finalizar(self):
        global eventos #Hacer un global implica que la variable eventos exista solo 1 vez por lo que se reduce la cantidad de lag en el programa. (utlizada en la clase juego)
        eventos = pygame.event.get()

        out = False
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    out = True
            if event.type == pygame.QUIT:
                out = True

            return out
    
    def empezarFrame(self):
       self.reloj.tick(60)

    def acabarFrame(self):
        pygame.display.flip() #El flip se añade al finalizar el frame.

class juego():
    def __init__(self):
        self.teclaPresionada_a = None
        self.ventana = ventana().devolverVentana() #En el constructor de la clase juego debemos implementar la variable self.ventana para así poder utilizarla posteriormente.

    def login(self):
        rutaPantallaLogin = obtenPathDeRecurso("pantallas", "pantallaLogin.jpg")
        pantallaLogin = pygame.image.load(rutaPantallaLogin)

        self.ventana.blit((pantallaLogin), (0, 0))

        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.teclaPresionada_a = True

                else:
                    if event.key == pygame.K_BACKSPACE:
                        self.teclaPresionada_a = False
                        print ("BACKSPACE presionado")


    def dibuja(self):
        if self.teclaPresionada_a == True:
            rutaLetra_aRojo = obtenPathDeRecurso("imagenes", "letra_aRojo.png")
            letra_aRojo = pygame.image.load(rutaLetra_aRojo)

            self.ventana.blit( (letra_aRojo), (50, 350)) #Linea del error, solucionado.

            print ("TeclaPresionada")




