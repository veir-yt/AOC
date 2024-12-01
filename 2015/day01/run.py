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
    print(data)

    ans = 0

    for index in range(len(data)):
        line = data[index]

        for c in line:
            if c == ')':
                ans -= 1
            else:
                ans += 1
        
    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')
    print(data)

    ans = 0

    for index in range(len(data)):
        line = data[index]

        for i in range(len(line)):
            c = line[i]
            if c == ')':
                ans -= 1
            else:
                ans += 1

            if ans == -1:
                return i + 1

print(f'part1: {part1()}')
print(f'part2: {part2()}')

