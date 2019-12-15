# Advent of Code 2019
# Day 13 part 2
# Hessel Prins
import numpy as np
from matplotlib import pyplot as plt
import keyboard

def processparam(index, intcode, base):
    output = 99999
    char = str(intcode[index])[::-1]
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
            intcode[inputs[0]] = inputKey()
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
    return nextindex, base, output

def processOutput(output):
    global image
    global score
    x, y, tile = output
    if x < 0:
        score = tile
        print(score)
    else:
        checkSize(x, y)
        image[x][y] = tile
        if tile > 2:
            plt.imshow(image.T)
            plt.draw()
            plt.pause(0.01)

def countBlock(image):
    count = 0
    for row in image.astype(int):
        counts = np.bincount(row)
        if len(counts) > 2:
            count += np.bincount(row)[2]
    return count

def checkSize(x, y):
    global image
    difx = max(0, (x + 1) - image.shape[0])
    dify = max(0, (y + 1) - image.shape[1])
    
    newx = np.zeros((difx, image.shape[1]))
    image = np.concatenate((image, newx), axis=0)
    newy = np.zeros((image.shape[0], dify))
    image = np.concatenate((image, newy), axis=1)

def inputKey():
    global image
    stickx, ballx = [0, 0]
    for i, row in enumerate(image.astype(int)):
        counts = np.bincount(row)
        if len(counts) > 2:
            ball = np.where(row == 4)
            stick = np.where(row == 3)
            if len(ball[0]) > 0:
                ballx = i
            if len(stick[0]) > 0:
                stickx = i
    if stickx > ballx:
        key = -1
    elif stickx < ballx:
        key = 1
    else:
        key = 0
    return key

day = 13

intcode = np.genfromtxt('./Day_'+ str(day) + '/input.txt', delimiter=',').astype(np.int64)

intcode = np.concatenate((intcode, np.zeros(10000, dtype=np.int64))) #cheatmode
intcode[0] = 2

plt.ion()

base = 0
nextindex = 0
suboutput = []
image = np.zeros((1,1), dtype=int)
joys = 0
score = 0
while nextindex != 99999:
    nextindex, base, output = processparam(nextindex, intcode, base)
    if output != 99999:
        suboutput.append(output)
    if len(suboutput) == 3:
        processOutput(suboutput)
        suboutput = []


