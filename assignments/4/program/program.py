import pygame
import colorsys
import math

from pendulum import Pendulum

# Set constants
iFps = 500
fScale = 200 # fScale number of pixels = 1 m, 15 pendula: 2000
fGravitationalAcceleration = 9.80665
fPendulumRadius = 0.7 # 15 pendula -> 0.04
fRopeThickness = 0.02 # 15 pendula -> 0.001
ropeColor = (112, 112, 112)
fInitialAngle = 45
fRainbowSpeed = 0.1
iRunTime = 260
iMaxAmountOfSwingsPerMinute = 21 # 15 pendula -> 65
iMinAmountOfSwingsPerMinute = 21 # 15 pendula -> 51
iWidthOfGame = 1200 
iHeightOfGame = 800

fCurrentAngle = fInitialAngle
fColorAngle = fCurrentAngle
fCurrentAngularVelocity = 0

pygame.init()

# Block other events, so speed up program
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

# Setup game window
gameSize = (iWidthOfGame, iHeightOfGame)

iHalfScreenWidth = int(iWidthOfGame / 2)

screen = pygame.display.set_mode(gameSize)
screen.set_alpha(None)  # Disable transparancy for faster run time
pygame.display.set_caption("Moving Miley by Douwe den Blanken")

# Play audio
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

# Import the pendulum
pendulumImage = pygame.image.load("miley-small.png")

pendula = []

for currentSwingsPerMinute in range(iMinAmountOfSwingsPerMinute, iMaxAmountOfSwingsPerMinute + 1):
    currentRopeLength = math.pow(((60/currentSwingsPerMinute) / (2 * math.pi)), 2) * fGravitationalAcceleration
    singlePendulum = Pendulum(fPendulumRadius, currentRopeLength, ropeColor, fRopeThickness, fScale, fGravitationalAcceleration, fInitialAngle, screen, pendulumImage)

    pendula.append(singlePendulum)

# Get time it takes to initilize the game
iMillisecondsSinceInit = pygame.time.get_ticks()
iMaxRunTimeInSeconds = iRunTime + iMillisecondsSinceInit

# Make sure program runs at 60 fps
clock = pygame.time.Clock()

bUpdate = True

while bUpdate:              
    dt = clock.tick(iFps) / 1000

    # Change background color based on current angle of pendulum
    fColorAngle += abs(fCurrentAngularVelocity) * dt
    backgroundColor = colorsys.hsv_to_rgb(abs(math.cos(pygame.time.get_ticks() / 1000 *fRainbowSpeed)), 1, 1)
    backgroundColor = (backgroundColor[0]*255, backgroundColor[1]*255, backgroundColor[2]*255)
    screen.fill(backgroundColor)

    for pendulum in pendula:
        pendulum.update(dt)

    # Redraw the window
    pygame.display.flip()

    if pygame.time.get_ticks() > iMaxRunTimeInSeconds*1000:
        bUpdate = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              bUpdate = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                bUpdate = False

pygame.quit()