# ------------------------------------------------------
# Imports
# ------------------------------------------------------

import pygame
import math
import colorsys

from matrixoflife import MatrixOfLife
from input import Input

# ------------------------------------------------------
# Terminal Setup
# ------------------------------------------------------

print("")
print("=============================")
print("| V0X's Matrix Of Life Game |")
print("=============================")
print("\nLast edited on 4 June 2019")
print("\n-----------------------------\n")

# ------------------------------------------------------
# Define constants
# ------------------------------------------------------

iEvolutionsPerSecond = 9
iTransparancy = 64 # between 0 and 255, lower means cells stay visible longer
fRainbowSpeed = 0.5
enableRainbow = True
iWidthOfGame = 1000
iHeightOfGame = 1000
iFieldWidth = 100
iFieldHeight = 100

# ------------------------------------------------------
# Ask for user preferred setup
# ------------------------------------------------------

currentLife = None

loadFile = Input.IsTrue(Input.Ask("Do you want to load a custom .LIFE file? (y/n)", ["y", "n"]))

if loadFile == True:
    lifFile = open("test.LIF", "r")

    currentLife = MatrixOfLife(iFieldWidth, iFieldHeight, False)
    currentLife.loadlife(lifFile.readlines())

else:
    currentLife = MatrixOfLife(iFieldWidth, iFieldHeight, True)

# ------------------------------------------------------
# Method to redraw the cell
# ------------------------------------------------------

def drawCell(currentWidth, currentHeight, color):
    currentCell = pygame.Surface((iCellWidth, iCellHeight))  # The size of one cell
    currentCell.set_alpha(iTransparancy)    # Alpha level

    currentCell.fill(color)

    screen.blit(currentCell, (iCellWidth*currentWidth,iCellHeight*currentHeight,iCellWidth,iCellHeight))    # (0,0) are the top-left coordinates

# ------------------------------------------------------
# Start the game window
# ------------------------------------------------------

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

# Play music
pygame.mixer.music.load("music.mp3") # Syncs to beat when iEvolutionsPerSecond = 6
pygame.mixer.music.play(-1)

screen.fill((0,0,0))

bUpdate = True

while bUpdate:              
    dt = clock.tick(iEvolutionsPerSecond) / 1000

    # Enable if you don't want trails
    # screen.fill((255, 255, 255))

    currentLife.evolve()

    currentStateMatrix = currentLife.matrix

    aliveColor = (255, 255, 255)

    # Get new rainbow color for the current redraw
    if enableRainbow == True:
        aliveColor = colorsys.hsv_to_rgb(abs(math.cos(pygame.time.get_ticks() / 1000 * fRainbowSpeed)), 1, 1)
        aliveColor = (aliveColor[0]*255, aliveColor[1]*255, aliveColor[2]*255)
    
    for iCurrentWidth in range(currentStateMatrix.shape[0]):
        for iCurrentHeight in range(currentStateMatrix.shape[1]):
            if currentStateMatrix[iCurrentWidth, iCurrentHeight] == 1:
                drawCell(iCurrentWidth, iCurrentHeight, aliveColor)
            else:
                drawCell(iCurrentWidth, iCurrentHeight, (0,0,0))

    # Redraw the window
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              bUpdate = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                bUpdate = False

pygame.quit()