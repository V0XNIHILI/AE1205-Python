import pygame

from matrixoflife import MatrixOfLife

# Set constants
iEvolutionsPerSecond = 2
iWidthOfGame = 1000 
iHeightOfGame = 1000
iFieldWidth = 25
iFieldHeight = 25

currentLife = MatrixOfLife(iFieldWidth, iFieldHeight, True)

pygame.init()

# Block other events, so speed up program
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

# Setup game window
gameSize = (iWidthOfGame, iHeightOfGame)

screen = pygame.display.set_mode(gameSize)
screen.set_alpha(None)  # Disable transparancy for faster run time
pygame.display.set_caption("Douwe's Game of Life")

# Make sure program runs at 60 fps
clock = pygame.time.Clock()

# Calculate size of one cell
iCellWidth = int(iWidthOfGame/iFieldWidth)
iCellHeight = int(iHeightOfGame/iFieldHeight)

# Cell image
cellImage = pygame.image.load("rabbit.png")
cellImage = pygame.transform.scale(cellImage, (iCellWidth, iCellHeight))

bUpdate = True

while bUpdate:              
    dt = clock.tick(iEvolutionsPerSecond) / 1000

    screen.fill((0, 0, 0))

    currentLife.evolve()

    currentStateMatrix = currentLife.matrix
    
    for iCurrentWidth in range(currentStateMatrix.shape[0]):
        for iCurrentHeight in range(currentStateMatrix.shape[1]):
            if currentStateMatrix[iCurrentWidth, iCurrentHeight] == 1:
                #pygame.draw.rect(screen, (255, 255, 255), (iCellWidth*iCurrentWidth,iCellHeight*iCurrentHeight,iCellWidth,iCellHeight), 0)
                screen.blit(cellImage, (iCellWidth*iCurrentWidth,iCellHeight*iCurrentHeight))

    # Redraw the window
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              bUpdate = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                bUpdate = False

pygame.quit()