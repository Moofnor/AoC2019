# Advent of Code 2019
# Day 6 - Part 2
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
    paths = []
    for end in ends:
        parent = planets[end].parent[0]
        subpath = [parent]
        while parent != center[0]:
            parent = planets[parent].parent
            if len(parent) > 1:
                print('Multiple parents')
                break
            else:
                parent = parent[0]
            subpath.append(parent)
        paths.append(subpath)
    return paths

def shortestPath(paths):
    pathlengths = []
    path0 = 0
    for obj in paths[0]:
        path0 += 1
        if obj in paths[1]:
            pathlengths.append(path0 + paths[1].index(obj))
    return pathlengths

class planet:
    def __init__(self, name):
        self.name = name
        self.parent = []
        self.child = []

if __name__ == "__main__":
    orbits = readinput(filename)
    planets = createPlanets(orbits)
    center, ends = findBoundary(planets)
    paths = tracePaths(center, ['YOU' , 'SAN'], planets)
    shortest = shortestPath(paths)
    output = min(shortest) - 1 # Hacks!
    print(output)