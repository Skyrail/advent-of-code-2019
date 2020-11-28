import sys, os, itertools

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

        if int(mode) == 1 or opcode in [3,4]:
            # Value/Immediate mode - the value given is to be used
            parameters[index] = position + index + 1

        elif int(mode) == 0:
            # Position mode - the value given indicates where the value is stored
            parameters[index] = intcode[position + index + 1]

    return parameters

def intcodeAddition(intcode, parameters):

    intcode[parameters[2]] = int(intcode[parameters[0]]) + int(intcode[parameters[1]])
    
    return intcode

def intcodeMultiplication(intcode, parameters):

    intcode[parameters[2]] = int(intcode[parameters[0]]) * int(intcode[parameters[1]])
    
    return intcode

def intcodeInsertValue(intcode, position):

    intcode[intcode[position]] = int(input("Please input a value: "))
    
    return intcode

def intcodeOutputValue(intcode, position):
    
    print(intcode[intcode[position]])

def processIntcode(intcode):

    position = 0

    while position < len(intcode):

        opcode = getOpcode(intcode[position])
        parameters = getParameters(intcode, position)
        
        if opcode == 99:
            break

        elif opcode == 1:
            intcode = intcodeAddition(intcode, parameters)
        
        elif opcode == 2:
            intcode = intcodeMultiplication(intcode, parameters)
        
        elif opcode == 3:
            intcode = intcodeInsertValue(intcode, parameters[0])
        
        elif opcode == 4:
            intcodeOutputValue(intcode, parameters[0])

        elif opcode == 5:
            if intcode[parameters[0]] != 0:
                position = intcode[parameters[1]]
                continue
        
        elif opcode == 6:
            if intcode[parameters[0]] == 0:
                position = intcode[parameters[1]]
                continue
        
        elif opcode == 7:
            if int(intcode[parameters[0]]) < int(intcode[parameters[1]]):
                intcode[intcode[parameters[2]]] = 1
            else:
                intcode[intcode[parameters[2]]] = 0

        elif opcode == 8:
            if int(intcode[parameters[0]]) == int(intcode[parameters[1]]):
                intcode[intcode[parameters[2]]] = 1
            else:
                intcode[intcode[parameters[2]]] = 0

        position += opcodeBlockSizes[opcode]
    
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