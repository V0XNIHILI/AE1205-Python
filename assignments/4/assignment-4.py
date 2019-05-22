import pygame
import pygame.gfxdraw
import math
import colorsys

# Set constants
iFps = 120
fScale = 80 # 100 cm = 1 px
fGravitationalAcceleration = 9.80665
fPendulumLength = 4
fPendulumRadius = 0.5
fRopeThickness = 0.05
fInitialAngle = math.pi / 2.1

fCurrentAngle = fInitialAngle
fCurrentAngularVelocity = 0

pygame.init()

# Setup game window
iWidthOfGame = 800
iHeightOfGame = 500
gameSize = (iWidthOfGame, iHeightOfGame)

screen = pygame.display.set_mode(gameSize)
pygame.display.set_caption("Pendula by Douwe den Blanken")

# Import the pendulum
pendulumImage = pygame.image.load("miley.png")
pendulumImage = pygame.transform.scale(pendulumImage, (int(fPendulumRadius * 2 * fScale), int(fPendulumRadius * 2 * fScale)))
pendulumSprite = pendulumImage.get_rect()

# Get time it takes to initilize the game
iMillisecondsSinceInit = pygame.time.get_ticks()
iMaxRunTimeInSeconds = 260 + iMillisecondsSinceInit

# Make sure program runs at 60 fps
clock = pygame.time.Clock()

bUpdate = True

while bUpdate:
    if pygame.time.get_ticks() > iMaxRunTimeInSeconds*1000:
        bUpdate = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              bUpdate = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                bUpdate = False
              
    dt = clock.tick(iFps) / 1000

    fCurrentAngularVelocity -= fGravitationalAcceleration / fPendulumLength * math.sin(fCurrentAngle) * dt
    fCurrentAngle += fCurrentAngularVelocity * dt

    iHorizontalPosition = int(fPendulumLength * math.sin(fCurrentAngle) * fScale + iWidthOfGame / 2)
    iVerticalPosition = int(fPendulumLength * math.cos(fCurrentAngle) * fScale)

    # Change background color based on current angle of pendulum
    backgroundColor = colorsys.hsv_to_rgb(math.cos(fCurrentAngle*0.5), 1, 1)
    backgroundColor = (backgroundColor[0]*255, backgroundColor[1]*255, backgroundColor[2]*255)
    screen.fill(backgroundColor)

    pygame.draw.line(screen, (0,0,0), (int (iWidthOfGame / 2), 0) , (iHorizontalPosition, iVerticalPosition), int(fRopeThickness*fScale))
    
    rotatedPendulumImage = pygame.transform.rotate(pendulumImage, math.degrees(fCurrentAngle))
    screen.blit(rotatedPendulumImage, pendulumSprite)

    pendulumSprite.centerx = iHorizontalPosition
    pendulumSprite.centery = iVerticalPosition

    # Redraw the window
    pygame.display.flip()

pygame.quit()