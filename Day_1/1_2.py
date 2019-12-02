# Advent of Code 2019
# Day 1 - Part 2
# Hessel Prins

import numpy as np

def neededfeul(mass, feul):
    mass = np.floor((mass)/3)-2
    if mass > 0:
        feul += mass + neededfeul(mass, feul)
    return feul

day = 1

testinput = np.loadtxt('./Day_'+ str(day) + '/input.txt')

output = np.int(np.sum([neededfeul(mass, 0) for mass in testinput]))

print(output)


