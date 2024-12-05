import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key, key3, UP, DOWN, LEFT, RIGHT, dUP, dRIGHT, dDOWN, dLEFT, bound

# (714, 8445)

# could not for the life of me think of a way to do part 2 until I stumbled on this solution

download_input(os.path.abspath(os.curdir))

def is_valid(arr, rules):
    correct = True

    for b, a in rules:
        try:
            if arr.index(b) > arr.index(a):
                correct = False
        except:
            continue

    return correct

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n\n')

    ans = 0

    rules = []

    z, o = data

    for rule in z.split('\n'):
        b,a = rule.split('|')
        b = int(b)
        a = int(a)
        rules.append([b, a])

    for line in o.split('\n'):
        arr = [int(x) for x in line.split(',')]

        if is_valid(arr, rules):
            ans += arr[len(arr) // 2]

    return ans

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n\n')

    rules = []
    lh = {}
    rh = {}

    z, o = data

    for rule in z.split('\n'):
        b,a = rule.split('|')
        b = int(b)
        a = int(a)
        rules.append([b, a])

    for l, r in rules:
        if l not in lh:
            lh[l] = []
        lh[l].append(r)

        if r not in rh:
            rh[r] = []
        rh[r].append(l)

    not_correct = []

    for line in o.split('\n'):
        arr = [int(x) for x in line.split(',')]

        if not is_valid(arr, rules):
            not_correct.append(arr)

    t = []

    for arr in not_correct:

        for m in arr:
            left = []
            right = []
            non = []

            for n in arr:
                if n != m:
                    if n in lh and m in lh[n]:
                        left.append(n)
                    elif n in rh and m in rh[n]:
                        right.append(n)
                    else:
                        non.append(n)

            if len(left) + len(non) == len(right) or len(right) + len(non) == len(left):
                t.append(m)

    return sum(t)


print(f'part1: {part1()}')
print(f'part2: {part2()}')
