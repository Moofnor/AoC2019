# Advent of Code 2019
# Day 2 - Part 2
# Hessel Prins

import numpy as np
import copy

day = 2

loadcode = np.genfromtxt('./Day_'+ str(day) + '/input.txt', delimiter=',').astype(int)

goal = 19690720

for noun in range(0, 99):
    for verb in range(0, 99):
        intcode = copy.deepcopy(loadcode)
        intcode[1:3] = [noun, verb]
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
        if intcode[0] == goal:
            print(100* noun + verb)
            break
