import sys, os

from itertools import permutations

opcodeBlockSizes = { 1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 99: 1 }

def getOpcode(intcodeBlock):
    return int(str(intcodeBlock)[-2:].lstrip('0'))

def getModes(intcodeBlock):
    return list(str(intcodeBlock)[:-2][::-1])

def getParameters(intcode, position):

    parameters = {}

    opcode = getOpcode(intcode[position])
    modes = getModes(intcode[position])

    for index in range(opcodeBlockSizes[opcode] - 1):
        
        mode = modes[index] if modes[index:] else 0

        if int(mode) == 1:
            # Value/Immediate mode - the value given is to be used
            parameters[index] = position + index + 1

        elif int(mode) == 0:
            # Position mode - the value given indicates where the value is stored
            parameters[index] = intcode[position + index + 1]

    return parameters

def processIntcode(intcode, inputValues = []):

    position, returnValues = 0, []

    while position < len(intcode):

        opcode = getOpcode(intcode[position])
        parameters = getParameters(intcode, position)
        
        if opcode == 99:
            # Quit program
            break

        elif opcode == 1:
            # Addition
            intcode[parameters[2]] = int(intcode[parameters[0]]) + int(intcode[parameters[1]])
        
        elif opcode == 2:
            # Multiplication
            intcode[parameters[2]] = int(intcode[parameters[0]]) * int(intcode[parameters[1]])
        
        elif opcode == 3:
            # Insert value
            intcode[parameters[0]] = inputValues.pop(0) if inputValues else 0
        
        elif opcode == 4:
            # Output value
            returnValues.append(intcode[parameters[0]])

        elif opcode == 5:
            # Jump if not zero
            if intcode[parameters[0]] != 0:
                position = intcode[parameters[1]]
                continue
        
        elif opcode == 6:
            # Jump if zero
            if intcode[parameters[0]] == 0:
                position = intcode[parameters[1]]
                continue
        
        elif opcode == 7:
            # Less than comparison
            if int(intcode[parameters[0]]) < int(intcode[parameters[1]]):
                intcode[parameters[2]] = 1
            else:
                intcode[parameters[2]] = 0

        elif opcode == 8:
            # Equality comparison
            if int(intcode[parameters[0]]) == int(intcode[parameters[1]]):
                intcode[parameters[2]] = 1
            else:
                intcode[parameters[2]] = 0

        position += opcodeBlockSizes[opcode]
    
    return returnValues 

def runAmplifierIntcode(intcode):
    sequences = tuple(permutations([0,1,2,3,4], 5))

    inputSignal, results = 0, []

    for sequence in sequences:

        inputSignal = 0

        for phaseSetting in sequence:

            intcode = originalIntcodeList.copy()

            inputSignal = processIntcode(intcode, [phaseSetting, inputSignal])[0]

            results.append(inputSignal)

    print(f'Max result is {max(results)}')

if len(sys.argv) != 2:
    raise ValueError('Please supply the intcode to be processed')

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        intcodeFile = open(inputPath)
        
        originalIntcodeList = list(map(int, intcodeFile.read().strip().split(',')))

        runAmplifierIntcode(originalIntcodeList)

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        intcodeFile.close()
else:
    print(f'Unable to locate file {inputPath}')