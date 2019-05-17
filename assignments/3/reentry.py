import isa
import math

from planet import Planet
from spacecraft import Spacecraft
from vector2d import Vector2D

class ReEntry:
    def __init__ (self, spacecraft, planet, initialAltitude, initialVelocity, initialFlightPath, drogueChute, mainChute):
        self.objSpacecraft = spacecraft
        self.objPlanet = planet
        self.fInitialAltitude = initialAltitude
        self.fInitialVelocity = initialVelocity
        self.fInitialFlightPath = initialFlightPath
        self.objDrogueChute = drogueChute
        self.objMainChute = mainChute

    def simulate(self, timeInterval, withParachutes):
        fCurrentAltitude = self.fInitialAltitude
        fHorizontalDistanceTravelled = 0
        fCurrentFlightPath = self.fInitialFlightPath
        currentVelocity2D = Vector2D(self.fInitialVelocity * math.cos(math.radians(fCurrentFlightPath)), self.fInitialVelocity * math.sin(math.radians(fCurrentFlightPath)))

        arrDataPoints = []

        fCurrentTravelTime = 0

        while fCurrentAltitude > 0:
            fCurrentDensity = isa.calculate(fCurrentAltitude)[2] # Density is the second column of the return contents of the ISA

            fGravitationalForce = self.getgravitationalforce(fCurrentAltitude)

            fCurrentSpeed = currentVelocity2D.length()
            
            fParachuteDrag = 0

            if withParachutes == True:
                if fCurrentSpeed < self.objDrogueChute.openingSpeed:
                    fParachuteDrag = self.getdragforce(self.objDrogueChute.dragCoefficient, fCurrentSpeed, fCurrentDensity, self.objDrogueChute.frontalArea)

                if fCurrentAltitude < self.objMainChute.openingAltitude:
                     fParachuteDrag = self.getdragforce(self.objMainChute.dragCoefficient, fCurrentSpeed, fCurrentDensity, self.objMainChute.frontalArea)

            fDragForce = self.getdragforce(self.objSpacecraft.dragCoefficient, fCurrentSpeed, fCurrentDensity, self.objSpacecraft.frontalArea)

            fResultantX = - (fDragForce + fParachuteDrag) * math.cos(math.radians(fCurrentFlightPath))
            fResultantY = - (fDragForce + fParachuteDrag) * math.sin(math.radians(fCurrentFlightPath)) - fGravitationalForce

            currentAcceleration2D = Vector2D(fResultantX / self.objSpacecraft.mass, fResultantY / self.objSpacecraft.mass)
            currentVelocity2D = Vector2D(currentVelocity2D.x + currentAcceleration2D.x * timeInterval, currentVelocity2D.y + currentAcceleration2D.y * timeInterval)

            fCurrentAltitude += currentVelocity2D.y * timeInterval
            fHorizontalDistanceTravelled += currentVelocity2D.x * timeInterval
            fCurrentFlightPath = math.degrees(math.atan(currentVelocity2D.y / currentVelocity2D.x))
            
            fCurrentTravelTime += timeInterval

            arrDataPoints.append([fCurrentTravelTime, currentAcceleration2D, currentVelocity2D, fCurrentAltitude, fHorizontalDistanceTravelled, fCurrentFlightPath])

        return arrDataPoints

    def getgravitationalforce (self, altitude):
        return (6.6741 * math.pow(10, -11)) * self.objPlanet.mass * self.objSpacecraft.mass / math.pow((self.objPlanet.radius + altitude), 2)

    def getdragforce (self, dragCoefficient, velocity, density, frontalArea):
        return 0.5 * dragCoefficient * density * math.pow(velocity, 2) * frontalArea

class PathTravelled:
    def __init__ (self, dataPoints): # Should be in the same format as what ReEntry returns
        self.arrDataPoints = dataPoints

    def getdatapointataltitude (self, altitude):
        fSmallestSquaredDistanceToAltitude = math.pow((self.arrDataPoints[0][3] - altitude), 2)
        dataPointAtAltitude = None

        for dataPoint in self.arrDataPoints:
            fSquaredAltitudeDistance = math.pow((dataPoint[3] - altitude), 2)
            if fSquaredAltitudeDistance < fSmallestSquaredDistanceToAltitude:
                fSmallestSquaredDistanceToAltitude = fSquaredAltitudeDistance
                dataPointAtAltitude = dataPoint

        return dataPointAtAltitude

    def getdatapointatspeed (self, speed):
        fSmallestSquaredDistanceToSpeed = math.pow((self.arrDataPoints[0][2].length() - speed), 2)
        dataPointAtSpeed = None

        for dataPoint in self.arrDataPoints:
            fSquaredSpeedDifference = math.pow((dataPoint[2].length() - speed), 2)
            if fSquaredSpeedDifference < fSmallestSquaredDistanceToSpeed:
                fSmallestSquaredDistanceToSpeed = fSquaredSpeedDifference
                dataPointAtSpeed = dataPoint

        return dataPointAtSpeed

    def getaltitudesinkft (self):
        arrAltitudesInKFt = []

        for dataPoint in self.arrDataPoints:
            arrAltitudesInKFt.append(dataPoint[3]/0.3048/1000)

        return arrAltitudesInKFt

    def getspeedsinkft (self):
        arrSpeedsInKFt = []

        for dataPoint in self.arrDataPoints:
            arrSpeedsInKFt.append(dataPoint[2].length()/0.3048/1000)

        return arrSpeedsInKFt

    def getgforces (self):
        arrGForces = []

        for dataPoint in self.arrDataPoints:
            arrGForces.append(dataPoint[1].y/9.980665)

        return arrGForces

    def gethorizontaldistancesfromimpactpointinkm (self):
        arrHorizontalDistancesInKm = []

        fTotalHorizontalDistanceTravelled = self.arrDataPoints[len(self.arrDataPoints)-1][4]/1000

        for dataPoint in self.arrDataPoints:
            arrHorizontalDistancesInKm.append(fTotalHorizontalDistanceTravelled - dataPoint[4]/1000)

        return arrHorizontalDistancesInKm

    def gettimesinsec (self):
        arrTimesInSec = []

        for dataPoint in self.arrDataPoints:
            arrTimesInSec.append(dataPoint[0])

        return arrTimesInSec

    def gettimesinminutes (self):
        arrTimesInMinutes = []

        for dataPoint in self.arrDataPoints:
            arrTimesInMinutes.append(dataPoint[0]/60)

        return arrTimesInMinutes

    def getflightpathangles (self):
        arrFlightPathAngles = []

        for dataPoint in self.arrDataPoints:
            arrFlightPathAngles.append(dataPoint[5] )

        return arrFlightPathAngles