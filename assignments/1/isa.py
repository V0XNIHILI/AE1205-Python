import math

# ------------------------------------------------------------------------------------------------------
# ALL FUNCTIONS REQUIRED TO CALCULATE ISA VALUES
# ------------------------------------------------------------------------------------------------------

# Function which returns the asked ISA values
def calculateISAValues (fAlt, fBaseTemp = 288.15):

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

    fLayerProperties = [
                            [11*1000,  -0.0065],
                            [20*1000,   0.0],
                            [32*1000,   0.001],
                            [47*1000,   0.0],
                            [51*1000,  -0.0028],
                            [71*1000,  -0.002],
                        ]

    fT0     = fBaseTemp
    fP0     = 101325
    fRho0   = fP0/287.00/fT0
    fH0     = 0

    fTemperature    = 0
    fPressure       = 0
    fDensity        = 0

    # Loop through all layers and break out of the loop if the layer is reached in which the altitude is
    for currentLayerProperties in fLayerProperties:

        fMinAlt = min(fAlt, currentLayerProperties[0])

        # If the layer is isothermal
        if currentLayerProperties[1] == 0:
            fTemperature = fT0
            fPressure = calcISAPressureWithoutLapse(fP0, fT0, fH0, fMinAlt)
            fDensity = calcISADensityWithoutLapse(fRho0, fT0, fH0, fMinAlt)

        # If the layer is not isothermal
        else:
            fTemperature = calcISATemp(fT0, currentLayerProperties[1], fH0, fMinAlt)
            fPressure = calcISAPressureWithLapse(fP0, fTemperature, fT0, currentLayerProperties[1])
            fDensity = calcISADensityWithLapse(fRho0, fTemperature, fT0, currentLayerProperties[1])
        
        # Set all the properties for the next loop though
        fT0 = fTemperature
        fP0 = fPressure
        fRho0 = fDensity
        fH0 = currentLayerProperties[0]

        if fMinAlt < currentLayerProperties[0]:
            break

    # Return the calculated values
    return [fTemperature, fPressure, fDensity]