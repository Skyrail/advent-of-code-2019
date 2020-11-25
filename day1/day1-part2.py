import sys, os, math

# Using the given mass calculates the required fuel, taking into account the mass of the fuel
def calculateFuelFromMass(mass):
    requiredFuel = math.floor(mass / 3) - 2
    if requiredFuel <= 0:
        return 0
    else: 
        return requiredFuel + calculateFuelFromMass(requiredFuel)

# Calculates the required fuel from a list of module masses
def calculateFuelFromFile(inputFile):
    fuelTotal = 0
    for inputLine in inputFile:
        fuelTotal += calculateFuelFromMass(int(inputLine))
    
    return fuelTotal

if len(sys.argv) != 2:
    raise ValueError('Please supply an input of module masses')

inputValue = sys.argv[1]

if os.path.isfile(inputValue):
    try:
        inputFile = open(inputValue)
        fuelAmount = calculateFuelFromFile(inputFile)
    except IOError:
        print(f'Unable to open file {inputValue}')
    finally:
        inputFile.close()
else:
    massAmount = int(inputValue)
    fuelAmount = calculateFuelFromMass(massAmount)


print(f'The total fuel required is {fuelAmount}')