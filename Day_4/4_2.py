# Advent of Code 2019
# Day 4 - Part 2
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

def checkoptions(options):
    check = []
    for i in options:
        if findoutlier(str(i)):
            check.append(i)
    return check
        
def findoutlier(char):
    double = False
    i = 0
    while i < 5:
        j = 1
        while char[i] == char[i+j]:
            j += 1
            if i+j > 5:
                break
        if j == 2:
            double = True
        i += j
    return double

options = generateoptions(limits[0], limits[1])
checkedoptions = checkoptions(options)

print(len(checkedoptions))