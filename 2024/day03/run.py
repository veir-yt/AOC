import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key, key3, UP, DOWN, LEFT, RIGHT, dUP, dRIGHT, dDOWN, dLEFT, bound

download_input(os.path.abspath(os.curdir))

# so bad, didn't catch that there were multiple lines, not just one big line
# my boilerplate really hurt me here

# (10627 6306)

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans  = 0

    for line in data:
        for i in range(len(line)):
            t = line[i:]
            if t.startswith('mul('):
                x = t.split('mul(')[1].split(')')[0]
                if len(x.split(',')) == 2:
                    if ' ' in x or '\t' in x:
                        continue
                    b,a = x.split(',')
                    try:
                        b = int(b)
                        a = int(a)
                    except:
                        continue
                    ans += b*a
    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans  = 0

    enabled = True

    for line in data:
        for i in range(len(line)):
            t = line[i:]
            if t.startswith('do()'):
                enabled = True
            if t.startswith("don't()"):
                enabled = False

            if t.startswith('mul(') and enabled:
                x = t.split('mul(')[1].split(')')[0]
                if len(x.split(',')) == 2:
                    if ' ' in x or '\t' in x:
                        continue
                    b,a = x.split(',')
                    try:
                        b = int(b)
                        a = int(a)
                    except:
                        continue
                    ans += b*a
    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
