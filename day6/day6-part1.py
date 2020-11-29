
import os, sys

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        orbitFile = open(inputPath)
        
        orbits = orbitFile.read().split()

        orbitCount, orbitMap = 0, {}

        for orbit in orbits:
            orbiting,orbitee = orbit.split(')')

            if orbiting in orbitMap:
                orbitMap[orbiting].append(orbitee)
            else:
                orbitMap[orbiting] = [orbitee]

            for planet in orbitMap:
                if orbiting in orbitMap[planet]:
                    orbitMap[planet].append(orbitee)

        for _,orbitMapOrbits in orbitMap.items():
            orbitCount += len(orbitMapOrbits)

        print(f'Total orbit count is {orbitCount}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        orbitFile.close()
else:
    print(f'Unable to locate file {inputPath}')