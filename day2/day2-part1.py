import sys, os

def getValuePositions(intcodes, startPosition):
    """ 
    Gets the positions of the required values as per the spec
    Intcodes come in blocks of 4
    1. Opcode
    2. Position of first value for operation
    3. Position of second value for operation
    4. Result position
    """
    return intcodes[startPosition + 1], intcodes[startPosition + 2], intcodes[startPosition + 3]

def intcodeAddition(intcodes, startPosition):
    """ Using the startPosition, adds the two calculated values and inserts the result as per the spec """
    firstValuePosition, secondValuePosition, resultValuePosition = getValuePositions(intcodes, startPosition)

    intcodes[resultValuePosition] = intcodes[firstValuePosition] + intcodes[secondValuePosition]
    
    return intcodes

def intcodeMultiplication(intcodes, startPosition):
    """ Using the startPosition, multiplies the two calculated values and inserts the result as per the spec """
    firstValuePosition, secondValuePosition, resultValuePosition = getValuePositions(intcodes, startPosition)

    intcodes[resultValuePosition] = intcodes[firstValuePosition] * intcodes[secondValuePosition]
    
    return intcodes

def processIntCode(intcode):
    intcodes = list(map(int, intcode.split(',')))

    for position in range(0, len(intcodes), 4):
        opcode = intcodes[position]

        if opcode == 99:
            break
        elif opcode == 1:
            intcodes = intcodeAddition(intcodes, position)
            continue
        elif opcode == 2:
            intcodes = intcodeMultiplication(intcodes, position)
            continue
        else:
            print('Opcode not recognised')
            break

    print(intcodes)

if len(sys.argv) != 2:
    raise ValueError('Please supply an input of Intcode')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        intcodeFile = open(inputPath)
        processIntCode(intcodeFile.read())
    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        intcodeFile.close()
else:
    print(f'Unable to locate file {inputPath}')