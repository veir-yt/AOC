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
        a, b, c = [int(x) for x in data[index].split()]
        if a + b > c and a + c > b and b + c > a:
            ans += 1
        
    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    arr = []

    aa = []
    bb = []
    cc = []

    for index in range(len(data)):
        a, b, c = [int(x) for x in data[index].split()]
        aa.append(a)
        bb.append(b)
        cc.append(c)

    for arr in [aa, bb, cc]:
        for x in range(0, len(arr), 3):
            a = arr[x]
            b = arr[x + 1]
            c = arr[x + 2]
            if a + b > c and a + c > b and b + c > a:
                ans += 1

    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')

