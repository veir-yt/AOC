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

    data = data.split('\n\n')

    arr = []

    for index in range(len(data)):
        line = data[index]

        t = 0

        for l in line.split('\n'):
            t += int(l)
        arr.append(t)
        
    return max(arr)

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n\n')

    arr = []

    for index in range(len(data)):
        line = data[index]

        t = 0

        for l in line.split('\n'):
            t += int(l)
        arr.append(t)

    arr.sort()

    return arr[-1] + arr[-2] + arr[-3]

print(f'part1: {part1()}')
print(f'part2: {part2()}')
