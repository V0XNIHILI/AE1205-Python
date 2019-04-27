import isa

# ------------------------------------------------------------------------------------------------------
# THIS FILE ASKS FOR USER INPUT AND HANDLES THE OUTPUT
# ------------------------------------------------------------------------------------------------------

print("==============================")
print("| V0X's Great ISA Calculator |")
print("==============================")
print("\nLast edited on 27 April 2019")
print("\n------------------------------")

# Ask for the input units
# Check if the input number is possible

while True:

    print("\nIn which units do you want to enter your altitude?\n")
    print("1. In [m]\n2. In [ft]\n3. In [FL]")

    sInputNo = input("\nEnter your choice: ")

    if sInputNo == "1" or sInputNo == "2" or sInputNo == "3":
        break
    else:
        print("\nYou did not enter a valid choice. Please try again.")

# Get the input altitude and calculate the temperature
# If the input is invalid, let the loop run again

fAltitude = 0

while True:

    sAltitude = input("\nEnter altitude: ")

    # Check if input is actually a number
    try:
        float(sAltitude)
    except:
        print("\nYou did not enter a number. Please try again.")
        continue

    # Convert string to float
    fAltitude = float(sAltitude)

    # Run conversion to metric units if required
    if sInputNo == "2":
        fAltitude = fAltitude*0.3048

    if sInputNo == "3":
        fAltitude = fAltitude*30.48

    # Run checks on the input
    if fAltitude < 0:
        print("\nYou entered an altitude smaller than 0. Please try again.")
        continue

    if fAltitude >= 84.852*1000:
        print("\nYour altitude is too large: you are in outer space. Please try again.")
        continue

    # If this point in the code is reached, the input was 100% so we can break out of the loop
    break

# Calculate the resulting ISA values
# These values will be stored in an array

arrISAValues = isa.calculateISAValues(fAltitude)

# Print results from input and calculation
# Round them to some decimals

print("\nTemperature: ", round(arrISAValues[0], 2), " [K]")
print("Pressure:    ", round(arrISAValues[1], 2), "[Pa]")
print("Density:     ", round(arrISAValues[2], 3), "[kg/m^3]\n")