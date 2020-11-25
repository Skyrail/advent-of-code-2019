import sys, os

def processIntCode(intcode):
    intcodeList = intcode.split(',')

    for key in range(0, len(intcodeList), 4):
        intcodeValue = int(intcodeList[key])

        if intcodeValue == 99:
            break

        firstValueKey = int(intcodeList[key + 1])
        firstValue = intcodeList[firstValueKey]
        secondValueKey = int(intcodeList[key + 2])
        secondValue = intcodeList[secondValueKey]
        resultKey = int(intcodeList[key + 3])

        if intcodeValue == 1:
            intcodeList[resultKey] = firstValue + secondValue
            print(f'It\'s an addition')
        elif intcodeValue == 2:
            intcodeList[resultKey] = firstValue * secondValue
            print(f'It\'s a multiplication')
        else:
            print(f'Intcode not recognised')

    print(intcodeList)

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