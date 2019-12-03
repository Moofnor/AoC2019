# Advent of Code 2019
# Day 3 - Part 2
# Hessel Prins

import numpy as np
from matplotlib import pyplot as plt
from functions import getlines, checkforintersect, actionsteps

day = 3

wirepath = np.genfromtxt('./Day_'+ str(day) + '/input.txt', delimiter=',', dtype=str)

actions_1, actions_2 = wirepath[0:2]
vectors = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}

lines1 = getlines(actions_1)
lines2 = getlines(actions_2)

intersections = checkforintersect(lines1, lines2)

steps = [actionsteps(actions_1, x[1]) + actionsteps(actions_2, x[2]) + sum(np.abs(x[3])) for x in intersections]

output = min(steps)

print(output)