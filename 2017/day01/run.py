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

    for index in range(len(data)):
        line = data[index]
        line += line[0]

        for i in range(1, len(line)):
            if line[i] == line[i - 1]:
                ans += int(line[i])
        
    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    for index in range(len(data)):
        line = data[index]
        line += line

        for i in range(0, len(line) // 4):
            if line[i] == line[i + (len(line) // 4)]:
                ans += int(line[i])
        
    return ans * 2 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
