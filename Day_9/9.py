# Advent of Code 2019
# Day 5 - Part 2
# Hessel Prins
import numpy as np

def processparam(code, index, intcode, base):
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
            elif c == '2':
                inputs.append(base + intcode[index + (i+1)])
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
            elif c == '2':
                inputs.append(base + intcode[index + (i+1)])
            else:
                inputs.append(intcode[index + (i+1)])
        if opcode == 30:
            intcode[inputs[0]] = input('code 30 input: ')
        elif opcode == 40:
            print('code 40: ', intcode[inputs[0]])
        else:
            print('error: unknown opcode <= 40: ', opcode)
        nextindex = index + 2
    elif opcode <= 60:
        # 2 inputs
        inputs = []
        for i, c in enumerate(char[2:4]):
            if c == '1':
                inputs.append(index+(i+1))
            elif c == '2':
                inputs.append(base + intcode[index + (i+1)])
            else:
                inputs.append(intcode[index + (i+1)])
        if opcode == 50:
            if intcode[inputs[0]] > 0:
                nextindex = intcode[inputs[1]]
            else:
                nextindex = index + 3
        elif opcode == 60:
            if intcode[inputs[0]] == 0:
                nextindex = intcode[inputs[1]]
            else:
                nextindex = index + 3
        else:
            print('error: unknown opcode <= 60: ', opcode)
    elif opcode <= 80:
        # 3 inputs
        inputs = []
        for i, c in enumerate(char[2:5]):
            if c == '1':
                inputs.append(index+(i+1))
            elif c == '2':
                inputs.append(base + intcode[index + (i+1)])
            else:
                inputs.append(intcode[index + (i+1)])
        if opcode == 70:
            if intcode[inputs[0]] < intcode[inputs[1]]:
                intcode[inputs[2]] = 1
            else:
                intcode[inputs[2]] = 0
            
        elif opcode == 80:
            if intcode[inputs[0]] == intcode[inputs[1]]:
                intcode[inputs[2]] = 1
            else:
                intcode[inputs[2]] = 0
        else:
            print('error: unknown opcode <= 80: ', opcode)
        nextindex = index + 4
    elif opcode < 99:
        # 1 input
        inputs = []
        for i, c in enumerate(char[2:3]):
            if c == '1':
                inputs.append(index+(i+1))
            elif c == '2':
                inputs.append(base + intcode[index + (i+1)])
            else:
                inputs.append(intcode[index + (i+1)])
        if opcode == 90:
            base += intcode[inputs[0]]
        nextindex = index + 2
    else:
        print('code :', opcode)
        nextindex = 99999
    return nextindex, base

day = 9

intcode = np.genfromtxt('./Day_'+ str(day) + '/input.txt', delimiter=',').astype(np.int64)

intcode = np.concatenate((intcode, np.zeros(10000, dtype=np.int64))) #cheatmode

nextindex = 0
base = 0
while nextindex != 99999:
    nextindex, base = processparam(intcode[nextindex], nextindex, intcode, base)



