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

    x, y = 0, 0
    dir = 0

    for index in range(len(data)):
        line = data[index]

        for move in line.split(', '):
            d = move[0]
            n = int(move[1:])

            if d == 'R':
                dir += 1
            else:
                dir -= 1

            if dir == 4:
                dir = 0
            if dir == -1:
                dir = 3

            if dir == 0:
                x += n
            elif dir == 1:
                y += n
            if dir == 2:
                x -= n
            elif dir == 3:
                y -= n

    return abs(x) + abs(y) 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    x, y = 0, 0
    dir = 0

    h = {}

    for index in range(len(data)):
        line = data[index]

        for move in line.split(', '):

            d = move[0]
            n = int(move[1:])

            if d == 'R':
                dir += 1
            else:
                dir -= 1

            if dir == 4:
                dir = 0
            if dir == -1:
                dir = 3

            dx = 0
            dy = 0

            if dir == 0:
                dx = 1
            elif dir == 1:
                dy = 1
            if dir == 2:
                dx = -1
            elif dir == 3:
                dy = -1

            for i in range(n):
                if (x, y) in h:
                    return abs(x) + abs(y)
                h[(x,y)] = 0
                x += dx
                y += dy


print(f'part1: {part1()}')
print(f'part2: {part2()}')
