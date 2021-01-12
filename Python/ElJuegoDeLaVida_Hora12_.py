import pygame
import numpy as np
import time

pygame.init()

size = width, height = 1000, 1000

NxC = 60
NyC = 60

DimCW = (width - 1)  / NxC
DimCH = (height - 1) / NyC

color = 25, 25, 25

screen = pygame.display.set_mode(size)

screen.fill(color)

#Randomizar el juego
#GameState = np.random.randint(0, 2, (NxC, NyC))

GameState = np.zeros((NxC, NyC))

#Automata movil
GameState[21, 21] = 1
GameState[22, 22] = 1
GameState[22, 23] = 1
GameState[21, 23] = 1
GameState[20, 23] = 1

pauseExect = False

while 1:

    newGameState = np.copy(GameState)

    screen.fill(color)

    time.sleep(0.1)

    ev = pygame.event.get()
     
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        mouseClick = pygame.mouse.get_pressed()
        
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / DimCW)), int(np.floor(posY / DimCH))
            newGameState[celX, celY] = not mouseClick[2]

    for y in range (0, NyC):
        for x in range (0, NxC):

            if not pauseExect:

                NumVec = GameState[(x-1) % NxC, (y-1) % NyC] + \
                         GameState[(x  ) % NxC, (y-1) % NyC] + \
                         GameState[(x+1) % NxC, (y-1) % NyC] + \
                         GameState[(x-1) % NxC, (y  ) % NyC] + \
                         GameState[(x+1) % NxC, (y  ) % NyC] + \
                         GameState[(x-1) % NxC, (y+1) % NyC] + \
                         GameState[(x  ) % NxC, (y+1) % NyC] + \
                         GameState[(x+1) % NxC, (y+1) % NyC]
           
                if GameState[x, y] == 1:
                    print(NumVec)

                # Una célula muerta con exactamente 3 células vecinas vivas "nace".
            
                if GameState[x, y] == 0 and NumVec == 3: 
                    newGameState[x, y] = 1 

                # Una célula viva con 2 o 3 células vecinas vivas sigue viva, en otro caso muere.
            
                elif GameState[x, y] == 1 and (NumVec < 2 or NumVec > 3):
                    newGameState[x, y] = 0


            poly = [((x    ) * DimCW, (y    ) * DimCH),
                    ((x + 1) * DimCW, (y    ) * DimCH),
                    ((x + 1) * DimCW, (y + 1) * DimCH),
                    ((x    ) * DimCW, (y + 1) * DimCH)]
            
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (160, 160, 160), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    GameState = newGameState

    pygame.display.flip()