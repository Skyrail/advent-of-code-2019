import os, sys
# Import data

def getIntersectingCoordinates(lineA, lineB):
    return list(set(lineA) & set(lineB))

def getIntersectionDistancesFromOrigin(intersectingCoordinates):
    """ Calculates the Manhattan distances for each intersecting coordinates from the origin """
    manhattanDistances = []

    for coordinate in intersectingCoordinates:
        manhattanDistances.append(calculateManhattanDistance((0,0), coordinate))

    return manhattanDistances

def calculateManhattanDistance(startPoint, endPoint):
    return abs(startPoint[0] - endPoint[0]) + abs(startPoint[1] - endPoint[1])

def getSmallestDistance(manhattanDistances):
    # Ignore the origin intersection as per the spec
    manhattanDistances.remove(0)
    return min(manhattanDistances)

def getNextCoordinate(startCoordinate, distance):
    """ Uses the given distance to calculate the next coordinate along from the given startCoordinate """
    return [x + y for x,y in zip(startCoordinate, distance)]

def getDistance(instruction):
    """ Extracts the distance value from the given instruction """
    return int(instruction.lstrip('UDLR'))

def getDirection(instruction):
    """ Extracts direction from instruction - typically U/D/L/R """
    return instruction[0] 

def generateLineCoordinates(startPoint, instruction):
    """ Generates a list of coordinates based on the startPoint and the given instruction """
    coordinates = []
    x,y = startPoint

    direction = getDirection(instruction)
    distance = getDistance(instruction)

    for _ in range(distance):
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
        
        coordinates.append((x,y))

    return coordinates        


# For each line calculate co-ordinate of each point
def calculatePathCoordinates(path):
    coordinates = [(0,0)]

    for instruction in path:
        previousCoordinate = coordinates[-1]

        coordinates.extend(generateLineCoordinates(previousCoordinate, instruction))        
    
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

        pointsOfIntersection = getIntersectingCoordinates(pathCoordinates[0], pathCoordinates[1])
        intersectionDistances = getIntersectionDistancesFromOrigin(pointsOfIntersection)
        smallestDistance = getSmallestDistance(intersectionDistances)

        print(f'Smallest distance is: {smallestDistance}')
    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        inputFile.close()
else:
    print(f'Unable to locate file {inputPath}')