# Advent of Code 2019
# Day 11 - part 1 and 2
# Hessel Prins
import numpy as np
from matplotlib import pyplot as plt

def processparam(index, intcode, base, colour,):
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

def createBackground(ax):
    minx, miny = ax[0]
    maxx, maxy = ax[1]
    
    xrow = range(minx, maxx + 1)
    ycol = range(miny, maxy + 1)

    x = np.tile(xrow, len(ycol))
    y = np.repeat(ycol, len(xrow))
    c = np.zeros(len(y))

    return x, y, c

day = 11

intcode = np.genfromtxt('./Day_'+ str(day) + '/input.txt', delimiter=',').astype(np.int64)

intcode = np.concatenate((intcode, np.zeros(10000, dtype=np.int64))) #cheatmode

nextindex = 0
base = 0
heading = 0
steps = 0
orientation = {0:[0, 1], 90:[1, 0], 180:[0, -1], 270:[-1, 0]}
x, y = [0, 0]
part = 2
if part == 2:
    painted = [[x, y]]
    coloured = [1]
else:
    painted = []
    coloured = []
end = False
while nextindex != 99999:
    if [x, y] not in painted:
        colour = 0
    else:
        colour = coloured[painted.index([x, y])]
    output = []
    while len(output) < 2:
        nextindex, base, paramoutput = processparam(nextindex, intcode, base, colour)
        if paramoutput != 99999:
            output.append(paramoutput)
        if nextindex == 99999:
            end = True
            break
    if end:
        break
    newcolour = output[0]
    if [x, y] not in painted:
        painted.append([x, y])
        coloured.append(newcolour)
    else:
        coloured[painted.index([x, y])] = newcolour
    heading = (heading + ((-1)**output[1] * -90)) % 360
    loc = np.add([x, y], orientation[heading])
    x, y = loc
    steps += 1

print('painted once: ', len(painted))
print('total: ', steps)


ax = [np.min(painted, 0), np.max(painted, 0)]
bx, by, bc =  createBackground(ax)
plt.figure()
plt.scatter(bx, by, s=5, c=bc)
plt.scatter(*zip(*painted), s=5, c=coloured)
plt.show()


