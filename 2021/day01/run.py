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
        arr.append(int(line))

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            ans += 1
        
    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    arr = []

    for index in range(len(data)):
        line = data[index]
        arr.append(int(line))

    for i in range(3, len(arr)):
        if arr[i] > arr[i - 3]:
            ans += 1
        
    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
