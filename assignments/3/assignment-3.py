import math

import isa

import reentry

'''

fSpacecraftMassLbs = 2662.8 * 0.45359237
fReferenceArea = 2.81
fDragCoefficient = 1.60

fEarthMass = 5.972 * math.pow(10, 24)
fEarthRadius = 6371 * 1000

fInitialAltitudeFt = 325 * 1000 * 0.3048
fInitialVelocityFtPerSecond = 22.5 * 1000 * 0.3048
fFlightPathDeg = -1.5

'''

currentSimulation = ReEntry(fSpacecraftMassLbs, fReferenceArea, fDragCoefficient, fInitialAltitudeFt * 0.3048, fInitialVelocityFtPerSecond, fFlightPathDeg, fEarthMass, fEarthRadius)

currentSimulation.CalculateAccelerations(0.2)