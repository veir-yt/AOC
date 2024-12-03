import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key, key3, UP, DOWN, LEFT, RIGHT, dUP, dRIGHT, dDOWN, dLEFT, bound

download_input(os.path.abspath(os.curdir))

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans, x, y = 0, 0, 0

    h = {}

    line = data[0]

    for foo in line:
        h[(x,y)] = 0

        if foo == '^':
            y += 1
        elif foo == '>':
            x += 1
        elif foo == '<':
            x -= 1
        else:
            y -= 1

    for k in h:
        ans += 1
        
    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans, x, y = 0, 0, 0
    x1, y1 = 0, 0

    h = {}

    line = data[0]

    for ii in range(len(line)):
        foo = line[ii]

        h[(x,y)] = 0
        h[(x1,y1)] = 0

        if foo == '^':
            if ii % 2 == 0:
                y += 1
            else:
                y1 += 1
        elif foo == '>':
            if ii % 2 == 0:
                x += 1
            else:
                x1 += 1
        elif foo == '<':
            if ii % 2 == 0:
                x -= 1
            else:
                x1 -= 1
        else:
            if ii % 2 == 0:
                y -= 1
            else:
                y1 -= 1

    for k in h:
        ans += 1
        
    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
