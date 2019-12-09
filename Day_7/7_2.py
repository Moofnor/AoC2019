# Advent of Code 2019
# Day 7 - Part 2
# Hessel Prins
import numpy as np
import copy
from itertools import permutations

def processparam(index, intcode, inputcode):
    output = 99999
    nextinput = False
    char = returnCode(intcode[index])
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
    elif opcode == 99:
        nextindex = 99999
        return nextindex, nextinput, output
    else:
        print('Error: unknown opcode')
    if int(returnCode(intcode[nextindex])[:2]) == 30:
        nextinput = True
    return nextindex, nextinput, output

def returnCode(opcode):
    char = str(opcode)[::-1]
    while len(char) < 5:
        char += '0'
    return char

class amplifier:
    def __init__(self, name, intcode, phase):
        self.name = name
        self.intcode = intcode
        self.phase = phase
        self.index = 0
        self.waiting = False
        self.finished = False
        self.input = []
        self.output = []
        while not self.waiting and not self.finished:
            self.index, self.waiting, paramOutput = processparam(self.index, self.intcode, self.phase)
            if paramOutput != 99999:
                self.output = paramOutput
            if self.index == 99999:
                self.finished = True
    def runStep(self):
        self.waiting = False
        while not self.waiting and self.index != 99999:
            self.index, self.waiting, paramOutput = processparam(self.index, self.intcode, self.input)
            if paramOutput != 99999:
                self.output = paramOutput
            if self.index == 99999:
                self.finished = True

day = 7

origintcode = np.genfromtxt('./Day_'+ str(day) + '/input.txt', delimiter=',').astype(int)

finalOutput = []

for inputOption in permutations(range(5, 10), 5):
    steps = 0
    amps = {}
    for amp in range(0,5):
        amps[amp] = amplifier(str(amp), copy.deepcopy(origintcode), inputOption[amp])
    amps[0].input = 0
    i = 0
    while not amps[4].finished:
        amp = i % 5
        amps[amp].runStep()
        amps[(i + 1) % 5].input = amps[amp].output
        i += 1
    finalOutput.append(amps[4].output)

print(max(finalOutput))


    


