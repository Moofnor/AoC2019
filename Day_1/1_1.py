# Advent of Code 2019
# Day 1 - Part 1
# Hessel Prins

import numpy as np

day = 1

testinput = np.loadtxt('./Day_'+ str(day) + '/input.txt')

output = np.int(np.sum(np.floor((testinput)/3)-2))

print(output)