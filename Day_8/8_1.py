# Advent of Code 2019
# Day 8 - Part 1
# Hessel Prins
import numpy as np
from matplotlib import pyplot as plt

def readinput(filename, img_size):
    with open(filename, 'r') as f:
        line = f.readlines()[0]
        n_layers = int(len(line) / np.prod(img_size))
        img_pixels = np.zeros((n_layers, img_size[0], img_size[1]))
        for i, char in enumerate(line):
            n, x, y = [int(i / np.prod(img_size)), i % img_size[0], i % img_size[1]]
            img_pixels[n][x][y] = int(char)
    return img_pixels

def countDigits(img_pixels):
    n_layers = img_pixels.shape[0]
    n_digits = np.zeros((3, n_layers))
    for i, n in enumerate(img_pixels):
        row = n.reshape((np.prod(n.shape),))
        for x in row:
            n_digits[int(x)][i] += 1
    return n_digits

day = 8

filename = './Day_'+ str(day) + '/input.txt'
img_size = [25, 6]

img_pixels = readinput(filename, img_size)
n_digits = countDigits(img_pixels)
n_zeros = n_digits[0]
minimum = np.where(n_zeros == min(n_zeros) )
output = n_digits[1][minimum] * n_digits[2][minimum]
print(output)

