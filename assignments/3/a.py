import math

import isa

class ReEntry:
    def __init__ (self, spacecraftMass, referenceArea, dragCoefficient, initialAltitude, initialVelocity, initialFlightPath, planetMass, planetRadius):
        self.fSpacecraftMass = spacecraftMass
        self.fReferenceArea = referenceArea
        self.fDragCoefficient = dragCoefficient
        self.fInitialAltitude = initialAltitude
        self.fInitialVelocity = initialVelocity
        self.fInitialFlightPath = initialFlightPath
        self.fPlanetMass = planetMass
        self.fPlanetRadius = planetRadius

    def CalculateAccelerations(self, timeInterval):
        fCurrentAltitude = self.fInitialAltitude
        fCurrentVelocity = self.fInitialVelocity
        fCurrentFlightPath = self.fInitialFlightPath

        fCurrentTravelTime = 0

        while fCurrentAltitude > 1:
            fcurrentDensity = isa.calculate(fCurrentAltitude)[2] # Density is the second column of the return contents of the ISA

            fGravitationalForce = self.GetGravitationalForce()
            fDragForce = self.GetDragForce(fCurrentVelocity, fcurrentDensity)

            fCurrentAcceleration = (fGravitationalForce - fDragForce) / self.fSpacecraftMass
            fCurrentVelocity += fCurrentAcceleration * timeInterval
            fCurrentAltitude -= fCurrentVelocity * timeInterval

            fCurrentTravelTime += timeInterval

            print(str(fCurrentAltitude) + "/" + str(fCurrentVelocity))

    def GetGravitationalForce (self):
        return (6.6741 * math.pow(10, -11)) * self.fPlanetMass * self.fSpacecraftMass / math.pow((self.fPlanetRadius + self.fInitialAltitude), 2)

    def GetDragForce (self, currentVelocity, currentDensity):
        return 0.5 * self.fDragCoefficient * currentDensity * math.pow(currentVelocity, 2) * self.fReferenceArea

fSpacecraftMassLbs = 2662.8
fReferenceArea = 2.81
fDragCoefficient = 1.60

fLbsToKgFactor = 0.45359237
fGravityConstant = 6.6741 * math.pow(10, -11)
fEarthMass = 5.972 * math.pow(10, 24)
fEarthRadius = 6371 * 1000

fInitialAltitudeFt = 325 * 1000
fInitialVelocityFtPerSecond = 22.5 * 1000
fFlightPathDeg = -1.5

currentSimulation = ReEntry(fSpacecraftMassLbs * fLbsToKgFactor, fReferenceArea, fDragCoefficient, fInitialAltitudeFt * 0.3048, fInitialVelocityFtPerSecond * 0.3048, fFlightPathDeg, fEarthMass, fEarthRadius)

currentSimulation.CalculateAccelerations(0.2)