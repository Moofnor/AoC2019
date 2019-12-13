# Advent of Code 2019
# Day 12 part 1
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

def calculateEnergy(moons):
    tot = 0
    for m in moons:
        pot = sum(np.abs(moons[m].pos))
        kin = sum(np.abs(moons[m].vel))
        tot += pot * kin
    return tot

class moon:
    def __init__(self, pos):
        self.pos = pos
        self.vel = [0, 0, 0]
    def stats(self):
        print('pos: ', self.pos, ', vel: ', self.vel)


day = 12
filename = './Day_'+ str(day) + '/input.txt'
data = readInput(filename)
moons = createMoons(data)
for i in range(1000):
    updateVel(moons)
    updatePos(moons)
    if i+1 in [5, 10, 50, 100, 500, 1000]:
        print('After ', i+1, ' steps:')
        for m in moons:
            moons[m].stats()
        print('Energy: ', calculateEnergy(moons))


