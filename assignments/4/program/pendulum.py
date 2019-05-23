import pygame
import math

class Pendulum:

    def __init__ (self, radius, length, ropeColor, ropeThickness, scale, gravity, initialAngle, screen, image):
        self.radius = radius
        self.length = length
        self.ropeColor = ropeColor
        self.ropeThickness = ropeThickness
        self.scale = scale
        self.gravity = gravity
        self.screen = screen
        self.screenWidth = pygame.display.get_surface().get_size()[0]
        self.image = pygame.transform.scale(image, (int(self.radius * 2 * self.scale), int(self.radius * 2 * self.scale)))

        self.angle = math.radians(initialAngle)
        self.angularVelocity = 0

        self.sprite = self.image.get_rect()

    def update (self, dt):
        self.angularVelocity -= self.gravity / self.length * math.sin(self.angle) * dt
        self.angle += self.angularVelocity * dt

        iHorizontalPosition = int(self.length * math.sin(self.angle) * self.scale + int(self.screenWidth / 2))
        iVerticalPosition = int(self.length * math.cos(self.angle) * self.scale)

        rotatedImage = pygame.transform.rotate(self.image, math.degrees(self.angle))

        self.sprite = rotatedImage.get_rect()
        self.sprite.centerx = iHorizontalPosition
        self.sprite.centery = iVerticalPosition

        self.screen.blit(rotatedImage, self.sprite)

        pygame.draw.line(self.screen, self.ropeColor, (int(self.screenWidth / 2), 0) , (iHorizontalPosition, iVerticalPosition), int(self.ropeThickness * self.scale))