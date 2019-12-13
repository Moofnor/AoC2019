# Advent of Code 2019
# Day 12 part 2
# Hessel Prins
import numpy as np
from itertools import combinations

def readInput(filename):
    with open(filename, 'r') as f:
        rows = [[int(x.split('=')[1]) for x in line.rstrip('>\n').lstrip('<').split(',')] for line in f]
    return rows

def createMoons(data):
    moons = {}
    for i, row in enumerate(data):
        moons[i] = moon(row)
    return moons

def updateVel(moons):
    pairs = combinations(moons,2)
    for pair in pairs:
        m1 = moons[pair[0]]
        m2 = moons[pair[1]]
        for ax in range(3):
            if m1.pos[ax] > m2.pos[ax]:
                m1.vel[ax] -= 1
                m2.vel[ax] += 1
            elif m1.pos[ax] < m2.pos[ax]:
                m1.vel[ax] += 1
                m2.vel[ax] -= 1

def updatePos(moons):
    for m in moons:
        moons[m].pos = np.add(moons[m].pos, moons[m].vel)

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(array):
    a = array[0]
    if len(array) > 2:
        b = lcm(array[1:])
    else:
        b = array[1]
    return a * b / gcd(a, b)

def getAxData(ax, moons):
    pos = []
    vel = []
    for m in moons:
        pos.append(moons[m].pos[ax])
        vel.append(moons[m].vel[ax])
    return pos, vel

class moon:
    def __init__(self, pos):
        self.pos = pos
        self.initpos = pos
        self.vel = [0, 0, 0]
    def stats(self):
        print('pos: ', self.pos, ', vel: ', self.vel)


day = 12
filename = './Day_'+ str(day) + '/input.txt'
data = readInput(filename)

moons = createMoons(data)
time = 0
phases = np.zeros(3)
initpos, initvel = [], []
for ax in range(3):
    pos, vel = getAxData(ax, moons)
    initpos.append(pos)
    initvel.append(vel)

while 0 in phases:
    time += 1
    updateVel(moons)
    updatePos(moons)

    for ax in range(3):
        pos, vel = getAxData(ax, moons)
        if np.array_equiv(pos,initpos[ax]) and np.array_equiv(vel,initvel[ax]) and phases[ax] == 0:
            print('Phase found')
            phases[ax] = time

    if time > 10000000:
        print('Time out')
        print(phases)
        break

output = lcm(phases)
print(output)
