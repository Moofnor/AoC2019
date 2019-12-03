# Advent of Code 2019
# Day 3 - Functions
# Hessel Prins

import numpy as np

def getlines(path):
    lines = []
    start = np.array([0, 0])
    for action in path:
        points = getlinepoints(start, action)
        lines.append(points)
        start = points[1]
    return lines

def getlinepoints(start, action):
    vectors = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}
    op = action[0]
    dist = int(action[1:])
    if op in 'UD':
        vert = 1
    else:
        vert = 0
    stop = start + np.multiply(vectors[op], dist)
    return [start, stop, vert]

def checkforintersect(lines1, lines2):
    intersections = []
    for i, line1 in enumerate(lines1):
        for j, line2 in enumerate(lines2):
            if line1[2] != line2[2]:
                intersect, point, s = lineintersect(line1, line2)
                if intersect:
                    intersections.append([point, i, j, s])
    return intersections

def lineintersect(line1, line2):
    intersect = False
    point = [0, 0]
    s = [0, 0]
    if line1[0][1] == line1[1][1]:
        if min(line1[0][0], line1[1][0]) <= line2[0][0] and max(line1[0][0], line1[1][0]) >= line2[0][0]:
            if min(line2[0][1], line2[1][1]) <= line1[0][1] and max(line2[0][1], line2[1][1]) >= line1[0][1]:
                intersect = True
                point = [line2[0][0], line1[0][1]]
                s = [point[0] - line1[0][0], point[1] - line2[0][1]]
    else:
        if min(line2[0][0], line2[1][0]) <= line1[0][0] and max(line2[0][0], line2[1][0]) >= line1[0][0]:
            if min(line1[0][1], line1[1][1]) <= line2[0][1] and max(line1[0][1], line1[1][1]) >= line2[0][1]:
                intersect = True
                point = [line1[0][0], line2[0][1]]
                s = [point[1] - line1[0][1], point[0] - line2[0][0]]
    return intersect, point, s

def manhattandist(point):
    return np.abs(point[0]) + np.abs(point[1])

def actionsteps(path, index):
    steps = 0
    for action in path[0:index]:
        steps += int(action[1:])
    return steps