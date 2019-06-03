import pygame
import math
import colorsys

from matrixoflife import MatrixOfLife

# Set constants
iEvolutionsPerSecond = 6
iTransparancy = 64 # between 0 and 255, lower means cells stay visible longer
fRainbowSpeed = 0.5
iWidthOfGame = 1000 
iHeightOfGame = 1000
iFieldWidth = 100
iFieldHeight = 100

currentLife = MatrixOfLife(iFieldWidth, iFieldHeight, True)

pygame.init()

# Block other events, so speed up program
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

# Setup game window
gameSize = (iWidthOfGame, iHeightOfGame)

screen = pygame.display.set_mode(gameSize)
pygame.display.set_caption("Douwe's Game of Life")

# Make sure program runs at 60 fps
clock = pygame.time.Clock()

# Calculate size of one cell
iCellWidth = int(iWidthOfGame/iFieldWidth)
iCellHeight = int(iHeightOfGame/iFieldHeight)

# ----> Enable for rabbits accross the screen
#cellImage = pygame.image.load("rabbit.png")
#cellImage = pygame.transform.scale(cellImage, (iCellWidth, iCellHeight))
# ----> Enable for rabbits accross the screen

# Play music
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

screen.fill((0,0,0))

bUpdate = True

while bUpdate:              
    dt = clock.tick(iEvolutionsPerSecond) / 1000

    # Enable if you don't want trails
    # screen.fill((255, 255, 255))

    currentLife.evolve()

    currentStateMatrix = currentLife.matrix
    
    for iCurrentWidth in range(currentStateMatrix.shape[0]):
        for iCurrentHeight in range(currentStateMatrix.shape[1]):
            if currentStateMatrix[iCurrentWidth, iCurrentHeight] == 1:
                # ----> Enable for simple black and white dots
                #pygame.draw.rect(screen, (0, 0, 0, 128), (iCellWidth*iCurrentWidth,iCellHeight*iCurrentHeight,iCellWidth,iCellHeight), 0)
                # ----> Enable for simple black and white dots
                
                # ----> Enable for rabbits accross the screen
                #screen.blit(cellImage, (iCellWidth*iCurrentWidth,iCellHeight*iCurrentHeight))
                # ----> Enable for rabbits accross the screen
                
                # ----> Enable for making the cell trails visible
                aliveColor = colorsys.hsv_to_rgb(abs(math.cos(pygame.time.get_ticks() / 1000 * fRainbowSpeed)), 1, 1)
                aliveColor = (aliveColor[0]*255, aliveColor[1]*255, aliveColor[2]*255)

                currentCell = pygame.Surface((iCellWidth, iCellHeight))  # the size of your rect
                currentCell.set_alpha(iTransparancy)                # alpha level
                currentCell.fill(aliveColor)           # this fills the entire surface
                screen.blit(currentCell, (iCellWidth*iCurrentWidth,iCellHeight*iCurrentHeight,iCellWidth,iCellHeight))    # (0,0) are the top-left coordinates

            else:
                # Enable for making the cell trails visible
                currentCell = pygame.Surface((iCellWidth, iCellHeight))  # the size of your rect
                currentCell.set_alpha(iTransparancy)                # alpha level
                currentCell.fill((0,0,0))           # this fills the entire surface
                screen.blit(currentCell, (iCellWidth*iCurrentWidth,iCellHeight*iCurrentHeight,iCellWidth,iCellHeight))    # (0,0) are the top-left coordinates
                # ----> Enable for making the cell trails visible

    # Redraw the window
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              bUpdate = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                bUpdate = False

pygame.quit()