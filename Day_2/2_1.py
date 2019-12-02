# Advent of Code 2019
# Day 2 - Part 1
# Hessel Prins

import numpy as np

day = 2

intcode = np.genfromtxt('./Day_'+ str(day) + '/input.txt', delimiter=',').astype(int)

intcode[1:3] = [12, 2]

i = 0
while intcode[i] != 99:
    x = intcode[i]
    if x == 1:
        intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
        i += 4
    elif x == 2:
        intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
        i += 4
    else:
        print('error: Unknown opcode')

print(intcode[0])