import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key, key3, UP, DOWN, LEFT, RIGHT, dUP, dRIGHT, dDOWN, dLEFT, bound

download_input(os.path.abspath(os.curdir))

# brutal, server crash, and I can't read

# (2849, 3288)

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans, x, y = 0, 0, 0


    for index in range(len(data)):
        line = data[index].split()
        a = [int(x) for x in line]

        all_inc = True
        for i in range(1, len(a)):
            if a[i] > a[i - 1] + 3 or a[i] <= a[i - 1]:
                all_inc = False

        all_dec = True
        for i in range(1, len(a)):
            if a[i] < a[i - 1] - 3 or a[i] >= a[i - 1]:
                all_dec = False

        if all_inc or all_dec:
            ans += 1
        
    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans, x, y = 0, 0, 0

    for index in range(len(data)):
        line = data[index].split()
        a = [int(x) for x in line]
        aa = copy.deepcopy(a)

        any1 = False
        for j in range(0, len(aa)):
            a = copy.deepcopy(aa)
            a.pop(j)

            valid = True

            for i in range(1, len(a)):
                if a[i] > a[i - 1] + 3 or a[i] <= a[i - 1]:
                    valid = False
            if valid:
                any1 = True
                break

        any2 = False
        for j in range(0, len(aa)):
            a = copy.deepcopy(aa)
            a.pop(j)

            valid = True

            for i in range(1, len(a)):
                if a[i] < a[i - 1] - 3 or a[i] >= a[i - 1]:
                    valid = False
            if valid:
                any2 = True
                break

        if any1 or any2:
            ans += 1
        
    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
