import pygame
pygame.init()

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
clock.tick(60)

event = pygame.event.get()

def fin():
    out = False
    print ("a")
    if event.type == pygame.QUIT:
        print ("v")
        out = True
    return out

def game_intro():

    text1("Please enter your name: ",300,400) #example asking name / #variable enviada directamente al método text.

    inpt() #Here we are calling our function
    fin()

def text1(word,x,y):
    font = pygame.font.SysFont(None, 25)
    text = font.render("{}".format(word), True, (255, 0, 0))
    screen.blit(text,(x,y))

def inpt():
    word=""
    pygame.display.flip()

    xLetra, yLetra = 500, 400

    print ("antes" +str(xLetra)) 
    done = True
    while done:
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
        xLetra += 20
    print ("despues" + str(xLetra))
    return text1(word,xLetra,yLetra)

game_intro()