import sys, os, itertools

opcodeBlockSizes = { 1: 4, 2: 4, 3: 2, 4: 2, 99: 1 }

def getOpcode(intcodeBlock):
    return int(str(intcodeBlock)[-2:].lstrip('0'))

def getParameterModes(intcodeBlock):
    return list(str(intcodeBlock)[:-2][::-1])

def getParameterValues(intcode, startPosition):
    parameters = {}
    opcode = getOpcode(intcode[startPosition])
    parameterModes = getParameterModes(intcode[startPosition])

    for index in range(opcodeBlockSizes[opcode] - 1):
        
        if opcode == 3 or opcode == 4:
            parameterMode = 1
        elif parameterModes[index:]:
            parameterMode = parameterModes[index]
        else:
            parameterMode = 0

        if int(parameterMode) == 0:
            # Position mode
            parameters[index] = int(intcode[intcode[startPosition + index + 1]])

        elif int(parameterMode) == 1:
            # Value/Immediate mode
            parameters[index] = int(intcode[startPosition + index + 1])

    return parameters

def intcodeAddition(intcode, startPosition):
    parameters = getParameterValues(intcode, startPosition)
    resultPosition = intcode[startPosition + 3]

    intcode[resultPosition] = parameters[0] + parameters[1]
    
    return intcode

def intcodeMultiplication(intcode, startPosition):
    parameters = getParameterValues(intcode, startPosition)
    resultPosition = intcode[startPosition + 3]

    intcode[resultPosition] = parameters[0] * parameters[1]
    
    return intcode

def intcodeInsertValue(intcode, startPosition):
    parameters = getParameterValues(intcode, startPosition)
    # Get input from user
    inputValue = input("Please input a value: ")
    # Insert the value given into the location from the parameter
    intcode[parameters[0]] = inputValue
    return intcode

def intcodeOutputValue(intcode, startPosition):
    parameters = getParameterValues(intcode, startPosition)
    # Output the value at the location given by the parameter
    print(intcode[parameters[0]])


def processIntcode(intcode):

    blockPosition = 0

    while blockPosition < len(intcode):

        block = intcode[blockPosition]
        opcode = getOpcode(block)
        
        if opcode == 99:
            break

        elif opcode == 1:
            intcode = intcodeAddition(intcode, blockPosition)
        
        elif opcode == 2:
            intcode = intcodeMultiplication(intcode, blockPosition)
        
        elif opcode == 3:
            intcode = intcodeInsertValue(intcode, blockPosition)
        
        elif opcode == 4:
            intcodeOutputValue(intcode, blockPosition)

        blockPosition += opcodeBlockSizes[opcode]
    
    return intcode

if len(sys.argv) != 2:
    raise ValueError('Please supply the intcode to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        intcodeFile = open(inputPath)
        
        intcode = intcodeFile.read()

        originalIntcodeList = list(map(int, intcode.split(',')))

        processIntcode(originalIntcodeList)


    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        intcodeFile.close()
else:
    print(f'Unable to locate file {inputPath}')