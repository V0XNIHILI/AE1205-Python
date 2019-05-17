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

dataPointAt32Km = travelledPath.getdatapointataltitude(32*1000)
dataPointAt11Km = travelledPath.getdatapointataltitude(11*1000)
dataPointAt0Km = travelledPath.getdatapointataltitude(0)

print("> At 32,000 [m]:\n\n" + "V_x:   " + str(round(dataPointAt32Km[2].x, 1)) + " [m/s]\nV_y:   " + str(round(dataPointAt32Km[2].y, 1)) + " [m/s]\nV_t:   " + str(round(dataPointAt32Km[2].length(), 1))  + " [m/s]\ny_p:   " + str(round(dataPointAt32Km[5], 2)) + " [deg]\n")
print("> At 11,000 [m]:\n\n" + "V_x:   " + str(round(dataPointAt11Km[2].x, 1)) + " [m/s]\nV_y:   " + str(round(dataPointAt11Km[2].y, 1)) + " [m/s]\nV_t:   " + str(round(dataPointAt11Km[2].length(), 1))  + " [m/s]\ny_p:   " + str(round(dataPointAt11Km[5], 2)) + " [deg]\n")
print("> At 0 [m]:\n\n"      + "V_x:   " + str(round(dataPointAt0Km[2].x, 1))  + " [m/s]\nV_y:   " + str(round(dataPointAt0Km[2].y, 1))  + " [m/s]\nV_t:   " + str(round(dataPointAt0Km[2].length(), 1))   + " [m/s]\ny_p:   " + str(round(dataPointAt0Km[5], 2)) + " [deg]\n")

# ------------------------------------------------------
# Display plot of results
# ------------------------------------------------------

# Get arrays with values for plots
arrAltitudeInKFt = travelledPath.getaltitudesinkft()
arrSpeedInKFt = travelledPath.getspeedsinkft()
arrGForces = travelledPath.getgforces()
arrTimeInSec = travelledPath.gettimesinsec()
arrTimeInMinutes = travelledPath.gettimesinminutes()
arrHorizontalDistanceTravelled = travelledPath.gethorizontaldistancesfromimpactpointinkm()

# x: alt in kft, y: speed in kft/s
plotter.subplot(2, 2, 1)
plotter.ylim(0, 25)
plotter.xlim(fInitialAltitude/1000/0.3048, 0)
plotter.plot(arrAltitudeInKFt, arrSpeedInKFt)
plotter.grid()
plotter.margins(x=0)
plotter.title("Speed versus altitude of re-entry")
plotter.xlabel("Altitude [kft]")
plotter.ylabel("Speed [kft/s]")

# x: time in sec, y: g forces
plotter.subplot(2, 2, 2)
plotter.plot(arrTimeInSec, arrGForces)
plotter.grid()
plotter.margins(x=0)
plotter.title("G-force versus time during re-entry")
plotter.xlabel("Time [s]")
plotter.ylabel("G-force [-]")

# x: horizontal distance from impact point in kft, y: alt in kft
plotter.subplot(2, 2, 3)
plotter.ylim(0, 400)
plotter.gca().invert_xaxis()
plotter.plot(arrHorizontalDistanceTravelled, arrAltitudeInKFt)
plotter.grid()
plotter.margins(x=0)
plotter.title("Altitude versus range of re-entry")
plotter.xlabel("Range [km]")
plotter.ylabel("Altitude [kft]")

# x: time in minutes, y: altitude in kft
plotter.subplot(2, 2, 4)
plotter.ylim(0, 400)
plotter.plot(arrTimeInMinutes, arrAltitudeInKFt)
plotter.grid()
plotter.margins(x=0)
plotter.title("Altitude versus time during re-entry")
plotter.xlabel("Time [min]")
plotter.ylabel("Altitude [kft]")

# Actually plot the graphs with some margins between the plots (tight_layout())
plotter.tight_layout()
plotter.show()