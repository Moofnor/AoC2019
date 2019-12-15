# Advent of Code 2019
# Day 13 part 1
# Hessel Prins
import numpy as np
from matplotlib import pyplot as plt

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
            intcode[inputs[0]] = colour
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
    x, y, tile = output
    checkSize(x, y)
    image[x][y] = tile
    if tile > 2:
        plt.imshow(image.T)
        plt.draw()
        plt.pause(1)

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

day = 13

intcode = np.genfromtxt('./Day_'+ str(day) + '/input.txt', delimiter=',').astype(np.int64)

intcode = np.concatenate((intcode, np.zeros(10000, dtype=np.int64))) #cheatmode

# 0 is an empty tile. No game object appears in this tile.
# 1 is a wall tile. Walls are indestructible barriers.
# 2 is a block tile. Blocks can be broken by the ball.
# 3 is a horizontal paddle tile. The paddle is indestructible.
# 4 is a ball tile. The ball moves diagonally and bounces off objects.

plt.ion()

base = 0
nextindex = 0
suboutput = []
image = np.zeros((1,1), dtype=int)
while nextindex != 99999:
    nextindex, base, output = processparam(nextindex, intcode, base)
    if output != 99999:
        suboutput.append(output)
    if len(suboutput) == 3:
        processOutput(suboutput)
        suboutput = []

output = countBlock(image)
print(output)

