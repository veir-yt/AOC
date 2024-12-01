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

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == 2020:
                return arr[i] * arr[j]
    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    arr = []

    for index in range(len(data)):
        line = data[index]
        arr.append(int(line))

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == 2020:
                    return arr[i] * arr[j] * arr[k]
    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
