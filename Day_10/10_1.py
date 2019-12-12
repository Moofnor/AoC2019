# Advent of Code 2019
# Day 10 part 1
# Hessel Prins
import numpy as np

def readInput(filename):
    with open(filename, 'r') as f:
        rows = [line.rstrip() for line in f]
    return rows

def calculateAngle(asteroids):
    n = len(asteroids)
    angles = np.zeros((n, n))
    for i in range(n - 1):
        for j in range(i + 1, n):
            angles[i][j] = np.arctan2(asteroids[j][1] - asteroids[i][1], asteroids[j][0] - asteroids[i][0]) * 180 / np.pi
    angles -= angles.T
    return angles

def listAsteroids(data):
    asteroids = []
    for i, row in enumerate(data):
        for j, obj in enumerate(row):
            if obj == '#':
                asteroids.append([j, i])
    return asteroids


def findVisible(angles):
    n = angles.shape[0]
    vis = np.zeros(n)
    for i, ast in enumerate(angles):
        vis[i] = len(np.unique(ast)) + 1
    return vis


day = 10
filename = './Day_'+ str(day) + '/input.txt'
data = readInput(filename)

asteroids = listAsteroids(data)
angles = calculateAngle(asteroids)
visible = findVisible(angles)

output = max(visible)
index = np.where(visible == max(visible))[0][0]
print(output, asteroids[index])

