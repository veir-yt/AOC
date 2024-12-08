import sys
sys.path.insert(0, '../../')
import os
import math
import copy
from itertools import permutations
from helper.helper import getFile, mymap, myfilter, download_input, hash_string, hashes_equal, key, key3, UP, DOWN, LEFT, RIGHT, dUP, dRIGHT, dDOWN, dLEFT, bound, get_grid

download_input(os.path.abspath(os.curdir))

# did it the next morning, fun puzzle!
# 231774, 9134

# pretty messy, especially for part2, but it works :)

def part1():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans, x, y = 0, 0, 0

    h = {}

    grid = (get_grid(data))
            
    for i in range(len(data)):
        for j in range(len(data[i])):
            c = grid[(i,j)]
            if c != '.':
                if c not in h:
                    h[c] = []
                h[c].append((i, j))

    anti = {}

    for c in h:
        for i in range(len(h[c])):
            for j in range(i + 1, len(h[c])):
                a,b = h[c][i], h[c][j]
                dy = abs(a[0] - b[0])
                dx = abs(a[1] - b[1])

                n1 = (0,0)
                n2 = (0,0)

                highest = 'a'
                if b[0] < a[0]:
                    highest = 'b'

                leftest = 'a'
                if b[1] < a[1]:
                    leftest = 'b'

                # two possible diags

                if highest == 'a' and leftest == 'b':
                    n1 = (a[0] - dy, a[1] + dx)
                    n2 = (b[0] + dy, b[1] - dx)
                elif highest == 'b' and leftest == 'b':
                    n2 = (b[0] - dy, b[1] - dx)
                    n1 = (a[0] + dy, a[1] + dx)
                elif highest == 'a' and leftest == 'a':
                    n1 = (a[0] - dy, a[1] - dx)
                    n2 = (b[0] + dy, b[1] + dx)
                else: # b, a
                    n2 = (b[0] - dy, b[1] + dx)
                    n1 = (a[0] + dy, a[1] - dx)

                if n1 in grid:
                    anti[n1] = 0

                if n2 in grid:
                    anti[n2] = 0


    for _ in anti:
        ans += 1

    return ans 

def part2():
    data = getFile(os.path.join(os.curdir, 'input.txt')).strip()

    data = data.split('\n')

    ans, x, y = 0, 0, 0

    h = {}

    grid = (get_grid(data))
            
    for i in range(len(data)):
        for j in range(len(data[i])):
            c = grid[(i,j)]
            if c != '.':
                if c not in h:
                    h[c] = []
                h[c].append((i, j))

    anti = {}

    for c in h:
        for i in range(len(h[c])):
            for j in range(i + 1, len(h[c])):
                a,b = h[c][i], h[c][j]
                dy = abs(a[0] - b[0])
                dx = abs(a[1] - b[1])

                n1 = (0,0)
                n2 = (0,0)

                highest = 'a'
                if b[0] < a[0]:
                    highest = 'b'

                leftest = 'a'
                if b[1] < a[1]:
                    leftest = 'b'

                # two possible diags

                if highest == 'a' and leftest == 'b':
                    n1 = (a[0] - dy, a[1] + dx)
                    n2 = (b[0] + dy, b[1] - dx)
                    n3 = (a[0] + dy, a[1] - dx)
                    n4 = (b[0] - dy, b[1] + dx)
                    while n1 in grid:
                        anti[n1] = 0
                        n1 = (n1[0] - dy, n1[1] + dx)
                    while n2 in grid:
                        anti[n2] = 0
                        n2 = (n2[0] + dy, n2[1] - dx)
                    while n3 in grid:
                        anti[n3] = 0
                        n3 = (n3[0] + dy, n3[1] - dx)
                    while n4 in grid:
                        anti[n4] = 0
                        n4 = (n4[0] - dy, n4[1] + dx)
                elif highest == 'b' and leftest == 'b':
                    n2 = (b[0] - dy, b[1] - dx)
                    n1 = (a[0] + dy, a[1] + dx)
                    n3 = (a[0] - dy, a[1] - dx)
                    n4 = (b[0] + dy, b[1] + dx)
                    while n1 in grid:
                        anti[n1] = 0
                        n1 = (n1[0] + dy, n1[1] + dx)
                    while n2 in grid:
                        anti[n2] = 0
                        n2 = (n2[0] - dy, n2[1] - dx)
                    while n3 in grid:
                        anti[n3] = 0
                        n3 = (n3[0] - dy, n3[1] - dx)
                    while n4 in grid:
                        anti[n4] = 0
                        n4 = (n4[0] + dy, n4[1] + dx)
                elif highest == 'a' and leftest == 'a':
                    n1 = (a[0] - dy, a[1] - dx)
                    n2 = (b[0] + dy, b[1] + dx)
                    n3 = (a[0] + dy, a[1] + dx)
                    n4 = (b[0] - dy, b[1] - dx)
                    while n1 in grid:
                        anti[n1] = 0
                        n1 = (n1[0] - dy, n1[1] - dx)
                    while n2 in grid:
                        anti[n2] = 0
                        n2 = (n2[0] + dy, n2[1] + dx)
                    while n3 in grid:
                        anti[n3] = 0
                        n3 = (n3[0] + dy, n3[1] + dx)
                    while n4 in grid:
                        anti[n4] = 0
                        n4 = (n4[0] - dy, n4[1] - dx)
                else: # b, a
                    n2 = (b[0] - dy, b[1] + dx)
                    n1 = (a[0] + dy, a[1] - dx)
                    n3 = (a[0] - dy, a[1] + dx)
                    n4 = (b[0] + dy, b[1] - dx)
                    while n1 in grid:
                        anti[n1] = 0
                        n1 = (n1[0] + dy, n1[1] - dx)
                    while n2 in grid:
                        anti[n2] = 0
                        n2 = (n2[0] - dy, n2[1] + dx)
                    while n3 in grid:
                        anti[n3] = 0
                        n3 = (n3[0] - dy, n3[1] + dx)
                    while n4 in grid:
                        anti[n4] = 0
                        n4 = (n4[0] + dy, n4[1] - dx)

    for _ in anti:
        ans += 1

    return ans 

print(f'part1: {part1()}')
print(f'part2: {part2()}')
