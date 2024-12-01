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

    arr = []
    nums = '0123456789'


    for index in range(len(data)):
        line = data[index]

        for i in range(0, len(line)):
            if line[i] in nums:
                ans +=  10 * int(line[i])
                break

        for i in range(len(line) -1, -1, -1):
            if line[i] in nums:
                ans +=  int(line[i])
                break
        
    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    h = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'zero': 0,
            }


    nums = '0123456789'
    for index in range(len(data)):
        line = data[index]

        arr = []

        for i in range(0, len(line)):
            if line[i] in nums:
                arr.append(int(line[i]))
            else:
                for k in h:
                    if line[i:].startswith(k):
                        arr.append(k)
                        break

        if type(arr[0]) == int:
            ans += 10*arr[0]
        else:
            ans += 10*h[arr[0]]

        if type(arr[-1]) == int:
            ans += arr[-1]
        else:
            ans += h[arr[-1]]
        
    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
