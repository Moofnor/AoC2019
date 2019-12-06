# Advent of Code 2019
# Day 6 - Part 1
# Hessel Prins
import numpy as np

day = 6
filename = './Day_'+ str(day) + '/input.txt'

def readinput(filename):
    with open(filename, 'r') as f:
        orbits = [line.rstrip().split(')') for line in f]
    return orbits

def createPlanets(orbits):
    planets = {}
    for orbit in orbits:
        p1, p2 = orbit[:]
        if p1 not in planets.keys():
            planets[p1] = planet(p1)
        planets[p1].child.append(p2)
        if p2 not in planets.keys():
            planets[p2] = planet(p2)
        planets[p2].parent.append(p1)
    return planets

def findBoundary(planets):
    center = []
    ends = []
    for obj in planets:
        if planets[obj].parent == []:
            center.append(planets[obj].name)
        if planets[obj].child == []:
            ends.append(planets[obj].name)
    print('Found %i center and %i ends' %(len(center), len(ends)))
    planets.pop(center[0])
    return center, ends

def tracePaths(center, ends, planets):
    totalOrbits = []
    for obj in planets:
        subOrbits = 1
        parent = planets[obj].parent[0]
        while parent != center[0]:
            parent = planets[parent].parent
            if len(parent) > 1:
                print('Multiple parents')
                break
            else:
                parent = parent[0]
            subOrbits += 1
        totalOrbits.append(subOrbits)
    return totalOrbits

class planet:
    def __init__(self, name):
        self.name = name
        self.parent = []
        self.child = []

if __name__ == "__main__":
    orbits = readinput(filename)
    planets = createPlanets(orbits)
    center, ends = findBoundary(planets)
    totalOrbits = tracePaths(center, ends, planets)
    output = sum(totalOrbits)
    print(output)

