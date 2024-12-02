import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key, key3, UP, DOWN, LEFT, RIGHT, dUP, dRIGHT, dDOWN, dLEFT, bound

download_input(os.path.abspath(os.curdir))

# didn't split the right way

# (714, 698)

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    arr1 = []
    arr2  = []

    for index in range(len(data)):
        line = data[index]

        b, e = line.split('   ') # tricky tricky
        b = int(b)
        e = int(e)

        arr1.append(b)
        arr2.append(e)

    arr1.sort()
    arr2.sort()

    for i in range(len(arr1)):
        ans += abs(arr1[i] - arr2[i]) 

    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    arr1 = []
    arr2  = []

    for index in range(len(data)):
        line = data[index]

        b, e = line.split('   ')
        b = int(b)
        e = int(e)

        arr1.append(b)
        arr2.append(e)

    h = {}

    # making "hash" of frequency of nums in arr2, called h
    for n in arr2:
        if n not in h:
            h[n] = 0
        h[n] += 1

    for n in arr1:
        if n in h:
            ans += n * h[n] # from contest

    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
