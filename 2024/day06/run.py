import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key, key3, UP, DOWN, LEFT, RIGHT, dUP, dRIGHT, dDOWN, dLEFT, bound

download_input(os.path.abspath(os.curdir))

# (3907, 1900), honestly really sloppy, should probably make grid helper

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans, x, y = 0, 0, 0

    h = {}

    for i in range(len(data)):
        line = data[i]
        for j in range(len(line)):
            h[(i, j)] = line[j]
            if line[j] == '^':
                x = j
                y = i

    d = 0
    dirs = [UP, RIGHT, DOWN, LEFT]

    h[(y, x)] = '.'

    vis = {}
    vis[(y, x)] = 0

    while (y, x) in h:
        dy, dx = dirs[d]

        x += dx
        y += dy

        while (y, x) in h and h[(y, x)] == '.':
            vis[(y,x)] = 0
            x += dx
            y += dy
        if (y, x) not in h:
            break
        x -= dx
        y -= dy
        d += 1
        if d == 4:
            d = 0

    for k in vis:
        ans += 1
        
    return ans

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans, x, y = 0, 0, 0

    h = {}

    for i in range(len(data)):
        line = data[i]
        for j in range(len(line)):
            h[(i, j)] = line[j]
            if line[j] == '^':
                x = j
                y = i

    startx = x
    starty = y

    dirs = [UP, RIGHT, DOWN, LEFT]

    for k in range(len(data)):
        for l in range(len(data)):

            if h[(k, l)] != '.':
                continue
            if k == starty and l == startx:
                continue

            h[(k, l)] = '#'

            y = starty
            x = startx

            d = 0
            h[(starty, startx)] = '.'

            vis = {}
            vis[(y, x, d)] = 0

            in_loop = False
            while (y, x) in h:
                dy, dx = dirs[d]

                x += dx
                y += dy

                while (y, x) in h and h[(y, x)] == '.':
                    if (y,x,d) in vis:
                        in_loop = True
                    vis[(y,x,d)] = 0
                    x += dx
                    y += dy
                if in_loop:
                    break
                if (y, x) not in h:
                    break
                x -= dx
                y -= dy
                d += 1
                if d == 4:
                    d = 0
            if in_loop:
                ans += 1
            h[(k, l)] = '.'

    return ans

print(f'ans1: {part1()}')
print(f'ans2: {part2()}')
