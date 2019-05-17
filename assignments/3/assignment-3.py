# ------------------------------------------------------
# Imports
# ------------------------------------------------------

import math

import isa

from reentry import ReEntry, PathTravelled
from planet import Planet
from spacecraft import Spacecraft

import matplotlib.pyplot as plotter

# ------------------------------------------------------
# Terminal Setup
# ------------------------------------------------------

print("")
print("=============================")
print("| V0X's Re-entry Calculator |")
print("=============================")
print("\nLast edited on 17 May 2019")
print("\n-----------------------------\n")

# ------------------------------------------------------
# Define constants
# ------------------------------------------------------

# All of these values where given in the exercise
fSpacecraftMassKg = 2662.8 * 0.45359237
fReferenceArea = 2.81
fDragCoefficient = 1.60

fEarthMass = 5.972 * math.pow(10, 24)
fEarthRadius = 6371 * 1000

fInitialAltitude = 325 * 1000 * 0.3048
fInitialVelocity = 22.5 * 1000 * 0.3048
fFlightPathDeg = -1.5

# Create spacecraft and planet objects with their respective properties
currentSpacecraft = Spacecraft(fSpacecraftMassKg, fReferenceArea, fDragCoefficient)
currentPlanet = Planet(fEarthMass, fEarthRadius)

# ------------------------------------------------------
# Simulate the whole thing
# ------------------------------------------------------

# Create, run and save the simulation
currentSimulation = ReEntry(currentSpacecraft, currentPlanet, fInitialAltitude, fInitialVelocity, fFlightPathDeg)
arrDatapointsFromSimulation = currentSimulation.simulate(0.1)
travelledPath = PathTravelled(arrDatapointsFromSimulation)

# ------------------------------------------------------
# Write required output to console
# ------------------------------------------------------

velocity2DAt32Km = travelledPath.getvelocityataltitude(32*1000)
velocity2DAt11Km = travelledPath.getvelocityataltitude(11*1000)
velocity2DAt0Km = travelledPath.getvelocityataltitude(0)

print("> Velocity at 32,000 [m]:\n\n" + "x:       " + str(round(velocity2DAt32Km.x, 1)) + " [m/s]\ny:       " + str(round(velocity2DAt32Km.y, 1)) + " [m/s]\nTotal:   " + str(round(velocity2DAt32Km.length(), 1))  + " [m/s]\n")
print("> Velocity at 11,000 [m]:\n\n" + "x:       " + str(round(velocity2DAt11Km.x, 1)) + " [m/s]\ny:       " + str(round(velocity2DAt11Km.y, 1)) + " [m/s]\nTotal:   " + str(round(velocity2DAt11Km.length(), 1))  + " [m/s]\n")
print("> Velocity at 0 [m]:\n\n"      + "x:       " + str(round(velocity2DAt0Km.x, 1))  + " [m/s]\ny:       " + str(round(velocity2DAt0Km.y, 1))  + " [m/s]\nTotal:   " + str(round(velocity2DAt0Km.length(), 1))   + " [m/s]\n")

# ------------------------------------------------------
# Display plot of results
# ------------------------------------------------------

arrX = []
arrY = []

for dataPoint in arrDatapointsFromSimulation:
    arrX.append(dataPoint[3])
    arrY.append(dataPoint[2].length())

plotter.plot(arrX, arrY)
plotter.show()


# x: alt in kft, y: speed in kft/s
# time on x in sec, g force of y-accel on y axis
# range (hor distance from impact point ) on x-axis, altitude in kft on y-axis
# time in minutes on x-axis, altitude in kft on y-axis