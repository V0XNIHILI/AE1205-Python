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

        while fCurrentAltitude > 0:
            fCurrentDensity = isa.calculate(fCurrentAltitude)[2] # Density is the second column of the return contents of the ISA

            fGravitationalForce = self.getgravitationalforce(fCurrentAltitude)
            fDragForce = self.getdragforce(currentVelocity2D.length(), fCurrentDensity)

            fResultantX = - fDragForce * math.cos(math.radians(fCurrentFlightPath))
            fResultantY = - fDragForce * math.sin(math.radians(fCurrentFlightPath)) - fGravitationalForce

            currentAcceleration2D = Vector2D(fResultantX / self.objSpacecraft.mass, fResultantY / self.objSpacecraft.mass)
            currentVelocity2D = Vector2D(currentVelocity2D.x + currentAcceleration2D.x * timeInterval, currentVelocity2D.y + currentAcceleration2D.y * timeInterval)

            fCurrentAltitude += currentVelocity2D.y * timeInterval
            fCurrentFlightPath = math.degrees(math.atan(currentVelocity2D.y / currentVelocity2D.x))

            fCurrentTravelTime += timeInterval

            arrDataPoints.append([fCurrentTravelTime, currentAcceleration2D, currentVelocity2D, fCurrentAltitude, fCurrentFlightPath])

        return arrDataPoints

    def getgravitationalforce (self, altitude):
        return (6.6741 * math.pow(10, -11)) * self.objPlanet.mass * self.objSpacecraft.mass / math.pow((self.objPlanet.radius + altitude), 2)

    def getdragforce (self, velocity, density):
        return 0.5 * self.objSpacecraft.dragCoefficient * density * math.pow(velocity, 2) * self.objSpacecraft.frontalArea

class PathTravelled:
    def __init__ (self, dataPoints): # Should be in the same format as what ReEntry returns
        self.arrDataPoints = dataPoints

    def getvelocityataltitude (self, altitude):
        fSmallestSquaredDistanceToAltitude = math.pow((self.arrDataPoints[0][3] - altitude), 2)
        velocity2DAtAltitude = Vector2D(0, 0)

        for dataPoint in self.arrDataPoints:
            fSquaredAltitudeDistance = math.pow((dataPoint[3] - altitude), 2)
            if fSquaredAltitudeDistance < fSmallestSquaredDistanceToAltitude:
                fSmallestSquaredDistanceToAltitude = fSquaredAltitudeDistance
                velocity2DAtAltitude = dataPoint[2]

        return velocity2DAtAltitude