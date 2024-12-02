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

    x, y = 0, 0

    for index in range(len(data)):
        dir, n = data[index].split()
        n = int(n)

        if dir == 'forward':
            x += n
        elif dir == 'down':
            y += n
        else:
            y -= n
        
    return x * y

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    x, y = 0, 0
    aim = 0

    for index in range(len(data)):
        dir, n = data[index].split()
        n = int(n)

        if dir == 'forward':
            x += n
            y += aim * n
        elif dir == 'down':
            aim += n
        else:
            aim -= n
        
    return x * y

print(f'part1: {part1()}')
print(f'part2: {part2()}')
