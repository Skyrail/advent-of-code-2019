
import os, sys

def count_orbits(orbitMap, body):
    count = 0
    if body in orbitMap:
        count += count_orbits(orbitMap, orbitMap[body]) + 1
    
    return count

def get_parents(orbitMap, child):

    parents = set()

    if child in orbitMap:
        parents.add(orbitMap.get(child))
        parents = parents.union(get_parents(orbitMap, orbitMap.get(child)))

    return parents


def count_pathway(orbitMap, pointA, pointB):

    pointAParents, pointBParents = get_parents(orbitMap, pointA), get_parents(orbitMap, pointB)

    uniqueParents = pointAParents ^ pointBParents

    return len(uniqueParents)

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

        print(f'Pathway count bteween SAN and YOU is: {count_pathway(orbitMap, "SAN", "YOU")}')

    except IOError:
        print(f'Unable to open file {inputPath}')
    finally:
        orbitFile.close()
else:
    print(f'Unable to locate file {inputPath}')