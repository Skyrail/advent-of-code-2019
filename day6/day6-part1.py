
import os, sys

inputPath = sys.argv[1]

if os.path.isfile(inputPath):
    try:
        orbitFile = open(inputPath)
        
        orbits = orbitFile.read().split()

        for orbit in orbits:
            print(f'Orbit: {orbit}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        orbitFile.close()
else:
    print(f'Unable to locate file {inputPath}')