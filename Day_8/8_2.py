# Advent of Code 2019
# Day 8 - Part 2
# Hessel Prins
import numpy as np
from matplotlib import pyplot as plt

def readinput(filename, img_size):
    with open(filename, 'r') as f:
        line = f.readlines()[0]
        n_layers = int(len(line) / np.prod(img_size))
        img_pixels = np.zeros((n_layers, img_size[0], img_size[1]))
        for i, char in enumerate(line):
            n, x, y = [np.floor((i / np.prod(img_size))), i % img_size[0], int(i / img_size[0]) % img_size[1]]
            img_pixels[int(n)][x][y] = int(char)
    return img_pixels

def findImage(img_pixels):
    n_layers = img_pixels.shape[0]
    image = np.ones((img_pixels.shape[1:])) * 2
    for x in range(img_pixels.shape[1]):
        for y in range(img_pixels.shape[2]):
            n = 0
            while img_pixels[n][x][y] == 2:
                n += 1
            image[x][y] = img_pixels[n][x][y]
    return image

day = 8

filename = './Day_'+ str(day) + '/input.txt'
img_size = [25, 6]

img_pixels = readinput(filename, img_size)
image = findImage(img_pixels)

plt.figure()
plt.imshow(image.T)
plt.show()
