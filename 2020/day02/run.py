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
        line = data[index]

        _min = int(line.split('-')[0])
        _max = int(line.split('-')[1].split(' ')[0])
        letter = (line.split(':')[0].split(' ')[1])
        pw = (line.split(' ')[2])

        h = hash_string(pw)

        if letter not in h:
            continue

        if h[letter] >= _min and h[letter] <= _max:
            ans += 1

    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans = 0

    for index in range(len(data)):
        line = data[index]

        _min = int(line.split('-')[0])
        _max = int(line.split('-')[1].split(' ')[0])
        letter = (line.split(':')[0].split(' ')[1])
        pw = (line.split(' ')[2])

        if (pw[_min - 1] == letter) ^ (pw[_max - 1] == letter):
            ans += 1

    return ans

print(f'part1: {part1()}')
print(f'part2: {part2()}')
