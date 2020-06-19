import pygame
pygame.init()

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
clock.tick(60)


"""  global eventos #Hacer un global implica que la variable eventos exista solo 1 vez por lo que se reduce la cantidad de lag en el programa. (utlizada en la clase juego)
    eventos = pygame.event.get()

    out = False
    for event in eventos:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                out = True
        if event.type == pygame.QUIT:
            out = True

        return out """

def fin():
    event = pygame.event.poll()
    print ("event")
    if event.type == pygame.KEYDOWN:
        print ("event2")
        if event.key == pygame.K_ESCAPE:
            print ("event3")
            out = True 

        return out

def game_intro():
    xLetra, yLetra = 500, 400
    while not fin():
        dibuja()
        flip()
        inpt(xLetra) #Here we are calling our function

#def returnCoordenadas():
    #return xLetra, yLetra

def dibujaAlPulsar(word,x,y):
    print ("dibujoPulsando")
    font = pygame.font.SysFont(None, 25)
    letra = font.render("{}".format(word), True, (255, 0, 0))
    screen.blit(letra, (x, y))

    """ print ("for")
        listaLetra = []
    for i in listaLetra:
        print ("B")
        listaLetra.append(letra)
        print ("A")
        screen.blit(letra,(x + 20,y))"""

def dibuja():
    font = pygame.font.SysFont(None, 25)
    textInput, x2, y2 = "Please enter your name: ", 300, 400
    text = font.render("{}".format(textInput), True, (255, 0, 0))

    screen.blit(text, (x2,y2))

def flip():
    pygame.display.flip()

def inpt(x):

    print ("antes" + str(x)) 
    done = True
    word=""
    while done:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    word+=str(chr(event.key))
                    done = False
                if event.key == pygame.K_b:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_c:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_d:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_e:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_f:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_g:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_h:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_i:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_j:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_k:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_l:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_m:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_n:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_o:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_p:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_q:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_r:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_s:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_t:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_v:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_w:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_x:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_y:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_z:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_SPACE:
                    word+=chr(event.key)
                    done = False
                if event.key == pygame.K_BACKSPACE:
                    word+=chr(event.key)
                    done = False

                #events...

    if done == False: 
        x += 20
        print ("despues" + str(x)) 
    if x == x + 20:
        print ("if x == x + 20 = " +str(x))
        return dibujaAlPulsar(word, x, yLetra) #el return implica que no se ejecute el while

    """dibuja devuelve el valor tan solo cuando la tecla es pulsada, por lo tanto
       el método dibuja hará el blit cuando la tecla se pulse."""

game_intro()

#TODO FIN NO SE EJECUTA.
#TODO variable font dos veces definida
#TODO variable xLetra augmenta y vuelve a su valor inicial
#TODO parametro x en el while de game_intro se repite por lo que nunca dejará de ser 500