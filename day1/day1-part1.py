import sys, os, math

def calculateFuelFromMass(mass):
    return math.floor(mass / 3) - 2

def calculateFuelFromFile(inputFile):
    fuelTotal = 0
    for inputLine in inputFile:
        fuelTotal += calculateFuelFromMass(int(inputLine))
    
    return fuelTotal

# Load input from the command line argument - either value or file
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