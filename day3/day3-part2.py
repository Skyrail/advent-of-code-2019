import os, sys
# Import data

def getIntersectingCoordinates(lineA, lineB):
    return list(lineA.keys() & lineB.keys())

def getDistance(instruction):
    """ Extracts the distance value from the given instruction """
    return int(instruction.lstrip('UDLR'))

def getDirection(instruction):
    """ Extracts direction from instruction - typically U/D/L/R """
    return instruction[0] 

# For each line calculate co-ordinate of each point
def calculatePathCoordinates(path):
    stepCount = x = y = 0
    coordinates = {(0,0): 0}

    for instruction in path:
        distance = getDistance(instruction)
        direction = getDirection(instruction)

        for _ in range(distance):
            stepCount += 1

            if direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            elif direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            else:
                print(f'Could not parse direction ({direction})')
            
            coordinates[(x,y)] = stepCount

    return coordinates

if len(sys.argv) != 2:
    raise ValueError('Please supply an input of wire paths')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        inputFile = open(inputPath)

        pathCoordinates = []

        with open(inputPath) as inputFile:
            for _,wirePath in enumerate(inputFile):
                wirePathInstructions = list(wirePath.rstrip().split(','))
                pathCoordinates.append(calculatePathCoordinates(wirePathInstructions))

        intersectingCoordinates = getIntersectingCoordinates(pathCoordinates[0], pathCoordinates[1])

        steps = {}

        for coordinate in intersectingCoordinates:
            steps[coordinate] = pathCoordinates[0][coordinate] + pathCoordinates[1][coordinate]

        del steps[(0,0)]

        minimumStepCoordinate = steps[min(steps,key=steps.get)]

        print(f'Minimum steps {minimumStepCoordinate}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        inputFile.close()
else:
    print(f'Unable to locate file {inputPath}')