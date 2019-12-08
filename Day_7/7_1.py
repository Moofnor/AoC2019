# Advent of Code 2019
# Day 5 - Part 1
# Hessel Prins
import numpy as np
import copy
from itertools import permutations

def processparam(code, index, intcode, inputcode):
    output = 99999
    nextinput = False
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
            intcode[inputs[0]] = inputcode
            nextinput = True
        elif opcode == 40:
            output = intcode[inputs[0]]
        else:
            print('error: unknown opcode <= 40: ', opcode)
        nextindex = index + 2
    elif opcode <= 60:
        # 2 inputs
        inputs = []
        for i, c in enumerate(char[2:4]):
            if c == '1':
                inputs.append(index+(i+1))
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
    else:
        nextindex = 99999
    return nextindex, nextinput, output

def runAmp(origintcode, paramInputs):
    paramOutputs = []
    for x, inp in enumerate(paramInputs[1]):
            intcode = copy.deepcopy(origintcode)
            inputcode = paramInputs[0]
            nextindex = 0
            while nextindex != 99999:
                nextindex, nextinput, paramOutput = processparam(intcode[nextindex], nextindex, intcode, inputcode)
                if nextinput:
                    inputcode = inp
                if paramOutput != 99999:
                    subOutput = paramOutput
            paramOutputs.append(subOutput)
    return paramOutputs

day = 7

origintcode = np.genfromtxt('./Day_'+ str(day) + '/input.txt', delimiter=',').astype(int)

finalOutput = []

for inputOption in permutations(range(5), 5):
    paramOutputs = [0]
    for amp in range(0,5):
        paramInputs = [inputOption[amp], paramOutputs]
        paramOutputs = runAmp(origintcode, paramInputs)
    finalOutput.append(max(paramOutputs))

print(finalOutput)
print(max(finalOutput))



