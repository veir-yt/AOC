import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key, key3, UP, DOWN, LEFT, RIGHT, dUP, dRIGHT, dDOWN, dLEFT, bound

download_input(os.path.abspath(os.curdir))

# 12 red cubes, 13 green cubes, and 14 blue cubes?
# pretty sloppy

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans, x, y = 0, 0, 0

    arr = []

    h = {}

    for index in range(len(data)):
        b, a = data[index].split(': ')
        id = b.split(' ')[1]
        games = a.split('; ')

        valid = True

        for game in games:
            foo = game.split(', ')

            for bar in foo:
                n, c = bar.split()
                n = int(n)
                if c == 'red':
                    if n > 12:
                        valid = False
                elif c == 'green':
                    if n > 13:
                        valid = False
                elif c == 'blue':
                    if n > 14:
                        valid = False
                else:
                    valid = False

        if valid:
            ans += int(id)
        
    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans, x, y = 0, 0, 0

    arr = []

    h = {}

    for index in range(len(data)):
        b, a = data[index].split(': ')
        id = b.split(' ')[1]
        games = a.split('; ')

        valid = True

        r = 0
        g = 0
        b = 0
        for game in games:
            foo = game.split(', ')

            for bar in foo:
                n, c = bar.split()
                n = int(n)
                if c == 'red':
                    if r == None:
                        r = n
                    r = max(r, n)
                elif c == 'green':
                    if g == None:
                        g = n
                    g = max(g, n)
                elif c == 'blue':
                    if b == None:
                        b = n
                    b = max(b, n)

        if r != None and b != None and g != None:
            ans += r * g * b
        
    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
