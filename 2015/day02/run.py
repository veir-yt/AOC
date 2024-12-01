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

    ans = 0

    arr = []

    for index in range(len(data)):
        line = data[index]
        # arr.append(int(line))

        l, w, h = line.split('x')
        l = int(l)
        w = int(w)
        h = int(h)

        ans += 2 * (l*w + l*h + h*w) + min(l*w, l*h, h*w)
        
    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    arr = []

    for index in range(len(data)):
        line = data[index]
        # arr.append(int(line))

        l, w, h = line.split('x')
        l = int(l)
        w = int(w)
        h = int(h)

        x = ((l + w + h) - max(l, w, h))
        ans += (l*w*h) + 2 * x
        
    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
