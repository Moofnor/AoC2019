# Advent of Code 2019
# Day 5 - Part 1
# Hessel Prins
import numpy as np

def processparam(code, index, intcode):
    char = str(code)[::-1]
    while len(char) < 5:
        char += '0'
    opcode = int(char[:2])
    if opcode <= 20:
        # 3 inputs
        inputs = []
        for i, c in enumerate(char[2:5]):
            if c == '1':
                inputs.append(index+(i+1))
            else:
                inputs.append(intcode[index + (i+1)])
        if opcode == 10:
            intcode[inputs[2]] = intcode[inputs[0]] + intcode[inputs[1]]
        elif opcode == 20:
            intcode[inputs[2]] = intcode[inputs[0]] * intcode[inputs[1]]
        else:
            print('error: unknown opcode <= 20: ', opcode)
        nextindex = index + 4
    elif opcode <= 40:
        # 1 input
        inputs = []
        for i, c in enumerate(char[2:3]):
            if c == '1':
                inputs.append(index+(i+1))
            else:
                inputs.append(intcode[index + (i+1)])
        if opcode == 30:
            intcode[inputs[0]] = input('code 30 input: ')
        elif opcode == 40:
            print('code 40: ', intcode[inputs[0]])
        else:
            print('error: unknown opcode <= 40: ', opcode)
        nextindex = index + 2
    else:
        print('code 99')
        nextindex = 99999
    return nextindex

day = 5

intcode = np.genfromtxt('./Day_'+ str(day) + '/input.txt', delimiter=',').astype(int)

nextindex = 0
while nextindex != 99999:
    nextindex = processparam(intcode[nextindex], nextindex, intcode)



