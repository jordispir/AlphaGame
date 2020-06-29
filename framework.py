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

class login():
    def __init__(self):
        self.teclaPresionada_a = None
        self.ventana = ventana().devolverVentana() #En el constructor de la clase juego debemos implementar la variable self.ventana para así poder utilizarla posteriormente.
        self.x, self.y = 100, 200
        self.listaLetras = []

    def logLetra(self, letraTecla):
        if self.x >= 500: #limitar el append de la lista hasta que la coordenada x sea mayor de 500.
            self.listaLetras.append(letraTecla)
        if self.x > 500:
            nombre = "".join(listaLetras) #.join sirve para concatenar la lista.
            print (nombre)

    def dibujaAlPulsar(self, word, x, y):
        print ("dibujoPulsando")
        font = pygame.font.SysFont(None, 25)
        letra = font.render("{}".format(word), True, (255, 0, 0))

        if x > 500: #limitar el dibujo de la coordenada x hasta que esta sea mayor de 500.
            self.ventana.blit(letra, (x, y))

    def dibuja():
        font = pygame.font.SysFont(None, 25)
        textInput, x2, y2 = "Please enter your name: ", 300, 400
        text = font.render("{}".format(textInput), True, (255, 0, 0))

        self.ventana.blit(text, (x2,y2))

    def inpt(self):
        print ("antes" + str(self.x)) 
        word=""
        done = True
        while done:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_a:
                        word+=str(chr(event.key))
                        login.logLetra(self, "a")
                        done = False
                    elif event.key == pygame.K_b:
                        word+=chr(event.key)
                        #logLetra("b")
                        done = False
                    elif event.key == pygame.K_c:
                        word+=chr(event.key)
                        #logLetra("c")
                        done = False
                    elif event.key == pygame.K_d:
                        word+=chr(event.key)
                        #logLetra("d")
                        done = False
                    elif event.key == pygame.K_e:
                        word+=chr(event.key)
                        #logLetra("e")
                        done = False
                    elif event.key == pygame.K_f:
                        word+=chr(event.key)
                        #logLetra("f")
                        done = False
                    elif event.key == pygame.K_g:
                        word+=chr(event.key)
                        #logLetra("g")
                        done = False
                    elif event.key == pygame.K_h:
                        word+=chr(event.key)
                        #logLetra("h")
                        done = False
                    elif event.key == pygame.K_i:
                        word+=chr(event.key)
                        #logLetra("i")
                        done = False
                    elif event.key == pygame.K_j:
                        word+=chr(event.key)
                        #logLetra("j")
                        done = False
                    elif event.key == pygame.K_k:
                        word+=chr(event.key)
                        #logLetra("k")
                        done = False
                    elif event.key == pygame.K_l:
                        word+=chr(event.key)
                        #logLetra("l")
                        done = False
                    elif event.key == pygame.K_m:
                        word+=chr(event.key)
                        #logLetra("m")
                        done = False
                    elif event.key == pygame.K_n:
                        word+=chr(event.key)
                        #logLetra("n")
                        done = False
                    elif event.key == pygame.K_o:
                        word+=chr(event.key)
                        #logLetra("o")
                        done = False
                    elif event.key == pygame.K_p:
                        word+=chr(event.key)
                        #logLetra("p")
                        done = False
                    elif event.key == pygame.K_q:
                        word+=chr(event.key)
                        #logLetra("q")
                        done = False
                    elif event.key == pygame.K_r:
                        word+=chr(event.key)
                        #logLetra("r")
                        done = False
                    elif event.key == pygame.K_s:
                        word+=chr(event.key)
                        #logLetra("s")
                        done = False
                    elif event.key == pygame.K_t:
                        word+=chr(event.key)
                        #logLetra("t")
                        done = False
                    elif event.key == pygame.K_u:
                        word+=chr(event.key)
                        #logLetra("u")
                        done = False
                    elif event.key == pygame.K_v:
                        word+=chr(event.key)
                        #logLetra("v")
                        done = False
                    elif event.key == pygame.K_w:
                        word+=chr(event.key)
                        #logLetra("w")
                        done = False
                    elif event.key == pygame.K_x:
                        word+=chr(event.key)
                        #logLetra("x")
                        done = False
                    elif event.key == pygame.K_y:
                        word+=chr(event.key)
                        l#ogLetra("y")
                        done = False
                    elif event.key == pygame.K_z:
                        #word+=chr(event.key)
                        logLetra("z")
                        done = False
                    elif event.key == pygame.K_SPACE:
                        word+=chr(event.key)
                        #logLetra(" ")
                        done = False
                    elif self.x > 500: #si la x es mayor de 500 puede borrar.
                        if event.key == pygame.K_BACKSPACE:
                            eliminarLetra(word, self.x, self.y)
                        self.x -= 10

                    #events...

        self.x += 10
        print ("despues" + str(self.x)) 
        return login.dibujaAlPulsar(self, word, self.x, self.y) #el return implica que no se ejecute el while

    """dibuja devuelve el valor tan solo cuando la tecla es pulsada, por lo tanto
       el método dibuja hará el blit cuando la tecla se pulse."""

    def loginPantalla(self):
        login.inpt(self)
            
            

    




