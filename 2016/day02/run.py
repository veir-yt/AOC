import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key, key3, UP, DOWN, LEFT, RIGHT, dUP, dRIGHT, dDOWN, dLEFT

download_input(os.path.abspath(os.curdir))

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = ''
    x, y = 1, 1

    for index in range(len(data)):
        line = data[index]
        # arr.append(int(line))

        for c in line:
            dx, dy = 0, 0
            if c == 'U':
                (dy, dx) = UP
            elif c == 'D':
                (dy, dx) = DOWN
            elif c == 'R':
                (dy, dx) = RIGHT
            elif c == 'L':
                (dy, dx) = LEFT

            x += dx
            y += dy
            if x < 0:
                x = 0
            if y < 0:
                y = 0
            if x > 2:
                x = 2
            if y > 2:
                y = 2

        ans += ['123', '456', '789'][y][x]
        
    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = ''
    x, y = 1, 1

    h = {}
    h[(0, 0)] = '1'
    h[(1, -1)] = '2'
    h[(1, 0)] = '3'
    h[(1, 1)] = '4'
    h[(2, -2)] = '5'
    h[(2, -1)] = '6'
    h[(2, 0)] = '7'
    h[(2, 1)] = '8'
    h[(2, 2)] = '9'
    h[(3, -1)] = 'A'
    h[(3, 0)] = 'B'
    h[(3, 1)] = 'C'
    h[(4, 0)] = 'D'

    for index in range(len(data)):
        line = data[index]
        # arr.append(int(line))

        for c in line:
            dx, dy = 0, 0
            if c == 'U':
                (dy, dx) = UP
            elif c == 'D':
                (dy, dx) = DOWN
            elif c == 'R':
                (dy, dx) = RIGHT
            elif c == 'L':
                (dy, dx) = LEFT

            x += dx
            y += dy

            if (y, x) not in h:
                x -= dx
                y -= dy

        ans += h[(y, x)]
        
    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
