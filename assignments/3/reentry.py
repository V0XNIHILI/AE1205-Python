import isa
import math

class ReEntry:
    def __init__ (self, spacecraft, planet, initialAltitude, initialVelocity, initialFlightPath):
        self.objSpacecraft = spacecraft
        self.objPlanet = planet
        self.fInitialAltitude = initialAltitude
        self.fInitialVelocity = initialVelocity
        self.fInitialFlightPath = initialFlightPath

    def simulate(self, timeInterval):
        fCurrentAltitude = self.fInitialAltitude
        fCurrentFlightPath = self.fInitialFlightPath
        fCurrentVelocity = Vector2D(self.fInitialVelocity * math.cos(math.radians(fCurrentFlightPath)), self.fInitialVelocity * math.sin(math.radians(fCurrentFlightPath)))

        fCurrentTravelTime = 0

        while fCurrentAltitude > 1:
            fcurrentDensity = isa.calculate(fCurrentAltitude)[2] # Density is the second column of the return contents of the ISA

            # if 95.687
            
            fGravitationalForce = self.GetGravitationalForce(fCurrentAltitude)
            fDragForce = self.GetDragForce(fCurrentVelocity, fcurrentDensity)

            fResultantX = fDragForce * math.cos(math.radians(fCurrentFlightPath)) # To the right is positive
            fResultantY = fGravitationalForce - fDragForce * math.sin(math.radians(fCurrentFlightPath)) # Downwards is positive

            arrCurrentAcceleration = Vector2D(fResultantX / self.objSpacecraft.mass, fResultantY / self.objSpacecraft.mass)
            arrCurrentVelocity = Vector2D(arrCurrentVelocity.x + arrCurrentAcceleration.x * timeInterval, arrCurrentVelocity.y + arrCurrentAcceleration.y * timeInterval)

            fCurrentAltitude -= arrCurrentVelocity.y * timeInterval    # -= because re-entry means the spacecraft is going down
            fCurrentFlightPath = math.degrees(math.tanh(arrCurrentVelocity.y / arrCurrentVelocity.x))

            fCurrentTravelTime += timeInterval

            print(str(fCurrentTravelTime) + "/" + str(fCurrentVelocity))

    def getgravitationalforce (self, altitude):
        return (6.6741 * math.pow(10, -11)) * self.objPlanet.mass * self.objSpacecraft.mass / math.pow((self.objPlanet.radius + altitude), 2)

    def getdragforce (self, velocity, density):
        return 0.5 * self.objSpacecraft.dragCoefficient * density * math.pow(velocity, 2) * self.objSpacecraft.frontalArea

class Vector2D:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

class Spacecraft:
    def __init__ (self, mass, frontalArea, dragCoefficient):
        self.mass = mass
        self.frontalArea = frontalArea
        self.dragCoefficient = dragCoefficient

class Planet:
    def __init__ (self, mass, radius):
        self.mass = mass
        self.radius = radius
