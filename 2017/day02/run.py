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

    ans = 0

    for index in range(len(data)):
        line = data[index]
        # arr.append(int(line))
        arr = []

        line = line.split('\t')
        for x in line:
            arr.append(int(x))

        ans += max(arr) - min(arr)
        
    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    for index in range(len(data)):
        line = data[index]
        # arr.append(int(line))
        arr = []

        line = line.split('\t')
        for x in line:
            arr.append(int(x))

        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                if i == j:
                    continue
                if arr[i] % arr[j] == 0:
                    ans += arr[i] // arr[j]

    return ans

print(f'part1: {part1()}')
print(f'part2: {part2()}')
