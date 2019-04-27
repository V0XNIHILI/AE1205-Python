import isa

# ------------------------------------------------------------------------------------------------------
# ASKING FOR USER INPUT AND HANDLING OUTPUT
# ------------------------------------------------------------------------------------------------------

print("================================")
print("| Douwe's Great ISA Calculator |")
print("================================")
print("\nLast edited on 27 April 2019")
print("\n--------------------------------")

bValidChoice = None

# Ask for the input units
# Check if the input number is possible

while bValidChoice == None:
    print("\nIn which units do you want to enter your altitude?\n")
    print("1. In [m]\n2. In [ft]\n3. In [FL]")
    sInputNo = input("\nEnter your choice: ")

    if sInputNo == "1" or sInputNo == "2" or sInputNo == "3":
        bValidChoice = True
    else:
        print("\nYou did not enter a valid choice. Please try again.")

bValidInput = None

# Get the input altitude and calculate the temperature
# If the input is invalid, let the loop run again

fAltitudeString = ""
fAltitude = 0

while bValidInput == None:
    sAltitude = input("\nEnter altitude: ")

    fAltitude = float(sAltitude)

    if sInputNo == "2":
        fAltitude = fAltitude*0.3048

    if sInputNo == "3":
        fAltitude = fAltitude*30.48

    if fAltitude < 0:
        print("\nYou entered an altitude smaller than 0. Please try again.")
        continue

    if fAltitude >= 100*1000:
        print("\nYour altitude crossed the Kármán line: you are in outer space. Please try again.")
        continue

    bValidInput = True

# Calculate the resulting ISA values
isaValues = isa.calculateISAValues(fAltitude)

# Print results from input and calculation
print("\nTemperature: ", round(isaValues[0], 2), " [K]")
print("Pressure:    ", round(isaValues[1], 2), "[Pa]")
print("Density:     ", round(isaValues[2], 3), "[kg/m^3]\n")