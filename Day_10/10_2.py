# Advent of Code 2019
# Day 10 part 2
# Hessel Prins
import numpy as np

def readInput(filename):
    with open(filename, 'r') as f:
        rows = [line.rstrip() for line in f]
    return rows

def calculateAngle(asteroids, source):
    n = len(asteroids)
    angles = np.zeros(n)
    offset = -90
    for i in range(n):
        angles[i] = ((np.arctan2(-asteroids[i][1] + source[1], -asteroids[i][0] + source[0]) * 180 / np.pi) + offset) % 360 # map to 0 - 360
    return angles

def calculateDist(asteroids, source):
    n = len(asteroids)
    dist = np.zeros(n)
    for i in range(n):
        dist[i] = np.sqrt((asteroids[i][1] - source[1])**2 + (asteroids[i][0] - source[0])**2)
    return dist

def listAsteroids(data):
    asteroids = []
    for i, row in enumerate(data):
        for j, obj in enumerate(row):
            if obj == '#':
                asteroids.append([j, i])
    return asteroids

def sortedAngles(asteroids, angles, dist):
    unqangle = sorted(np.unique(angles))
    sortedAngle = {}
    for i, ang in enumerate(unqangle):
        ids = np.where(angles == ang)
        dists = dist[ids]
        sortedDist = np.argsort(dists)
        sortedindex = [int(i) for i in sortedDist]
        sortedids = [ids[0][i] for i in sortedindex]
        sortedAngle[ang] = [asteroids[i] for i in sortedids]
    return sortedAngle, unqangle

day = 10
filename = './Day_'+ str(day) + '/input.txt'
data = readInput(filename)

asteroids = listAsteroids(data)
source = asteroids.pop(263)
angles = calculateAngle(asteroids, source)
dist = calculateDist(asteroids, source)
sortedAngle, unqangle = sortedAngles(asteroids, angles, dist)
target = sortedAngle[unqangle[199]][0]
output = 100*target[0] + target[1]
print(output)



