import pygame
pygame.init()

def game_intro():
    intro=True

    global screen
    screen = pygame.display.set_mode((1200, 800))
    global clock
    clock = pygame.time.Clock()

    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    intro=False
        inpt() #Here we are calling our function
        pygame.display.update()

        clock.tick(15)

def text1(word,x,y):
    font = pygame.font.SysFont(None, 25)
    text = font.render("{}".format(word), True, (255, 0, 0))
    return screen.blit(text,(x,y))

def inpt():
    word=""
    text1("Please enter your name: ",300,400) #example asking name
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    word+=str(chr(event.key))
                if event.key == pygame.K_b:
                    word+=chr(event.key)
                if event.key == pygame.K_c:
                    word+=chr(event.key)
                if event.key == pygame.K_d:
                    word+=chr(event.key)
                if event.key == pygame.K_RETURN:
                    done=False
                #events...
    print (word)
    return text1(word,700,30)

game_intro()