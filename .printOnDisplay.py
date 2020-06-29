import pygame

global x, y
x, y = 500, 400

global listLetras
listaLetras = []

pygame.init()

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
clock.tick(60)


def fin():
    out = False
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                out = True
        if event.type == pygame.QUIT:
            out = True

        return out

def game_intro():
    dibuja()
    while not fin():
        flip()
        inpt() #Here we are calling our function

def dibujaAlPulsar(word,x,y):
    print ("dibujoPulsando")
    font = pygame.font.SysFont(None, 25)
    letra = font.render("{}".format(word), True, (255, 0, 0))

    if x > 500: #limitar el dibujo de la coordenada x hasta que esta sea mayor de 500.
        screen.blit(letra, (x, y))

def dibuja():
    font = pygame.font.SysFont(None, 25)
    textInput, x2, y2 = "Please enter your name: ", 300, 400
    text = font.render("{}".format(textInput), True, (255, 0, 0))

    screen.blit(text, (x2,y2))

def logLetra(letraTecla):
    global listaLetras
    global nombre

    if x >= 500: #limitar el append de la lista hasta que la coordenada x sea mayor de 500.
        listaLetras.append(letraTecla)
    if x > 500:
        nombre = "".join(listaLetras) #.join sirve para concatenar la lista.
        print (nombre)

def eliminarLetra(word, x, y):
    global nombre
    colorNegro = (0,0,0)

    if x >= 500:
        pygame.draw.rect(screen, (colorNegro), (x, y, 20, 20))
        pygame.display.update() #actualiza únicamente esta parte del frame.

    if x >= 500:
        listaLetras.pop() #elimina el último caracter de la lista.


def flip():
    pygame.display.flip()

def inpt():
    global x, y
    print ("antes" + str(x)) 
    done = True
    word=""
    while done:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_a:
                    word+=str(chr(event.key))
                    logLetra("a")
                    done = False
                elif event.key == pygame.K_b:
                    word+=chr(event.key)
                    logLetra("b")
                    done = False
                elif event.key == pygame.K_c:
                    word+=chr(event.key)
                    logLetra("c")
                    done = False
                elif event.key == pygame.K_d:
                    word+=chr(event.key)
                    logLetra("d")
                    done = False
                elif event.key == pygame.K_e:
                    word+=chr(event.key)
                    logLetra("e")
                    done = False
                elif event.key == pygame.K_f:
                    word+=chr(event.key)
                    logLetra("f")
                    done = False
                elif event.key == pygame.K_g:
                    word+=chr(event.key)
                    logLetra("g")
                    done = False
                elif event.key == pygame.K_h:
                    word+=chr(event.key)
                    logLetra("h")
                    done = False
                elif event.key == pygame.K_i:
                    word+=chr(event.key)
                    logLetra("i")
                    done = False
                elif event.key == pygame.K_j:
                    word+=chr(event.key)
                    logLetra("j")
                    done = False
                elif event.key == pygame.K_k:
                    word+=chr(event.key)
                    logLetra("k")
                    done = False
                elif event.key == pygame.K_l:
                    word+=chr(event.key)
                    logLetra("l")
                    done = False
                elif event.key == pygame.K_m:
                    word+=chr(event.key)
                    logLetra("m")
                    done = False
                elif event.key == pygame.K_n:
                    word+=chr(event.key)
                    logLetra("n")
                    done = False
                elif event.key == pygame.K_o:
                    word+=chr(event.key)
                    logLetra("o")
                    done = False
                elif event.key == pygame.K_p:
                    word+=chr(event.key)
                    logLetra("p")
                    done = False
                elif event.key == pygame.K_q:
                    word+=chr(event.key)
                    logLetra("q")
                    done = False
                elif event.key == pygame.K_r:
                    word+=chr(event.key)
                    logLetra("r")
                    done = False
                elif event.key == pygame.K_s:
                    word+=chr(event.key)
                    logLetra("s")
                    done = False
                elif event.key == pygame.K_t:
                    word+=chr(event.key)
                    logLetra("t")
                    done = False
                elif event.key == pygame.K_u:
                    word+=chr(event.key)
                    logLetra("u")
                    done = False
                elif event.key == pygame.K_v:
                    word+=chr(event.key)
                    logLetra("v")
                    done = False
                elif event.key == pygame.K_w:
                    word+=chr(event.key)
                    logLetra("w")
                    done = False
                elif event.key == pygame.K_x:
                    word+=chr(event.key)
                    logLetra("x")
                    done = False
                elif event.key == pygame.K_y:
                    word+=chr(event.key)
                    logLetra("y")
                    done = False
                elif event.key == pygame.K_z:
                    word+=chr(event.key)
                    logLetra("z")
                    done = False
                elif event.key == pygame.K_SPACE:
                    word+=chr(event.key)
                    logLetra(" ")
                    done = False
                elif x > 500: #si la x es mayor de 500 puede borrar.
                    if event.key == pygame.K_BACKSPACE:
                        eliminarLetra(word, x, y)
                    x -= 10

                #events...

    x += 10
    print ("despues" + str(x)) 
    return dibujaAlPulsar(word, x, y) #el return implica que no se ejecute el while

    """dibuja devuelve el valor tan solo cuando la tecla es pulsada, por lo tanto
       el método dibuja hará el blit cuando la tecla se pulse."""

game_intro()

#TODO FIN NO SE EJECUTA. ---> OK
#TODO variable font dos veces definida ---> Está bien así.
#TODO variable xLetra augmenta y vuelve a su valor inicial. ---> OK
#TODO parametro x en el while de game_intro se repite por lo que nunca dejará de ser 500 --> OK 

#TODO printar nombre al eliminar letra. 