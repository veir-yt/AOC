import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key, key3, UP, DOWN, LEFT, RIGHT, dUP, dRIGHT, dDOWN, dLEFT, bound, get_grid

download_input(os.path.abspath(os.curdir))

# started like an hour late, similar to laternfish problem, just need to cache from start
# 11343, 5996

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    h = {}

    line = data[0].split()
    line = [int(x) for x in data[0].split()]

    for x in line:
        if x not in h:
            h[x] = 0
        h[x] += 1

    for _ in range(25):
        nh = {}
        for k in h:
            if k == 0:
                if 1 not in nh:
                    nh[1] = 0
                nh[1] += h[k]
            elif len(str(k)) % 2 == 0:
                a = int(str(k)[:len(str(k)) // 2])
                b = int(str(k)[len(str(k)) // 2:])
                if a not in nh:
                    nh[a] = 0
                nh[a] += h[k]
                if b not in nh:
                    nh[b] = 0
                nh[b] += h[k]
            else:
                c = 2024 * k
                if c not in nh:
                    nh[c] = 0
                nh[c] += h[k]

        h = copy.deepcopy(nh)

    for k in h:
        ans += h[k]
        
    return ans


def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    h = {}

    line = data[0].split()
    line = [int(x) for x in data[0].split()]

    for x in line:
        if x not in h:
            h[x] = 0
        h[x] += 1

    for _ in range(75):
        nh = {}
        for k in h:
            if k == 0:
                if 1 not in nh:
                    nh[1] = 0
                nh[1] += h[k]
            elif len(str(k)) % 2 == 0:
                a = int(str(k)[:len(str(k)) // 2])
                b = int(str(k)[len(str(k)) // 2:])
                if a not in nh:
                    nh[a] = 0
                nh[a] += h[k]
                if b not in nh:
                    nh[b] = 0
                nh[b] += h[k]
            else:
                c = 2024 * k
                if c not in nh:
                    nh[c] = 0
                nh[c] += h[k]

        h = copy.deepcopy(nh)

    for k in h:
        ans += h[k]
        
    return ans

print(f'part1: {part1()}')
print(f'part2: {part2()}')
