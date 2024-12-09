import sys
from typing import List
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key, key3, UP, DOWN, LEFT, RIGHT, dUP, dRIGHT, dDOWN, dLEFT, bound, get_grid

download_input(os.path.abspath(os.curdir))

# 217, 2045
# pretty happy with part 1, didn't really read part 2 right, then was dumb

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans, x = 0, 0

    arr = []

    line = data[0]
    line = [int(x) for x in line]

    id = 0
    for i in range(len(line)):
        c = line[i]
        if i % 2 == 0:
            for _ in range((c)):
                arr.append(id)
            id += 1
        else:
            for _ in range((c)):
                arr.append(-1)

    l = 0
    while -1 in arr:
        if arr[l] == -1:
            x = arr.pop()
            while x == -1:
                x = arr.pop()
            arr[l] = x
        l += 1

    for i in range(len(arr)):
        ans += arr[i] * i
        
    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    arr = []

    line = data[0]
    line = [int(x) for x in line]

    id = 0
    for i in range(len(line)):
        c = line[i]
        if i % 2 == 0:
            arr.append([c, id])
            id += 1
        else:
            arr.append([c, -1])

    j = len(arr) - 1
    while j >= 0:
        if arr[j][1] == -1:
            j -= 1
            continue
        for l in range(0, j):
            if arr[l][1] == -1 and arr[j][0] <= arr[l][0]:
                diff = arr[l][0] - arr[j][0]
                arr[l] = copy.deepcopy(arr[j])
                arr[j][1] = -1
                if diff > 0:
                    arr.insert(l + 1, [diff, -1])
                    j += 1
                break
        j -= 1

    narr = []
    for foo in arr:
        for _ in range(foo[0]):
            narr.append(foo[1])

    for i in range(len(narr)):
        if narr[i] != -1:
            ans += narr[i] * i

    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')

