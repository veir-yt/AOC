import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key, key3, UP, DOWN, LEFT, RIGHT, dUP, dRIGHT, dDOWN, dLEFT, bound, get_grid

# started late, pretty happy
# 6959, 5582

download_input(os.path.abspath(os.curdir))

h = {}
h2 = {}

def is_valid(i, num, c, arr):
    if not len(arr):
        if c == num:
            global h
            h[i] = c # could have multiple answers, need to hash or stop
        return c == num
    
    return is_valid(i, num, c + arr[0], arr[1:]) or is_valid(i, num, c * arr[0], arr[1:])
    
def is_valid2(i, num, c, arr):
    if not len(arr):
        if c == num:
            global h2
            h2[i] = c # could have multiple answers, need to hash or stop
        return c == num
    
    return is_valid2(i, num, c + arr[0], arr[1:]) or is_valid2(i, num, c * arr[0], arr[1:]) or is_valid2(i, num, int(str(c) + str(arr[0])), arr[1:])

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    for index in range(len(data)):
        line = data[index]

        big, end = line.split(': ')
        big = int(big)
        end = [int(x) for x in end.split()]

        is_valid(index, big, end[0], end[1:])
        
    ans = 0
    global h

    for k in h:
        ans += h[k]

    return ans

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    for index in range(len(data)):
        line = data[index]

        big, end = line.split(': ')
        big = int(big)
        end = [int(x) for x in end.split()]

        is_valid2(index, big, end[0], end[1:])

    ans = 0
    global h2

    for k in h2:
        ans += h2[k]

    return ans

print(f'part1: {part1()}')
print(f'part2: {part2()}')

