# ------------------------------------------------------
# Imports
# ------------------------------------------------------

import math

import isa

from reentry import ReEntry
from planet import Planet
from spacecraft import Spacecraft

import matplotlib.pyplot as plotter

# ------------------------------------------------------
# Define constants
# ------------------------------------------------------

fSpacecraftMassKg = 2662.8 * 0.45359237
fReferenceArea = 2.81
fDragCoefficient = 1.60

fEarthMass = 5.972 * math.pow(10, 24)
fEarthRadius = 6371 * 1000

fInitialAltitude = 325 * 1000 * 0.3048
fInitialVelocity = 22.5 * 1000 * 0.3048
fFlightPathDeg = 1.5

currentSpacecraft = Spacecraft(fSpacecraftMassKg, fReferenceArea, fDragCoefficient)
currentPlanet = Planet(fEarthMass, fEarthRadius)

# ------------------------------------------------------
# Run simulation
# ------------------------------------------------------

currentSimulation = ReEntry(currentSpacecraft, currentPlanet, fInitialAltitude, fInitialVelocity, fFlightPathDeg)

arrDatapointsFromSimulation = currentSimulation.simulate(0.2)

# ------------------------------------------------------
# Display plot of results
# ------------------------------------------------------

arrX = []
arrY = []

for dataPoint in arrDatapointsFromSimulation:
    arrX.append(dataPoint[3])
    arrY.append(dataPoint[2].x)

'''
for alt in range(0, 100*1000):
    arrY.append(alt)
    arrX.append(isa.calculate(alt)[0])
'''

plotter.plot(arrX, arrY)
plotter.show()