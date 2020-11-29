
import os, sys

def count_orbits(orbitMap, body):
    count = 0
    if body in orbitMap:
        count += count_orbits(orbitMap, orbitMap[body]) + 1
    
    return count

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        orbitFile = open(inputPath)
        
        orbitCount, orbitMap = 0, {}

        for orbit in orbitFile.read().split():
            body,planet = orbit.split(')')
            orbitMap[planet] = body

        for planet,body in orbitMap.items():
            orbitCount += count_orbits(orbitMap, body)
            orbitCount += 1

        print(f'Total orbit count is {orbitCount}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        orbitFile.close()
else:
    print(f'Unable to locate file {inputPath}')