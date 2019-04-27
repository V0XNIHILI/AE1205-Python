import math

# ------------------------------------------------------------------------------------------------------
# ALL FUNCTIONS REQUIRED TO CALCULATE ISA VALUES
# ------------------------------------------------------------------------------------------------------

# Function which returns the asked ISA values
def calculateISAValues (fAlt):

    # function to calculate the ISA temperature based on some parameters
    def calcISATemp (fT0, fLapseRate, fH0, fH1):
        return fT0 + fLapseRate*(fH1 - fH0)

    # Function to calculate the ISA pressure based on some parameters
    def calcISAPressureWithLapse (fP0, fT1, fT0, fLapseRate):
        return fP0 * math.pow((fT1/fT0), -9.80665/fLapseRate/287.00)

    # Function to calculate the ISA pressure based on some parameters
    def calcISAPressureWithoutLapse (fP0, fT, fH0, fH1):
        return fP0 * math.exp(-9.80665/287.00/fT*(fH1- fH0))

    # Function to calculate ISA density based on some parameters
    def calcISADensityWithLapse (fRho0, fT1, fT0, fLapseRate):
        return fRho0 * math.pow((fT1/fT0), -9.80665/fLapseRate/287.00-1)

    # Function to calculate ISA density based on some parameters
    def calcISADensityWithoutLapse (fRho0, fT, fH0, fH1):
        return fRho0 * math.exp(-9.80665/287.00/fT*(fH1- fH0))

    # Taken from 'Hand-out-ISA' on Brightspace from Introduction to Aerospace
    fAllLayerProperties =   [   [288.15,    101325.0,   1.22500,        -0.0065,    0.0],
                                [216.65,    22632.0,    0.363918,        0.0,       11.0*1000],
                                [216.65,    5474.9,     0.0880349,      0.001,      20.0*1000],
                                [228.65,    868.02,     0.0132250,      0.0028,     32.0*1000],
                                [270.65,    110.91,     0.00142753,     0.0,        47.0*1000],
                                [270.65,    66.939,     0.000861606,    -0.0028,    51.0*1000],
                                [214.65,    3.9564,     0.0000642110,   -0.002,     71.0*1000],
                                [186.95,    0.3734,     0.00000695788,  0.0,        84.852*1000],
                            ]

    # Get the initial values from the array
    fTemperature = fAllLayerProperties[0][0]
    fPressure = fAllLayerProperties[0][1]
    fDensity = fAllLayerProperties[0][2]

    # Loop through all layers and break out of the loop if the layer is reached in which the altitude is
    for fCurrentLayerProperties in fAllLayerProperties:

        # Get the values for the current layer from the array
        fT0     = fCurrentLayerProperties[0]
        fP0     = fCurrentLayerProperties[1]
        fRho0   = fCurrentLayerProperties[2]
        fA      = fCurrentLayerProperties[3]
        fH0     = fCurrentLayerProperties[4]

        # If the loop has arrived in the layer in which the altitude is
        if fAlt > fH0:
            # If the layer is isothermal
            if fA == 0:
                fTemperature = fT0
                fPressure = calcISAPressureWithoutLapse(fP0, fT0, fH0, fAlt)
                fDensity = calcISADensityWithoutLapse(fRho0, fT0, fH0, fAlt)

            # If the layer is not isothermal
            else:
                fTemperature = calcISATemp(fT0, fA, fH0, fAlt)
                fPressure = calcISAPressureWithLapse(fP0, fTemperature, fT0, fA)
                fDensity = calcISADensityWithLapse(fRho0, fTemperature, fT0, fA)

            continue

        # If the altitude is below the current layer, the loop is done
        else:
            break

    # Return the calculated values
    return [fTemperature, fPressure, fDensity]