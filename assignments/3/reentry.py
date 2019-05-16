import isa
import math

from planet import Planet
from spacecraft import Spacecraft
from vector2d import Vector2D

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
        currentVelocity2D = Vector2D(self.fInitialVelocity * math.cos(math.radians(fCurrentFlightPath)), self.fInitialVelocity * math.sin(math.radians(fCurrentFlightPath)))
        
        arrDataPoints = []

        fCurrentTravelTime = 0

        while fCurrentAltitude > 15*1000:
            fCurrentDensity = isa.calculate(fCurrentAltitude)[2] # Density is the second column of the return contents of the ISA

            fGravitationalForce = self.getgravitationalforce(fCurrentAltitude)
            fDragForce = self.getdragforce(currentVelocity2D.length(), fCurrentDensity)

            fResultantX = -fDragForce * math.cos(math.radians(fCurrentFlightPath)) # -fDragForce #* math.cos(math.radians(fCurrentFlightPath)) # To the right is positive
            fResultantY = fGravitationalForce - fDragForce * math.sin(math.radians(fCurrentFlightPath)) # Downwards is positive

            currentAcceleration2D = Vector2D(fResultantX / self.objSpacecraft.mass, fResultantY / self.objSpacecraft.mass)
            currentVelocity2D = Vector2D(currentVelocity2D.x + currentAcceleration2D.x * timeInterval, currentVelocity2D.y + currentAcceleration2D.y * timeInterval)
            
            fCurrentAltitude -= currentVelocity2D.y * timeInterval    # -= because re-entry means the spacecraft is going down
            fCurrentFlightPath = math.degrees(math.tanh(currentVelocity2D.y / currentVelocity2D.x))

            fCurrentTravelTime += timeInterval

            arrDataPoints.append([fCurrentTravelTime, currentAcceleration2D, currentVelocity2D, fCurrentAltitude, fCurrentFlightPath, fCurrentDensity])

        return arrDataPoints

    def getgravitationalforce (self, altitude):
        return (6.6741 * math.pow(10, -11)) * self.objPlanet.mass * self.objSpacecraft.mass / math.pow((self.objPlanet.radius + altitude), 2)

    def getdragforce (self, velocity, density):
        return 0.5 * self.objSpacecraft.dragCoefficient * density * math.pow(velocity, 2) * self.objSpacecraft.frontalArea