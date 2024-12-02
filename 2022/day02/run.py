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

    ans, x, y = 0, 0, 0

    arr = []

    h = {}

    for index in range(len(data)):
        op, me = data[index].split()

        if me == 'X':
            ans += 1
            if op == 'A':
                ans += 3
            if op == 'B':
                ans += 0
            if op == 'C':
                ans += 6
        if me == 'Y':
            ans += 2
            if op == 'A':
                ans += 6
            if op == 'B':
                ans += 3
            if op == 'C':
                ans += 0
        if me == 'Z':
            ans += 3
            if op == 'A':
                ans += 0
            if op == 'B':
                ans += 6
            if op == 'C':
                ans += 3

    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans, x, y = 0, 0, 0

    arr = []

    h = {}

    for index in range(len(data)):
        op, me = data[index].split()

        if me == 'Y':
            if op == 'A':
                me = 'X'
            elif op == 'B':
                me = 'Y'
            else:
                me = 'Z'
        elif me == 'X':
            if op == 'A':
                me = 'Z'
            elif op == 'B':
                me = 'X'
            else:
                me = 'Y'
        elif me == 'Z':
            if op == 'A':
                me = 'Y'
            elif op == 'B':
                me = 'Z'
            else:
                me = 'X'

        if me == 'X':
            ans += 1
            if op == 'A':
                ans += 3
            if op == 'B':
                ans += 0
            if op == 'C':
                ans += 6
        elif me == 'Y':
            ans += 2
            if op == 'A':
                ans += 6
            if op == 'B':
                ans += 3
            if op == 'C':
                ans += 0
        else:
            ans += 3
            if op == 'A':
                ans += 0
            if op == 'B':
                ans += 6
            if op == 'C':
                ans += 3

    return ans

print(f'part1: {part1()}')
print(f'part2: {part2()}')
