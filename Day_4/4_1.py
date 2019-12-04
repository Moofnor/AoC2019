# Advent of Code 2019
# Day 4 - Part 1
# Hessel Prins
import numpy as np

day = 4

limits = np.genfromtxt('./Day_'+ str(day) + '/input.txt', delimiter='-', dtype=int)

def generateoptions(start, stop):
    viable = []
    for i in range(start,stop):
        double = 0
        char = str(i)
        for j in range(1,6):
            if char[j] >= char[j-1]:
                if char[j] == char[j-1]:
                    double += 1
            else:
                break
        else:
            if double > 0:
                viable.append(i)
    return viable

options = generateoptions(limits[0], limits[1])

print(len(options))
