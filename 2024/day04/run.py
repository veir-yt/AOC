import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key, key3, UP, DOWN, LEFT, RIGHT, dUP, dRIGHT, dDOWN, dLEFT, bound

download_input(os.path.abspath(os.curdir))

# pretty happy once I had a half baked solution lol

# (1462, 696)

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    h = {}

    for i in range(len(data)):
        for j in range(len(data[0])):
            h[(i, j)] = data[i][j]

    for i in range(len(data)):
        for j in range(len(data[0])):

            # horiz
            if check(h, i, j + 0, 'X') and check(h, i, j + 1, 'M') and check(h, i, j + 2, 'A') and check(h, i, j + 3, 'S'):
                ans += 1
            if check(h, i, j - 0, 'X') and check(h, i, j - 1, 'M') and check(h, i, j - 2, 'A') and check(h, i, j - 3, 'S'):
                ans += 1

            # vert
            if check(h, i + 0, j, 'X') and check(h, i + 1, j, 'M') and check(h, i + 2, j, 'A') and check(h, i + 3, j, 'S'):
                ans += 1
            if check(h, i - 0, j, 'X') and check(h, i - 1, j, 'M') and check(h, i - 2, j, 'A') and check(h, i - 3, j, 'S'):
                ans += 1

            # diag
            if check(h, i, j, 'X') and check(h, i + 1, j + 1, 'M') and check(h, i + 2, j + 2, 'A') and check(h, i + 3, j + 3, 'S'):
                ans += 1
            if check(h, i, j, 'X') and check(h, i - 1, j - 1, 'M') and check(h, i - 2, j - 2, 'A') and check(h, i - 3, j - 3, 'S'):
                ans += 1
            if check(h, i, j, 'X') and check(h, i + 1, j - 1, 'M') and check(h, i + 2, j - 2, 'A') and check(h, i + 3, j - 3, 'S'):
                ans += 1
            if check(h, i, j, 'X') and check(h, i - 1, j + 1, 'M') and check(h, i - 2, j + 2, 'A') and check(h, i - 3, j + 3, 'S'):
                ans += 1

    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    h = {}

    for i in range(len(data)):
        for j in range(len(data[0])):
            h[(i, j)] = data[i][j]

    for i in range(len(data)):
        for j in range(len(data[0])):

            # all cross shapes
            if check(h, i, j, 'A'):
                if check(h, i + 1, j + 1, 'M') and check(h, i - 1, j - 1, 'S') and check(h, i + 1, j - 1, 'M') and check(h, i - 1, j + 1, 'S'):
                    ans += 1
                if check(h, i + 1, j + 1, 'S') and check(h, i - 1, j - 1, 'M') and check(h, i + 1, j - 1, 'M') and check(h, i - 1, j + 1, 'S'):
                    ans += 1
                if check(h, i + 1, j + 1, 'S') and check(h, i - 1, j - 1, 'M') and check(h, i + 1, j - 1, 'S') and check(h, i - 1, j + 1, 'M'):
                    ans += 1
                if check(h, i + 1, j + 1, 'M') and check(h, i - 1, j - 1, 'S') and check(h, i + 1, j - 1, 'S') and check(h, i - 1, j + 1, 'M'):
                    ans += 1

    return ans 

def check(h, i, j, l):
    if (i, j) not in h:
        return False
    return h[(i, j)] == l

print(f'ans: {part1()}')
print(f'ans: {part2()}')

