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

    two_count = 0
    three_count = 0

    arr = []

    for index in range(len(data)):
        line = data[index]
        # arr.append(int(line))
        h = hash_string(line)

        for k in h:
            if h[k] == 2:
                two_count += 1
                break

        for k in h:
            if h[k] == 3:
                three_count += 1
                break
        
    return two_count * three_count 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    arr = []

    for index in range(len(data)):
        line = data[index]
        arr.append(line)

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            ans = ''
            for k in range(len(arr[i])):
                if arr[i][k] == arr[j][k]:
                    ans += arr[i][k]

            if len(ans) == len(arr[i]) - 1:
                return ans

print(part1())
print(part2())
