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

    ops = [int(x) for x in data[0].split(',')]

    ops[1] = 12
    ops[2] = 2

    for i in range(0, len(ops) - 4, 4):
        op, in1, in2, out1 = ops[i] , ops[i + 1] , ops[i + 2] , ops[i + 3]

        if op == 99:
            break

        v1 = ops[in1]
        v2 = ops[in2]

        v = None

        if op == 1:
            v = v1 + v2
        else:
            v = v1 * v2

        ops[out1] = v

    return ops[0]

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    yes = 19690720

    ops = [int(x) for x in data[0].split(',')]

    _ops = copy.deepcopy(ops)

    for ii in range(0, 100):
        for jj in range(0, 100):
            ops = copy.deepcopy(_ops)

            ops[1] = ii
            ops[2] = jj

            for i in range(0, len(ops) - 4, 4):
                op, in1, in2, out1 = ops[i] , ops[i + 1] , ops[i + 2] , ops[i + 3]

                if op == 99:
                    break

                v1 = ops[in1]
                v2 = ops[in2]

                v = None

                if op == 1:
                    v = v1 + v2
                else:
                    v = v1 * v2

                ops[out1] = v

            if ops[0] == yes:
                return 100 * ii + jj

print(f'part1: {part1()}')
print(f'part2: {part2()}')
